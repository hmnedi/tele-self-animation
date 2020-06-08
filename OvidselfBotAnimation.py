# 2020 - 8th - june | making animation in telegram using editing via a self-bot
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import logging
import config, sys
import getpass
import asyncio
from pprint import pprint


instance =  input('Enter your instance name [example: ovid]: ') if len(sys.argv) < 2 else sys.argv[1]
# Start your app I don't know! this is for printing the error and...
client = TelegramClient(instance, config.api_id, config.api_hash)
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)

def throwError(error):
    print("[Error]: ", error)

# making an event for receiving a message
@client.on(events.NewMessage)
async def animame(event):
    cmd_message = str(event.raw_text)
    splited_cmd_message = cmd_message.split(' ', 2)
    me = await client.get_me()

    # Animation a specific message
    if splited_cmd_message[0].lower() == '!animame' and splited_cmd_message[1].isdigit() and len(splited_cmd_message) == 3:
        loop_time = int(splited_cmd_message[1])
        repetition_txt = splited_cmd_message[2]

        message = await event.edit(repetition_txt)
        for i in range(loop_time):
            for j in range(len(repetition_txt)):
                if repetition_txt[j] != ' ':
                    await client.edit_message(message, repetition_txt[0:j+1])
                    
    # Animation heart
    if splited_cmd_message[0].lower() == '!heart' and splited_cmd_message[1].isdigit():
        loop_time = int(splited_cmd_message[1])

        emojies = ["❤️", "💋", "😘", "😂"]

        message = await event.edit("😍")
        for i in range(loop_time):
            for emoji in emojies:
                await asyncio.sleep(0.5)
                await client.edit_message(message, emoji)

    # Animation heart
    if cmd_message == '!selfhelp':
        helpText = """📍 راهنمای دستورات سلف :
➖➖
!me
💭 ارسال اطلاعات عمومی اکانت

!animame [Loop] [Emojies]
💭 لوپ چند شکلک به ترتیب

!heart [Loop]
💭 لوپ شکلک های قلبی

!id [reply]
💭 ارسال اطلاعات یک اکانت با ریپلای

!stats
💭 ارسال آمار اکانت
"""
        await event.edit(helpText)

    # Show account stats
    if cmd_message == '!stats':
        await event.edit('**My stats is loading...**')
        dialogs = await client.get_dialogs()
        count_all = 0
        count_users = 0
        count_groups = 0
        count_channels = 0
        count_bots = 0
        for d in dialogs:
            count_all += 1
            if d.is_user:
                if d.entity.bot:
                    count_bots += 1
                else:
                    count_users += 1
            elif d.is_group:
                count_groups += 1
            elif d.is_channel:
                count_channels += 1

        resultText = "**My Stats**\n\nUsers: `{}`\nGroups: `{}`\nChannels: `{}`\nBots: `{}`\nAll: `{}`".format(count_users, count_groups, count_channels, count_bots, count_all)
        await event.edit(resultText)

    # Show myself information
    if cmd_message == '!me':
        resultText = "i'm {} with user_id: {}".format(me.first_name, me.id)
        await event.edit(resultText)
    
    # Show another information by reply
    if cmd_message == '!id':
        rep = await event.get_reply_message()
        sender = rep.sender
        username = "@{}".format(sender.username) if sender.username != None else None
        first_name = "[{}](tg://user?id={})".format(sender.first_name, sender.id)
        resultText = "First Name: {}\nLast Name: **{}**\nFrom ID: **{}**\nUsername: **{}**".format(first_name, sender.last_name, sender.id, username)
        await client.send_message(me.id, resultText)
        await event.edit(resultText)
        
try:
    client.start()
    client.run_until_disconnected()
except Exception as error:
    throwError(error)