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
re_start = re.compile(r"^https://(?:x|twitter)\.com\/.*\/status\/.*")


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


err_msg = "error"


@client.event
async def on_message(message: discord.Message):
    try:
        if message.author.bot:  # ボットのメッセージは無視
            return

        if re_start.match(message.content):
            match = re_username.match(message.content)

            if match != None:
                matchGroup = match.groups()
                result = f"https://vxtwitter.com/{matchGroup[0]}/status/{matchGroup[1]}"

                if len(result) < 2000:
                    await message.reply(
                        f"https://vxtwitter.com/{matchGroup[0]}/status/{matchGroup[1]}"
                    )
                    return
                
            else:
                await message.channel.send(err_msg)

    except Exception as e:
        await message.channel.send(f"予期してないエラーが発生しました\n```\n{e}\n```")

    finally:
        return


client.run(os.environ["TOKEN"])
