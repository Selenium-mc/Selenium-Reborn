import discord
from discord.ext import commands

from utils.GlobalUtil import Globals

import time


async def log(title, body, color):
    logChannel = Globals.bot.get_channel(803712034801582151)
    logEmbed = discord.Embed(
        title       = "**{} Log**".format(title),
        description = body,
        color       = color
    )
    logEmbed.set_footer(text=str(time.ctime(time.time())))
    
    await logChannel.send(embed=logEmbed)
    