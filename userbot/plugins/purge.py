# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from sql.global_variables_sql import SYNTAX, MODULE_LIST
from asyncio import sleep
from telethon import events
from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils import register, errors_handler


@borg.on(events.NewMessage(pattern=r"\.purge", outgoing=True))
@errors_handler
async def fastpurger(event):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await event.get_input_chat()
    msgs = []
    count = 0

    async for msg in event.client.iter_messages(chat,
                                               min_id=event.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(event.reply_to_msg_id)
        if len(msgs) == 100:
            await event.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await event.client.delete_messages(chat, msgs)
    done = await event.client.send_message(
        event.chat_id,
        "`Purge complete!\n`Purged " + str(count) + " messages.",
    )

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Purge of " + str(count) + " messages done successfully.")
    await sleep(2)
    await done.delete()


@borg.on(events.NewMessage(pattern=r"\.purgeme", outgoing=True))
@errors_handler
async def purgeme(event):
    """ For .purgeme, delete x count of your latest message."""
    message = event.text
    count = int(message[9:])
    i = 1

    async for message in event.client.iter_messages(event.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await event.client.send_message(
        event.chat_id,
        "`Private Purge complete!` Purged " + str(count) + " messages.",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Purge of " + str(count) + " messages done successfully.")
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern="^.del$")
@errors_handler
async def delete_it(delme):
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Deletion of message was successful")
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Well, I can't delete a message")


@register(outgoing=True, pattern="^.edit")
@errors_handler
async def editer(edit):
    """ For .editme command, edit your last message. """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "Edit query was executed successfully")


@register(outgoing=True, pattern="^.sd")
@errors_handler
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "Self-destructed successfully")


MODULE_LIST.append("purge")
MODULE_LIST.append("self_destruct")

SYNTAX.update({
    "purge": "\
**A paragraph from Dictionary for purge module**\
\n\n• `.purge`\
\nUsage: Purges all messages starting from the reply.\
\n\n• `.purgeme <no of your messages>`\
\nUsage: Deletes specified no of your latest messages.\
\n\n• `.del`\
\nUsage: Deletes the message you replied to.\
\n\n• `.edit <newmessage>`\
\nUsage: Replace your last message with <newmessage>.\
"
})

SYNTAX.update({
    "self_destruct": "\
**A message that can self-destruct**\
\n\n• `.sd <time> <message>`\
\n\n__Usage: Creates a message that selfdestructs in specified seconds.__\
\nMaximum time: 100.\
"
})
