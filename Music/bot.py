import discord, asyncio, youtube_dl
from discord.ext import commands
import os

# from dotenv import load_dotenv

# load_dotenv()


def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ["s."]  # Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)


bot = commands.Bot(command_prefix=get_prefix, description="Multipurpose Discord Bot")


exts = ["music"]  # Add your Cog extensions here


@bot.event
async def on_ready():
    song_name = "Made By Shubh Mittal"
    activity_type = discord.ActivityType.listening
    await bot.change_presence(
        activity=discord.Activity(type=activity_type, name=song_name)
    )
    print(bot.user.name)


for i in exts:
    bot.load_extension(i)


bot.run("NzczOTIzNDMzNTM2NDIxOTI5.X6QSXQ.vZu9hbvsn8VqEDvwNLQRnnCfMes")