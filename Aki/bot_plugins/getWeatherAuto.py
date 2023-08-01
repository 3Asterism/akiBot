import json

import jsonpath
import nonebot
import requests

__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@nonebot.scheduler.scheduled_job('cron', hour='9')
async def _():
    location = "江岸"
    url = "https://geoapi.qweather.com/v2/city/lookup?location={0}&key=78c8f2bd60494a3981e5a2cd5217db20".format(
        location)
    response = requests.get(url=url)
    page = json.loads(response.text)
    resultData = page["location"]
    cityID = jsonpath.jsonpath(resultData, '$..id')
    weatherURL = "https://devapi.qweather.com/v7/weather/now?location={0}&key=78c8f2bd60494a3981e5a2cd5217db20".format(
        cityID[0])
    response = requests.get(url=weatherURL)
    page = json.loads(response.text)
    resultData = page["now"]
    # 获得温度
    temp = jsonpath.jsonpath(page, '$..temp')[0]
    # 获得体感温度
    bodyTemp = jsonpath.jsonpath(page, '$..feelsLike')[0]
    # 获得当前天气
    weather = jsonpath.jsonpath(page, '$..text')[0]
    # 获得当前风速
    windSpeed = jsonpath.jsonpath(page, '$..windScale')[0]
    # 获得当前湿度
    humidity = jsonpath.jsonpath(page, '$..humidity')[0]
    await session.send("今天"+location+"的天气是:\n"+"实际温度为:"+temp+"\n"+"体感温度为:"+bodyTemp+"\n"+"天气为:"+weather+"\n"+"当前风速为:"+windSpeed+"级"+"\n"+"当前湿度为:"+humidity+"%"+"\n")
