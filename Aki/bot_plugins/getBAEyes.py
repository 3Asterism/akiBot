import os

from nonebot import on_command


@on_command('千里眼')
async def getPic(session):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(current_dir, '..', '..', 'pic', 'eyes', 'eye.png')
    await session.send(f"[CQ:image,file=file:///{save_path}]", at_sender=True)
