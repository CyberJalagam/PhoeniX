"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from sql.global_variables_sql import SYNTAX, MODULE_LIST

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.about$")
async def amireallyalive(alive):
    """ For .about command, check if the bot is running.  """
    await alive.edit("      👍🏻  `PhoeniX!` 🍻\n"
                     "__Telethon: 6.9.0 // Python: 3.7.3\n\n__"
                     "𝐵𝑜𝑡 𝑐𝑟𝑒𝑎𝑡𝑒𝑑 𝑏𝑦:  [SnapDragon](t.me/null7410) , [anubis](t.me/anubisxx)\n"
                     f"𝐹𝑎𝑖𝑡𝒉𝑓𝑢𝑙𝑙𝑦 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: 🎖{DEFAULTUSER}\n\n"
                     "                  ★彡 [GitHub](https://github.com/MPSinGH2005/X-tra-Telegram) 彡★\n"
                     "                                                ")
    
MODULE_LIST.append("about")

SYNTAX.update({
    "about": "\
ℹ️ **About this UserBot**\
\n\n• `.alive`\
\n\n__Brings out the information panel for this UserBot with credits__ :)\
"
})
