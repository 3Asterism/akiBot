from aiocqhttp import MessageSegment
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('返回')
async def _(session):
    await session.send("[CQ:image,file=https://pixiv.re/110383914.jpg]")
