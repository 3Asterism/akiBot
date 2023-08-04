import json

import jsonpath
import requests

url = "https://api.bilibili.com/x/space/like/video?vmid=3493084176320605&w_rid=d3e9df4aa8a65c008155487f65c6a5b7&wts=1691137220"

# headers = {
#     "Cookie": "nostalgia_conf=-1; _uuid=448EA1B6-6A105-22ED-1096E-101A99CFF1F1D17567infoc; buvid3=8161C239-DC69-82D2-A844-8F9E1467F8EF18149infoc; b_nut=1690253718; buvid4=4BC71CE1-E1A6-18A9-E06D-F3FDF5DCCE7718149-023072510-qyaL1DibeR1xhFkpLJcqzg%3D%3D; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; DedeUserID=1899520; DedeUserID__ckMd5=c2f11c6afd09dc88; hit-new-style-dyn=1; hit-dyn-v2=1; CURRENT_FNVAL=4048; rpdid=|(u||uuJ|~)u0J'uYm|JJ)lkk; buvid_fp_plain=undefined; CURRENT_QUALITY=116; fingerprint=a24e83d3317fded368e208adde795166; SESSDATA=3d475411%2C1706582301%2C7fc5c%2A814N6-s6EnWBVKRSBAVgOZ9PkiKumXPzpe35jjT9awoAGiSjiIO4sb693LNp24LN5JlDMwFgAAFAA; bili_jct=42402c19436825620196c5fd24e204dc; LIVE_BUVID=AUTO6616910531911882; browser_resolution=1225-681; home_feed_column=4; sid=7v3uquli; bp_video_offset_1899520=825850188742524951; buvid_fp=a24e83d3317fded368e208adde795166; b_lsid=54AFF3E9_189BF834B96; PVID=2"
# }

json_obj = json.loads(requests.get(url).text)

# 提取 "pic"、"title"、"short_link_v2" 和 "pub_location" 值并存入列表
pic_list = jsonpath.jsonpath(json_obj, "$.data.list[*].pic")[0]
title_list = jsonpath.jsonpath(json_obj, "$.data.list[*].title")[0]
short_link_v2_list = jsonpath.jsonpath(json_obj, "$.data.list[*].short_link_v2")[0]
pub_location_list = jsonpath.jsonpath(json_obj, "$.data.list[*].pub_location")[0]
name_list = jsonpath.jsonpath(json_obj, "$.data.list[*].owner.name")[0]
id = "474248209"
vmidURL = f"https://api.bilibili.com/x/space/like/video?vmid={id}&w_rid=d3e9df4aa8a65c008155487f65c6a5b7&wts=1691137220"
jsonResponse = json.loads(requests.get(vmidURL).text)["code"]

# 打印列表
print("图片链接列表:", pic_list)
print("视频标题列表:", title_list)
print("短链接列表:", short_link_v2_list)
print("发布地点列表:", pub_location_list)
print("用户姓名:", name_list)
print(jsonResponse == 53013)




