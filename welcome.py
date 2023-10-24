# 开发时间：2023/10/24  22:58
# The road is nothing，the end is all    --Demon

from libs.event.qqevent import onkeyword,onGroupIncrease
import asyncio


@onGroupIncrease()
async def handle(n):
    id = n.netpackage.group_id
    u_id = n.netpackage.user_id
    print(type(id))
    speak_welcome = f'[CQ:at,qq={u_id}]' + '欢迎加入！'
    await asyncio.sleep(2)
    rp = await n.callAPI(url="send_group_msg", group_id=id, message=speak_welcome)

