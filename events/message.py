import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil
import utils.LogUtil  as LogUtil

import requests
import string
import os
import re


class MessageEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.regex = {
            #"video" : re.compile(r"^(?:<@!\d+>\s*)*((?:https?:\/\/)?(?:w{3}\.)?youtu(?:\.be[\/\\]|be\.co(?:m|\.\w+)[\/\\](?:watch\?v=)?)\w+)(?:\s*<@!\d+>)*\s*$"),
            "number": re.compile(r"(\d+)(\s*-.*)?")
        }

        # QOL variables
        self.alphanumeric = string.ascii_letters + string.digits


    @commands.Cog.listener()
    async def on_message(self, message):
        # Prevent bot from replying to itself
        if message.author == self.bot.user: return
        

        # Automatically move videos
        if message.channel.id != 759924194262646814:
            match = self.regex["video"].search(message.content)
        
            if match != None:
                channel  = self.bot.get_channel(759924194262646814)
                metadata = requests.get("https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={}".format(match.group(1))).json()
                
                embed = discord.Embed(
                    title       = metadata["title"],
                    description = message.content,
                    color       = 0x0D7375
                )
                embed.set_author(
                    name     = message.author.display_name,
                    icon_url = message.author.avatar_url
                )
                embed.set_image( # set_thumbnail
                    url = metadata["thumbnail_url"].replace("hqdefault", "maxresdefault")
                )
                embed.set_footer(text = "Automatically moved to this channel")
                await channel.send(embed = embed)

                await message.delete()
        

        # Counting functionality
        elif message.channel.id == 776554955418501141:
            match = self.number_pattern.search(message.content)
            cdata = JsonUtil.get("count")

            if match and\
                int(match.group(1)) == (v := cdata["value"] + 1) and\
                message.author.id != cdata["uid"]:
                cdata = {
                    "value": v,
                    "uid": message.author.id
                }
                
                JsonUtil.dump("count", cdata)

            else:
                await message.delete()



def setup(bot):
    bot.add_cog(MessageEventCog(bot))
