import json

import jsonpath
import requests

# 取得消息的内容，并且去掉首尾的空白符
id = 22259479
idURL = f"https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids={id}&req_biz=web_room_componet"
response = requests.get(url=idURL)
page = json.loads(response.text)
picURL = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..live_status")[0]
uid = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..uid")[0]
room_id = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..room_id")[0]
uname = jsonpath.jsonpath(page["data"]["by_room_ids"][f"{id}"], "$..uname")[0]
print("现在直播间的状态是" + str(picURL))
print(uid)
print(room_id)
print(uname)
