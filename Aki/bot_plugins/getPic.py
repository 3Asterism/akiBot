import json
import os

import requests
import jsonpath

from nonebot import on_command, MessageSegment


def save_image_from_url(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"图片保存成功：{save_path}")
    except requests.exceptions.RequestException as e:
        print(f"图片保存失败：{e}")


@on_command('getpic')
async def getPic(session):
    originalURL = "https://api.lolicon.app/setu/v2"
    # 取得消息的内容，并且去掉首尾的空白符
    tag = session.current_arg_text.strip()
    if not tag:
        tag = (await session.aget(prompt='请输入tag 多tag以|分隔符号分割')).strip()
        tagURL = "https://api.lolicon.app/setu/v2?tag={0}&size=regular".format(tag)
        response = requests.get(url=tagURL)
        page = json.loads(response.text)
        picURL = jsonpath.jsonpath(page["data"], "$..regular")[0]
        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(current_dir, '..', '..', 'pic', 'getpic', 'image.jpg')
        save_image_from_url(picURL, save_path)
        await session.send(f"[CQ:image,file=file:///{save_path}]", at_sender=True)
