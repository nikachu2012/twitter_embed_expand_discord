import discord
import re
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.none()
intents.messages = True
intents.message_content = True


client = discord.Client(intents=intents)

re_username = re.compile(r"^https://(?:x|twitter)\.com/(.*?)/status/([0-9]*)$")
re_postid = re.compile(r"[0-9]+")


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:  # ボットのメッセージは無視
        return

    match = re_username.match(message.content)

    if match != None:
        matchGroup = match.groups()
        await message.reply(
            f"https://vxtwitter.com/{matchGroup[0]}/status/{matchGroup[1]}"
        )
        return
    else:
        await message.channel.send("蛍は可愛い！！！！")


client.run(os.environ["TOKEN"])