"""Information about PhoeniX UserBot."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from sql.global_variables_sql import SYNTAX, MODULE_LIST

BOSS = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.about$")
async def amireallyalive(alive):
    """ For .about command, check if the bot is running.  """
    await alive.edit("      👍🏻  `PhoeniX UserBot` 🍻\n"
                     "__Telethon: 6.9.0 // Python: 3.7.3\n\n__"
                     "𝐵𝑜𝑡 𝑐𝑟𝑒𝑎𝑡𝑒𝑑 𝑏𝑦:  [Ꮇᑭ 𝕊𝕚𝕟𝔾ℍ✪](t.me/techynewbie)\n"
                     f"𝑀𝑦 𝑀𝑎𝑠𝑡𝑒𝑟: 🎖{BOSS}\n\n"
                     "                  ★彡 [GitHub](https://github.com/Techy05/Phoenix) 彡★\n"
                     "                                                ")
    
MODULE_LIST.append("about")

SYNTAX.update({
    "about": "\
ℹ️ **About this UserBot**\
\n\n• `.alive`\
\n\n__Brings out the information panel for PhoeniX UserBot with credits__ :)\
"
})
