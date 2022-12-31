import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot
import requests
import time
import sys

openai.api_key = "isi api dari open ai"
bot = AsyncTeleBot('isi api dari telegram')

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Silahkan masukkan pertannyan?\
""")

@bot.message_handler(commands=['help'])
async def send_welcome(message):
    await bot.reply_to(message, """\
/start memulai CatErBot \n
/help bantuan! \n
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])

print("""
██████   ██████  ████████
██   ██ ██    ██    ██
██████  ██    ██    ██
██   ██ ██    ██    ██
██████   ██████     ██
""")

z = """
                 Checking the Server !!!
[+]█████████████████████████████████████████████████[+]
                    SERVER RUNNING !!!
"""

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

while True:
    try:
        asyncio.run(bot.polling())
    except:
        pass
