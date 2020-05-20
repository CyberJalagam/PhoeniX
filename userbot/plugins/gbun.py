# This is a troll indeed ffs *facepalm*
import asyncio
from telethon import events
from platform import uname
from userbot import ALIVE_NAME
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.**"

@borg.on(admin_cmd("gbun"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Boss {DEFAULTUSER}\n`"
    no_reason = "__Reason: Heavy SPAM + OT. __"
    await event.edit("**Gathering Information... ⚜️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1109396517:
            await reply_message.reply("`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 50$ to my master__ [Mp $inGH✪](https://t.me/TechyNewbie) __to release your account__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  f"` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Boss {DEFAULTUSER}\n\n`"
                  "**Name of the IDIOT: ** {}\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Spammer's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Spammer's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = f"`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Boss {DEFAULTUSER}\nReason: Heavy SPAM + OT. `"
        await event.reply(mention)
    await event.delete()
