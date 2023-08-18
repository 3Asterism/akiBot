import nonebot
from aiocqhttp import Event

# 创建一个事件响应器，用于监听群消息
bot = nonebot.get_bot()


@bot.on_message()
async def handle_group_message(event: Event):
    print(event.message)
    print(event.group_id)
    print(event.message_id)

    # self_id: int  # 机器人自身 ID
    # user_id: Optional[int]  # 用户 ID
    # operator_id: Optional[int]  # 操作者 ID
    # group_id: Optional[int]  # 群 ID
    # discuss_id: Optional[int]  # 讨论组 ID，此字段已在 OneBot v11 中移除
    # message_id: Optional[int]  # 消息 ID
    # message: Optional[Any]  # 消息
    # raw_message: Optional[str]  # 未经 OneBot (CQHTTP) 处理的原始消息
    # sender: Optional[Dict[str, Any]]  # 消息发送者信息
    # anonymous: Optional[Dict[str, Any]]  # 匿名信息
    # file: Optional[Dict[str, Any]]  # 文件信息
    # comment: Optional[str]  # 请求验证消息
    # flag: Optional[str]  # 请求标识
