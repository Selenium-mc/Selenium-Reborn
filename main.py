import discord
from discord.ext import commands

import utils.WalkUtil as WalkUtil
from utils.GlobalUtil import Globals

import uptime
import os



# Initialize bot
intents = discord.Intents.default()
intents.members = True
intents.reactions = True

uptime.start()
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)

# Add globals
Globals.bot = bot

# Load commands and events
for com in WalkUtil.walk(
    "commands",
    lambda fn: fn.endswith(".py") and not "__init__" in fn,
    lambda rt: "_sub" in rt or "__pycache__" in rt):

    bot.load_extension(com)

for eve in WalkUtil.walk(
    "events",
    lambda fn: fn.endswith(".py") and not "__init__" in fn):

    bot.load_extension(eve)
    

# Start bot instance
if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
