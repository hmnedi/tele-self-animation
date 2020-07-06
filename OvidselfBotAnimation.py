# 2020 - 8th - june | making animation in telegram using editing via a self-bot
from telethon import TelegramClient, events
import logging

# Use your own values from my.telegram.org
api_id = 1234
api_hash = 'dsfoi4r3....'
# Start your app I don't know! this is for printing the error and...
client = TelegramClient('anon', api_id, api_hash)
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)


# making an event for receiving a message
@client.on(events.NewMessage)
async def animame(event):
    # converting to string the message user's entered:
    cmd_message = str(event.raw_text)

    # splitting the string just by the first two spaces:
    # NOTE: you can change the split(' ') to anything like split('|')
    cmd_message = cmd_message.split(' ', 2)

    # checking if the input is based on: <animame> <number> <text>
    if cmd_message[0].lower() == 'animame' and cmd_message[1].isdigit() and len(cmd_message) == 3:
        loop_time = int(cmd_message[1])
        repetition_txt = cmd_message[2]
        # you can literally enter anything you like in respond()
        message = await event.respond(repetition_txt)

        # the first loop is to repeat the repetition, which is the second loop!
        for i in range(loop_time):
            for j in range(len(repetition_txt)):
                # we cannot append ' ' to the end of a message i telegram
                if repetition_txt[j] != ' ':
                    await client.edit_message(message, repetition_txt[0:j+1])


client.start()
client.run_until_disconnected()
