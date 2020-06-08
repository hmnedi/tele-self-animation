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
    # then your input should be <cmd_message>|<number>|<text> and so on...
    cmd_message = cmd_message.split(' ', 2)

    # checking if the input is based on: <animame> <number> <text>
    # you can change the animame to anything you like
    if cmd_message[0].lower() == 'animame' and cmd_message[1].isdigit() and len(cmd_message) == 3:
        # just making some var to understanding better
        loop_time = int(cmd_message[1])
        repetition_txt = cmd_message[2]
        # you can literally enter anything you like in respond()
        # the text you put there is the message which will be sent but soon
        # will be edited
        message = await event.respond(repetition_txt)

        # making a loop and a loop inside it
        # the first loop is to repeat the repetition, which is the second loop!
        for i in range(loop_time):
            for j in range(len(repetition_txt)):
                # we cannot append ' ' to the end of a message i telegram
                # therefor if txt[j] == ' ' we ignore it,
                # and because we are printing with substring and
                # it contains ' ' so in the next round,
                # it will be added in its place
                if repetition_txt[j] != ' ':
                    await client.edit_message(message, repetition_txt[0:j+1])


client.start()
client.run_until_disconnected()
