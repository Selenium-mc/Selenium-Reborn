import discord
from discord.ext import commands


class ReadyEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.bot.user, "has logged into discord!")
        await self.bot.change_presence(activity=discord.Game(name="Selenium Bot v2.0 underway!"))
    

def setup(bot):
    bot.add_cog(ReadyEventCog(bot))
