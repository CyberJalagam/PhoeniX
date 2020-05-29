"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from sql.global_variables_sql import SYNTAX, MODULE_LIST

BOSS = str(ALIVE_NAME) if ALIVE_NAME else "**THIS CRIMINAL**"



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 22)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Making a private call to DarkWEB.`",
            "`Making a private call to DarkWEB..`",
            "`Making a private call to DarkWEB...`",
            "**Terminated by PhoeniX security**!!\nThis is @HawkEyesMohak. You were connecting to DarkWEB, eh?",
            "IT IS FORBIDDEN",
            "`Redirecting Call To Telegram Headquarters`",
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "Telegram HQ: `Hello This is Telegram HQ. Who is this?`",
            "Telegram HQ: `Hello This is Telegram HQ. Who is this?`\n\nmpSinGH: `Yo this is` @HawkEyesMohak",
            "Telegram HQ: `Oh Hello Peru Sir!! I Know You Are The Creator Of The Awesome PhoeniX Userbot. How May I Help You?`",
            f"Telegram HQ: `Oh Hello Peru Sir!! I Know You Are The Creator Of The Awesome PhoeniX Userbot. How May I Help You?`\n\nmpSinGH: `Hello Sir, Please Ban` {BOSS}'s `Telegram Account.`",    
            "Telegram HQ: `May I Know What Did He Do?`",
            "Telegram HQ: `May I Know What Did He Do?`\n\nmpSinGH: `He tried to use the forbidden .call command and tried connecting to DarkWEB`",
            "Telegram HQ: `OMG!!! I'll Make Sure That Guy Account Will Get Banned From Telegram Within 24Hrs.`",
            "Telegram HQ: `OMG!!! I'll Make Sure That Guy Account Will Get Banned From Telegram Within 24Hrs.`\n\nmpSinGH: `Thanks, See You Later Brah.`",
            "Telegram HQ: `Please Don't Thank Sir. It's Our Duty To Ban These Guys. Thanks For Reporting Him`",
            "Telegram HQ: `Please Don't Thank Sir. It's Our Duty To Ban These Guys. Thanks For Reporting Him`\n\nmpSinGH: `Okay! See you later`",
            "Telegram HQ: `Sure Sur. TC Bye Bye :)`",
            "`Private Call Disconnected.`",
            f"{BOSS}'s **account will get banned in 24 Hours**",
            f"{BOSS}'s **account will get banned in 24 Hours**\n\n__Contact__ @HawkEyesMohak __to free up your account.__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 22])

MODULE_LIST.append("call")
SYNTAX.update({
    "call": "\
**Requested Module --> Private Call**\
\n\n• `.call`\
\nUsage: __Places a Private Call to the forbidden DarkWEB__\
"
})
            
