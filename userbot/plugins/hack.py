"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from sql.global_variables_sql import SYNTAX, MODULE_LIST
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
import asyncio

from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.**"


@borg.on(events.NewMessage(pattern=r"(.gmailhack)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "gmailhack":
        
        await event.edit(input_str)
        
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1109396517:
            await reply_message.reply(f"`Wait a second, {DEFAULTUSER} is My Boss!`\n**How dare you even think to hack my boss' google account stupid!**\n\n__Your account will be hacked in a few minutes! Pay 50$ to my Boss__ [Mp $inGH✪](https://t.me/TechyNewbie) __OR delete your telegram account to prevent the virus getting into your Gmail account __😏")
        else:
            animation_chars = [
        
            "`Connecting To Dark WEB Secret Server...`",
            "`Connection Successful!`",
            "`Targetting` [{}](tg://user?id={})'s `Google Account.`".format(firstname, idd),
            "`Attempting method I... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method I FAILED!`",
            "`Attempting method II... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method II Out Of Order!`",
            "`Attempting method III... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Disabling Account Security... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting Password... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Pulling Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Hacking... 74%\n███████████████████▒▒▒▒▒▒ `",
            "`Hacking.... 80%\n█████████████████████▒▒▒▒ `",
            "`Adding Modules... 86%\n██████████████████████▒▒▒ `",
            "`Adding Finishing Touches... 98%\n████████████████████████▒`",
            "`HACKED 100%\n█████████████████████████ `",
            f"{DEFAULTUSER} `Has Hacked` [{firstname}](tg://user?id={idd})'s `Google Account Successfully...`\n[{firstname}](tg://user?id={idd})'s __account is under Boss' control now__\n\n**Pay 50$ To** @TechyNewbie **Or Get Ready To Lose all your YouTube Subscribers and See Your Mail Full Of Spams.**"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 21)
   
    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)
        
        animation_chars = [
        
            "`Connecting To DarkWEB Secret Server...`",
            "`Connection Successful!`",
            "`Targetting your Telegram Account`",
            "`Target Selected.`",
            "`Attempting method 1... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method 1 FAILED!`",
            "`Attempting method 2... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Removing Encryption... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting API ID and API Hash.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting API ID and API Hash... 17%\n████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploding Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking. 29%\n███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking.. 35%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 43%\n███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`modifying INFORMATION... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`MODIFYING information... 58%\n███████████████▒▒▒▒▒▒▒▒▒▒ `",
            "`modifying INFORMATION... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Adding Modules... 84%\n█████████████████████▒▒▒▒ `",
            "`Adding Finishing Touches... 98%\n████████████████████████▒`",
            "`HACKED... 100%\n█████████████████████████ `",
            "`Your Telegram Account Hacked Successfully...`\n__Your userbot will now start spamming everywhere...__\n\n**Pay 25$ To** @TechyNewbie **Or delete and re-deploy your userbot to remove this hack.**"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 21])
            
            
            
MODULE_LIST.append("hack")      

SYNTAX.update({
    "hack": "\
**Special Prank module for Hacking**\
\n\n• ```.hack``` (as a reply to message)\
\nUsage: __Hacks the Telegram account of the targeted user.__\
\n\n• ```.gmailhack``` (as a reply to message)\
\nUsage: __Hacks the Google account of the targeted user.__\
"
})
