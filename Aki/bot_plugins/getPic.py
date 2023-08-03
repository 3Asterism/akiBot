import json
import requests
import jsonpath

from nonebot import on_command, MessageSegment


@on_command('33333')
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
        await session.send(MessageSegment.image(picURL))
