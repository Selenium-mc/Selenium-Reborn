import discord
from discord.ext import commands


class ReactionAddedEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass


def setup(bot):
    bot.add_cog(ReactionAddedEventCog(bot))
