# Exclusive module for PhoeniX
# By @Techy05
# Syntax (.error <error_name>)
from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from sql.global_variables_sql import SYNTAX, MODULE_LIST, ERROR, ERRORS


MODULE_LIST.append("error")

@borg.on(admin_cmd(pattern="error ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        err = event.pattern_match.group(1)
        if err:
            if err in ERROR:
                await event.edit(ERROR[err])
            else:
                await event.edit("Please specify a real error.")
        else:
            await event.edit("Please specify an error.\n**Tip: Get a list of all errors using .errors**")
