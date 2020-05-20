"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





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
