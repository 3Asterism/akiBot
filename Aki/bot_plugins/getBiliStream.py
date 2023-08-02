import json
from datetime import datetime

import jsonpath
import nonebot
import requests
from nonebot import on_command
import mysql.connector
from PIL import Image, ImageDraw, ImageFont


def save_records_as_image_with_auto_adaptation(records, filename, background_image_path):
    # 加载背景图片并获取其尺寸
    background_image = Image.open(background_image_path)
    background_width, background_height = background_image.size

    # 获取记录文本图片的尺寸
    text_width, text_height = 1200, 800

    # 选择较大的宽度和高度作为输出图片的尺寸
    image_width = max(background_width, text_width)
    image_height = max(background_height, text_height)

    # 创建新图片，并将背景图片作为底层图像
    image = Image.new('RGBA', (image_width, image_height), color=(255, 255, 255, 0))
    image.paste(background_image, (0, 0))

    # 初始化绘制对象
    draw = ImageDraw.Draw(image)

    # 定义字体和字体大小
    font_path = r'C:\Windows\Fonts\msyhbd.ttc'
    font = ImageFont.truetype(font_path, 24)

    # 设置绘制记录的起始位置
    x = 50
    y = 50

    # 将每条记录写入图片
    for record in records:
        record_str = str(record)
        draw.text((x, y), record_str, fill='black', font=font)
        y += 40

    # 保存图片至指定路径
    image.save(filename)


def get_live_status_by_room_ids(room_ids):
    live_statuses = []
    titles = []
    unames = []
    changed_records = []  # 存储发生变化的记录元组的列表

    for id in room_ids:
        idURL = f"https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids={id}&req_biz=web_room_componet"
        response = requests.get(idURL)
        if response.status_code == 200:
            page = response.json()
            live_status = jsonpath.jsonpath(page["data"]["by_room_ids"][str(id)], "$..live_status")[0]
            title = jsonpath.jsonpath(page["data"]["by_room_ids"][str(id)], "$..title")[0]
            uname = jsonpath.jsonpath(page["data"]["by_room_ids"][str(id)], "$..uname")[0]
            live_statuses.append(live_status)
            titles.append(title)
            unames.append(uname)

            # 查询当前数据库中的数据
            current_data = get_data_from_database(id)

            if current_data is not None:
                current_live_status, current_title, current_uname = current_data
                if current_live_status != live_status or current_title != title or current_uname != uname:
                    # 出现了不同，将变化的记录添加到列表中
                    changed_records.append((live_status, title, uname))

        else:
            print(f"请求{idURL}失败")

    return live_statuses, titles, unames, changed_records


