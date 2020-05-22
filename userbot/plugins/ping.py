from telethon import events
from datetime import datetime
from sql.global_variables_sql import SYNTAX, MODULE_LIST

@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))
    
    
@command(pattern="^.alive")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Yeah!")
    end = datetime.now()
    await event.edit("Yeah! 👍🏻 I'm Alive 🍻")

MODULE_LIST.append("ping")
                     
SYNTAX.update({
    "ping": "\
**Checks if PhoeniX is working or not!!**\
\n\n  `.ping`\
\nUsage: __Ping-Pong!!__\
\n\n `.alive`\
\nUsage: __Same as .ping__\
"
})
