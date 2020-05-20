"""CoronaVirus LookUp
"""

from covid import Covid
from userbot.utils import admin_cmd
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from global_variables_sql import SYNTAX, MODULE_LIST

@borg.on(admin_cmd(pattern="covid (.*)"))
async def _(event):
    covid = Covid()
    data = covid.get_data()
    country = event.pattern_match.group(1)
    country_data = get_country_data(country, data)
    output_text = "" 
    for name, value in country_data.items():
        output_text += "`{}`: `{}`\n".format(str(name), str(value))
    await event.edit("**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text))

def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return {"Status": "Invalid format!\n\nUse .syntax corona_virus for more info"}


@borg.on(admin_cmd(pattern="corona ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply to text message```")
       return
    chat = '@NovelCoronaBot'
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1124136160))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@NovelCoronaBot) u Nigga```")
              return
          if response.text.startswith("Country"):
             await event.edit("Something Went Wrong Check [This Post](https://t.me/TechnoAyanBoT/22?single)")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)



MODULE_LIST.append("corona_virus")

SYNTAX.update({
    "corona_virus": "\
**Get current Corona Virus stats for any country**\
\n\n• `.covid <country name>`\
\n\n• `.corona <as a reply to country name>`\
\n__Usage: First send the name of the country. Then reply__ `.corona` __to the message.__\
\n\nFirst letter of the country name must be capital!!\
"
})