def get_data_from_database(room_id):
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()

    try:
        # 查询当前数据库中的数据
        cursor.execute("SELECT live_status, title, uname FROM bili_live_status WHERE room_id = %s", (room_id,))
        current_data = cursor.fetchone()

        return current_data

    except Exception as e:
        print("查询数据库失败:", e)
        return None

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def get_all_room_ids():
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()

    # 准备SQL查询语句，只查询room_id字段
    sql = "SELECT room_id FROM bili_live_status"

    try:
        # 执行查询
        cursor.execute(sql)

        # 获取查询结果
        results = cursor.fetchall()

        # 将room_id放入一个列表中
        room_ids = [result[0] for result in results]

        return room_ids
    except Exception as e:
        print("查询失败:", e)
    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def insert_data_into_database(uid, room_id, live_status, uname, title):
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()  # 将 cursor 的初始化移到 try 块的外部
    # 准备插入数据的SQL查询语句
    sql = "INSERT INTO bili_live_status (uid, room_id, live_status, uname, title) VALUES (%s, %s, %s, %s, %s)"

    try:
        # 执行带有数据的SQL查询
        cursor.execute(sql, (int(uid), int(room_id), live_status, uname, title))

        # 提交更改到数据库
        conn.commit()

        return "直播间监控数据插入成功！"
    except Exception as e:
        # 处理异常并抛出外层异常
        conn.rollback()
        raise Exception("直播间监控数据插入失败：" + str(e))
    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def get_live_status_equals_1():
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()

    # 准备SQL查询语句，添加title字段
    sql = "SELECT live_status, uname, title FROM bili_live_status"

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute(sql)

        # 获取查询结果
        results = cursor.fetchall()

        # 处理结果
        processed_results = []
        for row in results:
            live_status = row[0]
            uname = row[1]
            title = row[2]  # 获取新增的title字段数据

            # 根据live_status的值进行替换
            if live_status == 1:
                live_status = "直播中"
            elif live_status == 2:
                live_status = "轮播中"
            elif live_status == 0:
                live_status = "摸鱼中"

            processed_results.append((live_status, uname, title))  # 加入title数据

        return processed_results
    except Exception as e:
        print("查询失败:", e)
    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def update_database(room_ids, live_statuses, titles):
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()

    try:
        for i in range(len(room_ids)):
            room_id = room_ids[i]
            new_live_status = live_statuses[i]
            new_title = titles[i]

            # 将live_status字段从字符串转换为整数
            new_live_status = map_live_status_to_integer(new_live_status)

            # 查询当前数据库中的数据
            cursor.execute("SELECT live_status, title FROM bili_live_status WHERE room_id = %s", (room_id,))
            current_data = cursor.fetchone()

            if current_data is not None:
                current_live_status, current_title = current_data
                if current_live_status != new_live_status or current_title != new_title:
                    # 出现了不同，更新数据库中的数据和时间
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute(
                        "UPDATE bili_live_status SET live_status = %s, title = %s, time = %s WHERE room_id = %s",
                        (new_live_status, new_title, current_time, room_id))
                    conn.commit()

    except Exception as e:
        print("更新数据库失败:", e)
    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def map_live_status_to_string(live_status):
    status_map = {
        1: "直播中",
        2: "轮播中",
        0: "摸鱼中"
    }
    return status_map.get(live_status, "未知状态")


def map_live_status_to_integer(live_status):
    status_map = {
        "直播中": 1,
        "轮播中": 2,
        "摸鱼中": 0
    }
    return status_map.get(live_status, -1)  # 如果无法匹配，返回默认值 -1


@nonebot.scheduler.scheduled_job('cron', minute='*')
async def getMinutesData():
    bot = nonebot.get_bot()
    room_ids = get_all_room_ids()
    live_statuses, titles, unames, changed_records = get_live_status_by_room_ids(room_ids)
    live_statuses = [map_live_status_to_string(status) for status in live_statuses]
    if not changed_records:
        print("没有发生变化的记录")
        return
    update_database(room_ids, live_statuses, titles)
    save_records_as_image_with_auto_adaptation(changed_records, 'D:/statpic/records_image_high_resolution2.png',
                                               'D:/background/back.jpg')
    save_path = r"D:/statpic/records_image_high_resolution2.png"
    if not changed_records:
        return
    else:
        await bot.send_group_msg(group_id=699194084, message=f"[CQ:image,file=file:///{save_path}]")


# 绑定主播
@on_command('bind')
async def _(session):
    id = (await session.aget(prompt='请输入要绑定主播的直播间号(room_id) 可以通过查看直播间的url得到')).strip()
    idURL = f"https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids={id}&req_biz=web_room_componet"
    response = requests.get(url=idURL)
    page = json.loads(response.text)
    # 直播间状态 1直播中 2轮播 0摸了
    live_status = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..live_status")[0]
    # 直播者uid
    uid = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..uid")[0]
    # 直播者直播间id
    room_id = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..room_id")[0]
    # 直播者名称
    uname = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..uname")[0]
    # 直播间标题
    title = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..title")[0]
    await session.send(insert_data_into_database(int(uid), int(room_id), int(live_status), uname, title))


# 返回现在所有主播的状态
@on_command('监控')
async def _(session):
    records = get_live_status_equals_1()
    save_records_as_image_with_auto_adaptation(records, 'D:/statpic/records_image_high_resolution.png',
                                               'D:/background/back.jpg')
    save_path = r"D:/statpic/records_image_high_resolution.png"
    await session.send(f"[CQ:image,file=file:///{save_path}]", at_sender=True)