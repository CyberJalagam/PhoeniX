"""Emoji

Available Commands:

.police"""


from sql.global_variables_sql import SYNTAX, MODULE_LIST

from telethon import events

import asyncio

from telethon.tl.functions.users import GetFullUserRequest



@borg.on(events.NewMessage(pattern=r"(.police)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.6

    animation_ttl = range(0, 37)

    input_str = event.pattern_match.group(1)

    if input_str == "police":
        
        await event.edit(input_str)
        
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1109396517:
            await reply_message.reply("~~Calling Police~~ `Wait a second, This is my boss!`\n**How dare you report my boss' message to police!?**\n\n__Your ID is noted and this account will be hacked soon...__😏")
        else:
            animation_chars = [
        
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",    
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "**Telegram Security Service is on its way here.**",
            "**Telegram Security Service is on its way here..**",
            "**Telegram Security Service is on its way here...**",
            "**Directly entering this Chat.**",
            "**Directly entering this Chat..**",
            "Via",
            "Server",
            "`2048`",
            "`2048.786`",
            "`2048.786.69`",
            "`2048.786.69.1`",
            "Passing through Narrow and Complicated Servers.",
            "Passing through Narrow and Complicated Servers..",
            "**@TechyNewbie Police is here**",
            "**@TechyNewbie Police is here!!**",
            "Looking for Guilty.",
            "Looking for Guilty..",
            "Looking for Guilty...",
            "Getting F.I.R..",
            "Getting F.I.R...",
            "**!!Guilty Arrested!!**",
            "**!! Guilty Arrested !!**",
            "__user BANNED from TELEGRAM__",
            "__USER banned FROM telegram__",
            "__user BANNED from TELEGRAM__",
            f"***JUSTICE***\n\nPolice has arrested [{firstname}](tg://user?id={idd})!"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 37])


MODULE_LIST.append("police")

SYNTAX.update({
    "police": "\
**Requested Module --> police**\
\n\n`.police`\
\nUsage: Call police, make an FIR. Police will arrest the guilty.\
"
})

