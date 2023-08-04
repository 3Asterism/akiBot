import json
import os
import random

import jsonpath
import mysql
import requests
from nonebot import on_command

import mysql.connector


def get_uid_data_from_db():
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
        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 执行 SQL 查询语句，获取数据
        sql = "SELECT `pic`, `title`, `bvid`, `author` FROM `bili_uid_icecreamer_firstvideo`"
        cursor.execute(sql)

        # 获取所有数据行
        result = cursor.fetchall()

        # 将数据拆分为四个列表
        pic_list = []
        title_list = []
        bvid_list = []
        author_list = []

        for row in result:
            pic_list.append(row[0])
            title_list.append(row[1])
            bvid_list.append(row[2])
            author_list.append(row[3])

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

    return pic_list, title_list, bvid_list, author_list


def get_vmdata_from_db():
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
        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 执行 SQL 查询语句，获取数据
        sql = "SELECT `pic`, `title`, `short_link_v2`, `pub_location`, `name` FROM `bili_icecreamer_firstvideo`"
        cursor.execute(sql)

        # 获取所有数据行
        result = cursor.fetchall()

        # 将数据拆分为五个列表
        pic_list = []
        title_list = []
        short_link_v2_list = []
        pub_location_list = []
        name_list = []

        for row in result:
            pic_list.append(row[0])
            title_list.append(row[1])
            short_link_v2_list.append(row[2])
            pub_location_list.append(row[3])
            name_list.append(row[4])

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

    return pic_list, title_list, short_link_v2_list, pub_location_list, name_list


def insert_data_to_db(vmid):
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
        # 提取数据
        pic, title, short_link_v2, pub_location, name, vmid = extract_data_vmid(vmid)

        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 编写 SQL 插入语句
        sql = "INSERT INTO `bili_icecreamer_firstvideo` (`vmid`, `pic`, `title`, `short_link_v2`, `pub_location`, `name`) VALUES (%s, %s, %s, %s, %s, %s)"

        # 执行 SQL 插入语句
        cursor.execute(sql, (vmid, pic, title, short_link_v2, pub_location, name))

        # 提交更改到数据库
        conn.commit()

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


def insert_uid_data_to_db(uid):
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
        # 提取数据
        pic, title, bvid, author, mid = extract_data_uid(uid)

        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 编写 SQL 插入语句
        sql = "INSERT INTO `bili_uid_icecreamer_firstvideo` (`mid`, `pic`, `title`, `bvid`, `author`) VALUES (%s, %s, %s, %s, %s)"

        # 执行 SQL 插入语句
        cursor.execute(sql, (mid, pic, title, bvid, author))

        # 提交更改到数据库
        conn.commit()

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()


# 特殊长id
def extract_data_vmid(vmid):
    url = f"https://api.bilibili.com/x/space/like/video?vmid={vmid}&w_rid=d3e9df4aa8a65c008155487f65c6a5b7&wts=1691137220"

    json_obj = json.loads(requests.get(url).text)

    # 提取最新的 "pic"、"title"、"short_link_v2"、"name" 和 "pub_location" 值
    pic = jsonpath.jsonpath(json_obj, "$.data.list[*].pic")[0]
    title = jsonpath.jsonpath(json_obj, "$.data.list[*].title")[0]
    short_link_v2 = jsonpath.jsonpath(json_obj, "$.data.list[*].short_link_v2")[0]
    pub_location = jsonpath.jsonpath(json_obj, "$.data.list[*].pub_location")[0]
    name = jsonpath.jsonpath(json_obj, "$.data.list[*].owner.name")[0]
    vmid = jsonpath.jsonpath(json_obj, "$.data.list[*].owner.mid")[0]

    # 返回五个值
    return pic, title, short_link_v2, pub_location, name, vmid


# 普通uid
def extract_data_uid(uid):
    url = f"https://api.bilibili.com/x/space/wbi/arc/search?pn=1&ps=1&mid={uid}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                      'Safari/537.36 QIHU 360SE'
    }

    json_obj = json.loads(requests.get(url, headers=headers).text)

    # 使用 JSONPath 表达式提取字段
    pic = jsonpath.jsonpath(json_obj, "$.data.list.vlist[*].pic")[0]
    title = jsonpath.jsonpath(json_obj, "$.data.list.vlist[*].title")[0]
    # 这玩意儿是视频链接
    bvid = jsonpath.jsonpath(json_obj, "$.data.list.vlist[*].bvid")[0]
    author = jsonpath.jsonpath(json_obj, "$.data.list.vlist[*].author")[0]
    # uid
    mid = jsonpath.jsonpath(json_obj, "$.data.list.vlist[*].mid")[0]

    # 返回五个值
    return pic, title, bvid, author, mid


def save_data_from_url(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"图片保存成功：{save_path}")
    except requests.exceptions.RequestException as e:
        print(f"图片保存失败：{e}")


@on_command('绑定雪糕')
async def bindIcecream(session):
    id = int((await session.aget(prompt='请输入要绑定主播的id(uid/vmid) 如果是非常长一串大概率是vmid')).strip())
    vmidURL = f"https://api.bilibili.com/x/space/like/video?vmid={id}&w_rid=d3e9df4aa8a65c008155487f65c6a5b7&wts=1691137220"
    jsonResponse = json.loads(requests.get(vmidURL).text)["code"]
    # 输入的是vmid
    if jsonResponse == 0:
        insert_data_to_db(id)
    # 输入的是uid
    else:
        insert_uid_data_to_db(id)

    await session.send("绑定成功")


@on_command('随机雪糕')
async def randomIcecream(session):
    # 生成一个包含两个函数的列表
    functions = [get_uid_data_from_db, get_vmdata_from_db]

    # 抽取权重 调高uid的权重 因为使用uid的up主较多
    weights = [5, 1]

    # 随机选择一个函数
    random_func = random.choices(functions, weights=weights)

    # 调用随机选择的函数并获取数据
    data = random_func()

    # 抽到vmid的情况
    if len(data) == 5:
        pic, title, short_link_v2, pub_location, name = data[0][0], data[1][0], data[2][0], data[3][0], data[4][0]
        # 要获取的图片URL
        image_url = pic

        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(current_dir, '..', '..', 'pic', 'icecream', 'icecream.jpg')

        # 发送GET请求并保存图片
        save_data_from_url(image_url, save_path)

        await session.send(
            f"[CQ:image,file=file:///{save_path}]" + "标题:" + title + "\n" + "链接:" + short_link_v2 + "\n" + "发布自:" + pub_location + "\n" + "up主:" + name,
            at_sender=True)
    # 抽取到uid的情况
    else:
        pass
