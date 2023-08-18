import json
import random
import jsonpath
import requests
import os

from nonebot import on_command
@on_command('星巴克')

async def star(session):
    category = (await session.aget(prompt='要推荐饮料还是食物')).strip()
    url = "https://www.starbucks.com.cn/assets/search/menu-source-zh.json"
    response = requests.get(url)
    page = json.loads(response.text)
    if category == "饮料":
        filtered = {key: value for key, value in page.items() if "beverage" in key.lower()}

        title = jsonpath.jsonpath(filtered, '$..title')
        body = jsonpath.jsonpath(filtered, '$..body')
        preview = jsonpath.jsonpath(filtered, '$..preview')
        popular = jsonpath.jsonpath(filtered, '$..popular')
        for index, value in enumerate(popular):
            if value == "":
                popular[index] = "false"
        random_title = random.choice(title)
        index = title.index(random_title)

        image_url = "https://www.starbucks.com.cn" + preview[index]
        save_path = os.path.join(os.getcwd(), "image.jpg")

        response = requests.get(image_url)
        with open(save_path, "wb") as f:
            f.write(response.content)

        await session.send("推荐的饮料" + random_title + "\n" + "描述:" + body[index] + "\n" + "预览图:" + f"[CQ:image,file=file:///{save_path}]" + "\n" + "是否畅销:" + popular[index], at_sender=True)

    elif category == "食物":
        filtered = {key: value for key, value in page.items() if "food" in key.lower()}

        title = jsonpath.jsonpath(filtered, '$..title')
        body = jsonpath.jsonpath(filtered, '$..body')
        preview = jsonpath.jsonpath(filtered, '$..preview')
        popular = jsonpath.jsonpath(filtered, '$..popular')
        for index, value in enumerate(popular):
            if value == "":
                popular[index] = "false"
        random_title = random.choice(title)
        index = title.index(random_title)

        image_url = "https://www.starbucks.com.cn" + preview[index]
        save_path = os.path.join(os.getcwd(), "image.jpg")

        response = requests.get(image_url)
        with open(save_path, "wb") as f:
            f.write(response.content)

        await session.send("推荐的饮料" + random_title + "\n" + "描述:" + body[index] + "\n" + "预览图:" + f"[CQ:image,file=file:///{save_path}]" + "\n" + "是否畅销:" + popular[index], at_sender=True)

    else:
        await session.send("错误的输入")









