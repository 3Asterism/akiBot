import json
import random
import re
import jsonpath
import requests
from nonebot import on_command


def extract_number_from_url(url):
    # 使用正则表达式匹配URL中的数字部分
    match = re.search(r'/(\d+)_p0_', url)
    if match:
        number = match.group(1)
        return number
    return None


@on_command('1')
async def _(session):
    tag = "足"
    keywords = ['男', 'R-18']
    url = "https://www.pixiv.net/ajax/search/artworks/%E8%B6%B3?word={" \
          "0}&order=date_d&mode=all&p=1&s_mode=s_tag&type=all" \
          "&lang=zh&version=19921c54619a740796d32683244aad17e288a534".format(tag)
    response = requests.get(url=url)
    page = json.loads(response.text)
    # 拿到json文件最内层 data层
    resultData = page["body"]["illustManga"]["data"]
    # 拿到该tag对应的50个data tags
    tagList = jsonpath.jsonpath(resultData, '$..tags')
    # 拿到该tag对应的50个data url
    urlList = jsonpath.jsonpath(resultData, '$..url')
    # 输出所有带keywords的下标
    indices_with_man = [index for index, sublist in enumerate(tagList) if
                        any(keyword in item for keyword in keywords for item in sublist)]
    # 筛选掉所有带keywords的
    filtered_single_list = [elem for index, elem in enumerate(urlList) if index not in indices_with_man]
    # 拿到该画的id
    # 对filtered_url_list中的每个元素进行替换并提取数字，然后拼接新的URL
    new_url_list = ['https://pixiv.re/' + extract_number_from_url(url) + '.jpg' for url in filtered_single_list]
    randomPic = new_url_list[random.randint(0, 49)]
    print(urlList)
    print(tagList)
    print(indices_with_man)
    print(filtered_single_list)
    print(new_url_list)
    print(randomPic)
    print("[CQ:image,file={0}]".format(str(randomPic)))
    await session.send("[CQ:image,file={0}]".format(str(randomPic)))
