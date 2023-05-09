from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('简介', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('这是AkiBot!目前有查成分 涩图功能')
