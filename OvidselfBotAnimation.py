# 2020 - 8th - june | making animation in telegram using editing via a self-bot
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import logging
import config, sys
import getpass

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

    # Animation a specific message
    if splited_cmd_message[0].lower() == 'animame' and splited_cmd_message[1].isdigit() and len(splited_cmd_message) == 3:
        loop_time = int(splited_cmd_message[1])
        repetition_txt = splited_cmd_message[2]

        message = await event.respond(repetition_txt)
        for i in range(loop_time):
            for j in range(len(repetition_txt)):
                if repetition_txt[j] != ' ':
                    await client.edit_message(message, repetition_txt[0:j+1])
    # Shpw myself information
    if cmd_message == '!whoami':
        me = await client.get_me()
        resultText = "i'm {} with user_id: {}".format(me.first_name, me.id)
        message = await event.respond(resultText)


try:
    client.start()
    client.run_until_disconnected()
except Exception as error:
    throwError(error)