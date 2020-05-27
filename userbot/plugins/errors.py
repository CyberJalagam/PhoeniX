# Credits --> @authoritydmc and Priyam Kalra and @HawkEyesMohak
# A dictionary of errors. With solutions ofc.
# Syntax (.errors)

from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from sql.global_variables_sql import ERRORS


@borg.on(admin_cmd(pattern="errors ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    erros = "💫  **List of known errors in Userbots**\n"
    ERRORS.sort()
    prev = "1"
    num = 0
    for err in ERRORS:
        num += 1
        if prev[0] != err[0]:
            erros += f"\n\t{err[0].upper()}\n"
        erros += f"-  ```{err}```\n"
        prev = err
    erros += f"\n\n__Number of solutions loaded:__ {num}\n**Tip:** Use .error <error_name> for more info."
    await event.edit(erros)
