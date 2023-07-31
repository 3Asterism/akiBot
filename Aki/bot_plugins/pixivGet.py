import json
import random
import re
import jsonpath
import requests
from nonebot import on_command


def extract_number_from_url(url):
    # 使用正则表达式匹配URL中的数字部分
    match = re.search(r'/(\d+)_p\d_', url)
    if match:
        number = match.group(1)
        return number
    return None


@on_command('2')
async def _(session):
    # pixiv的tags是以空格分割的
    tag = session.current_arg_text.strip()
    if not tag:
        tag = (await session.aget(prompt='请输入tag 多tag以空格分隔符号分割')).strip()
    url = "https://www.pixiv.net/ajax/search/artworks/{0}?order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh".format(tag)
    print(url)
    keywords = ['男']
    response = requests.get(url=url, verify=False)
    response.raise_for_status()
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
    print(urlList)
    print(tagList)
    print(indices_with_man)
    print(filtered_single_list)
    # 拿到该画的id
    # 对filtered_url_list中的每个元素进行替换并提取数字，然后拼接新的URL
    new_url_list = ['https://pixiv.nl/' + extract_number_from_url(url) + '.jpg' for url in filtered_single_list if extract_number_from_url(url)]
    randomPic = random.choice(new_url_list)
    print(new_url_list)
    print(randomPic)
    print("[CQ:image,file={0}]".format(str(randomPic)))
    await session.send("[CQ:image,file={0}]".format(str(randomPic)))
