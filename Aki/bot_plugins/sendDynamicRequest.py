import json
import requests
import jsonpath

from nonebot import on_command


def circulateForAllDynamic(uid):
    originalURL = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset=&host_mid={0}&timezone_offset=-480&features=itemOpusStyle".format(
        uid)
    response = requests.get(url=originalURL)
    page = json.loads(response.text)
    # 拿到第一页的数据
    resultList = jsonpath.jsonpath(page["data"]["items"], '$..orig_text')
    flag0 = jsonpath.jsonpath(page["data"], '$..has_more')[0]
    # 如果有更多内容 进行循环
    if flag0 is True:
        while True:
            OldOffsetList = jsonpath.jsonpath(page["data"], '$..offset')
            fullDynamicURL = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset={0}&host_mid={1}&timezone_offset=-480&features=itemOpusStyle".format(
                OldOffsetList[0], uid)
            response = requests.get(url=fullDynamicURL)
            page = json.loads(response.text)
            resultData = page["data"]["items"]
            commentList = jsonpath.jsonpath(resultData, '$..orig_text')
            flag = jsonpath.jsonpath(page["data"], '$..has_more')[0]
            for dynamic in commentList:
                resultList.append(dynamic)
            # 循环结束的标志为 has_more字段为False
            if flag is True:
                continue
            else:
                break

    return resultList


def circulateForFollow(uid):
    originalURL = "https://api.bilibili.com/x/relation/followings?vmid={0}&pn=1&ps=50&order=desc".format(
        uid)
    response = requests.get(url=originalURL)
    page = json.loads(response.text)
    # 检查是否设置了隐私
    if jsonpath.jsonpath(page, '$..message')[0] != '0':
        return "该用户设置了隐私！"
    # 拿到第一页的up主名字数据
    resultList = jsonpath.jsonpath(page["data"]["list"], '$..uname')
    flag = int(jsonpath.jsonpath(page["data"], '$..total')[0] / 50)
    # 如果有更多内容 进行循环
    if flag - 1 >= 0:
        for i in range(flag - 1):
            if i + 2 > 5:
                break
            newFlag = i + 2
            newURL = "https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=50&order=desc".format(
                uid, newFlag)
            response = requests.get(url=newURL)
            page = json.loads(response.text)
            uList = jsonpath.jsonpath(page["data"]["list"], '$..uname')
            for uname in uList:
                resultList.append(uname)

    return resultList


def getAnimeRequest(uid):
    url = "https://api.bilibili.com/x/space/bangumi/follow/list?type=1&follow_status=0&pn=1&ps=30&vmid={0}&ts=1683275503129".format(
        uid)
    response = requests.get(url=url)
    page = json.loads(response.text)
    resultData = page["data"]["list"]
    # 拿到第一页的追番
    length = int(jsonpath.jsonpath(page["data"], '$..total')[0])
    resultList = jsonpath.jsonpath(resultData, '$..title')
    flag = int(length / 30)
    # 如果有更多内容 进行循环
    if flag - 1 >= 0:
        for i in range(flag - 1):
            if i + 2 > 5:
                break
            newFlag = i + 2
            newURL = "https://api.bilibili.com/x/space/bangumi/follow/list?type=1&follow_status=0&pn={0}&ps=30&vmid={1}&ts=1683275503129".format(
                newFlag, uid)
            response = requests.get(url=newURL)
            page = json.loads(response.text)
            uList = jsonpath.jsonpath(page["data"]["list"], '$..title')
            for title in uList:
                resultList.append(title)

    return resultList, length


def sendRequest(uid):
    return circulateForAllDynamic(uid)


def removeBadData(List):
    newList = []
    result = []
    badData = ["OP&ED", "预告·花絮", "次元发电机专访", "花絮", "精彩看点", "总集篇", "其他", "全片", "主题曲",
               "经典回顾", "猜你喜欢", "高能速看", "预告", "UP主带你一起吃瓜", "特别篇", "精选二创", "研发记录"]
    for i in range(len(List)):
        for j in range(len(badData)):
            if badData[j] in List[i]:
                break
            if j == len(badData) - 1:
                newList.append(List[i])

    for ele in newList:
        if "0" not in ele and "1" not in ele and "2" not in ele and "3" not in ele and "4" not in ele and "5" not in ele and "6" not in ele and "7" not in ele and "8" not in ele and "9" not in ele and "PV" not in ele:
            result.append(ele)
        else:
            continue
    return result


def sendFollowRequest(uid):
    # 返回b站关注数据
    return circulateForFollow(uid)


def sendAnimeRequest(uid):
    # 返回b站关注数据
    result, length = getAnimeRequest(uid)
    # 去除脏数据 暂时没想到更好的解决方法
    result = list(dict.fromkeys(result))
    result2 = removeBadData(result)
    return result2


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('查成分')
async def weather(session):
    # 取得消息的内容，并且去掉首尾的空白符
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='uid')).strip()
        command = (await session.aget(prompt='可查动态，关注，追番列表，未返回则设置了隐藏')).strip()
        if command == "动态":
            await session.send(",".join(sendRequest(city)))
        elif command == "关注":
            await session.send(",".join(sendFollowRequest(city)))
        elif command == "追番":
            await session.send(",".join(sendAnimeRequest(city)))
        else:
            await session.send("ERROR!")
        while not city:
            city = (await session.aget(prompt='uid不能为空，请重新输入')).strip()
