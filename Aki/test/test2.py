import json

import jsonpath
import requests

onlineURL = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=510C7A5DDD6C217F54D197E9501F055C&steamids=76561198156719464"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 QIHU 360SE'
}
response = requests.get(url=onlineURL, headers=headers)
page = json.loads(response.text)
onlineNum = jsonpath.jsonpath(page["response"], "$..players")
has_game_extrainfo = any('gameextrainfo' in d for d in onlineNum[0])
print(has_game_extrainfo)