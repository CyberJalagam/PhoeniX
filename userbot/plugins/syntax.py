# Pirated from Priyam's The TG Bot 2.0
# A clean and beautiful alternative to .help
# Syntax (.syntax <module_name>)
from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from global_variables_sql import SYNTAX, MODULE_LIST


MODULE_LIST.append("syntax")

@borg.on(admin_cmd(pattern="syntax ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        module = event.pattern_match.group(1)
        if module:
            if module in SYNTAX:
                await event.edit(SYNTAX[module])
            else:
                await event.edit("Please specify a valid module.")
        else:
            await event.edit("Please specify a module.\n**Tip: Get a list of all modules using .modules**")
