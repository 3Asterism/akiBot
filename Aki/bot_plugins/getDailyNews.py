import nonebot
from nonebot import on_command


@nonebot.scheduler.scheduled_job('cron', hour='12')
async def getDailyNews():
    bot = nonebot.get_bot()
    await bot.send_group_msg(group_id=699194084, message="[CQ:image,file=https://api.03c3.cn/zb/]")


@on_command('今日新闻')
async def _(session):
    await session.send("[CQ:image,file=https://api.03c3.cn/zb/]", at_sender=True)
