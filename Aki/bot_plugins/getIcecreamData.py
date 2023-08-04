import json
import os

import jsonpath
import nonebot
import requests
from nonebot import on_command


def extract_data():
    url = "https://api.bilibili.com/x/space/like/video?vmid=3493084176320605&w_rid=d3e9df4aa8a65c008155487f65c6a5b7&wts=1691137220"

    json_obj = json.loads(requests.get(url).text)

    # 提取最新的 "pic"、"title"、"short_link_v2"、"name" 和 "pub_location" 值
    pic_list = jsonpath.jsonpath(json_obj, "$.data.list[*].pic")[0]
    title_list = jsonpath.jsonpath(json_obj, "$.data.list[*].title")[0]
    short_link_v2_list = jsonpath.jsonpath(json_obj, "$.data.list[*].short_link_v2")[0]
    pub_location_list = jsonpath.jsonpath(json_obj, "$.data.list[*].pub_location")[0]
    name_list = jsonpath.jsonpath(json_obj, "$.data.list[*].owner.name")[0]

    # 返回五个值
    return pic_list, title_list, short_link_v2_list, pub_location_list, name_list


def save_data_from_url(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"图片保存成功：{save_path}")
    except requests.exceptions.RequestException as e:
        print(f"图片保存失败：{e}")


@on_command('随机雪糕')
async def randomIcecream(session):
    pic, title, short_link_v2, pub_location, name = extract_data()
    # 要获取的图片URL
    image_url = pic

    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(current_dir, '..', '..', 'pic', 'icecream', 'icecream.jpg')

    # 发送GET请求并保存图片
    save_data_from_url(image_url, save_path)

    await session.send(f"[CQ:image,file=file:///{save_path}]"+"标题:" + title + "\n" + "链接:" + short_link_v2 + "\n" + "发布自:" + pub_location + "\n" + "up主:" + name, at_sender=True)
