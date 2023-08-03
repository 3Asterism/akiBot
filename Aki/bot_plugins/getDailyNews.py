import nonebot
from nonebot import on_command
import requests

def save_image_from_url(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"图片保存成功：{save_path}")
    except requests.exceptions.RequestException as e:
        print(f"图片保存失败：{e}")


@nonebot.scheduler.scheduled_job('cron', hour='12')
async def getDailyNews():
    bot = nonebot.get_bot()
    await bot.send_group_msg(group_id=699194084, message="[CQ:image,file=https://api.03c3.cn/zb/]")


@on_command('今日新闻')
async def _(session):
    # 要获取的图片URL
    image_url = 'https://api.03c3.cn/zb/'

    # 保存图片的本地路径（注意使用原始字符串表示路径）
    save_path = r'C:\news\image.jpg'

    # 发送GET请求并保存图片
    save_image_from_url(image_url, save_path)

    await session.send(f"[CQ:image,file=file:///{save_path}]", at_sender=True)
