"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd
from sql.global_variables_sql import SYNTAX, MODULE_LIST


@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` or `.alive` to check if I am alive after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` or `.alive` to check if I am alive after a lil bit.")
    # await asyncio.sleep(2)
    await event.edit("Restarted. Use `.ping` or `.alive` to check if I am alive")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await borg.disconnect()

MODULE_LIST.append("PhoeniX Tools")
SYNTAX.update({
    "PhoeniX Tools": "\
**Requested Module --> PhoeniX Developer Tools**\
\n\n• `.restart`\
\nUsage: __Restarts the bot. Takes 2 mins__\
\n\n• `.shutdown`\
\nUsage: __Shut downs the bot.__\
"
})
