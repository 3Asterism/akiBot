import datetime
import json

import jsonpath
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
}
steamIds = ["76561199255316734", "76561198156719464", "76561198446777688", "76561198445434327", "76561198849006226",
            "76561199046764332", "76561198357775138", "76561198973120451", "76561198146244935", "76561198274823489",
            "76561199001084508", "76561198866693285", "76561198284249633", "76561198846544228"]
friendsStateURL = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=510C7A5DDD6C217F54D197E9501F055C&steamids={0}".format(
    ",".join(steamIds))
print(friendsStateURL)
response = requests.get(url=friendsStateURL, headers=headers)
page1 = json.loads(response.text)
# 生成该用户的字典
data_json = jsonpath.jsonpath(page1["response"], "$..players")

# 初始化空列表来存储提取的值
# 个人名称
personanames = []
# 在线状态 0离线 1在线 3在打游戏 4离开
personastates = []
# 上次下机的时间
lastlogoffs = []
# 现在在打的游戏
gameextrainfos = []

# 遍历数据中的每个内部列表
for inner_list in data_json:
    for entry in inner_list:
        # 从字典中提取值并添加到相应的列表中
        personanames.append(entry.get('personaname', ''))
        personastates.append(entry.get('personastate', 0))
        lastlogoffs.append(datetime.datetime.fromtimestamp(entry.get('lastlogoff', 0)))
        gameextrainfos.append(entry.get('gameextrainfo', ''))

# 找出gameextrainfos列表中不为空字符串的下标
non_empty_indices = [i for i, gameinfo in enumerate(gameextrainfos) if gameinfo != '']

# 根据找到的下标提取其他三个列表的元素
selected_personanames = [personanames[i] for i in non_empty_indices]
selected_personastates = [personastates[i] for i in non_empty_indices]
selected_lastlogoffs = [lastlogoffs[i] for i in non_empty_indices]
selected_gameextrainfos = [gameextrainfos[i] for i in non_empty_indices]

# 假设你有四个列表：selected_personanames、selected_personastates、selected_lastlogoffs和selected_gameextrainfos

# 将列表转换成字典
data_dict = {
    '姓名': selected_personanames,
    '状态': selected_personastates,
    '最后登录': selected_lastlogoffs,
    '游戏名称': selected_gameextrainfos,
}

# 创建一个Pandas DataFrame
df = pd.DataFrame(data_dict)

# 设置保存图片时的字体样式（使用支持中文字符的字体SimHei.ttf）
font = ImageFont.truetype('C:\Windows\Fonts\msyhbd.ttc', 18)

# 设置图片大小和行高（调整分辨率）
image_width = 1200  # Increase the width of the image
image_height = len(df) * 50  # Increase the height of the image

# 创建空白图片
image = Image.new('RGB', (image_width, image_height), color='white')
draw = ImageDraw.Draw(image)

# 循环遍历DataFrame，并将数据写入图片
for i, row in df.iterrows():
    y = i * 50  # Increase the line height to 50
    for j, column in enumerate(df.columns):
        x = j * 300  # Increase the column width to 300 for extra spacing
        # Convert the data to string using str() to handle non-ASCII characters
        draw.text((x, y), f"{column}: {str(row[column])}", fill='black', font=font)

# 保存图片到本地，并指定'utf-8' encoding
save_path = r"D:\statpic\selected_data.png"
image.save(save_path, 'png', encoding='utf-8')

# 显示图片（可选）
image.show()