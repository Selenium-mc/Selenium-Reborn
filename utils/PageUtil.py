import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


# Cycle through Text
async def ViewText(ctx, pages,
                   wait   = 60.0,
                   delete = False):
    index = 0
    target = await ctx.send(pages[index])
    
    while True:
        react = await TextUtil.wait_react(
            ctx,
            target,
            ["⏮️", "⬅️", "➡️", "⏭️", "⏹️"],
            existing = True,
            wait = wait
        )
        
        if react:
            await target.remove_reaction(react, ctx.message.author)
            if   react == "⏮️": index = 0
            elif react == "⬅️": index = max(0, index-1)
            elif react == "➡️": index = min(len(pages)-1, index+1)
            elif react == "⏭️": index = len(pages)-1
            elif react == "⏹️": break
            # elif react == ""
        else: break

        await target.edit(content=pages[index])

    for r in ["⏮️", "⬅️", "➡️", "⏭️", "⏹️"]:
        await target.clear_reaction(r)


# Cycle through embeds
async def ViewEmbed(ctx, draw, pages,
                    wait=60.0,
                    delete = False):
    index = 0
    target = await ctx.send(embed=draw(pages, index))
    
    while True:
        react = await TextUtil.wait_react(
            ctx,
            target,
            ["⏮️", "⬅️", "➡️", "⏭️", "⏹️"],
            existing = True,
            wait = wait
        )
        
        if react:
            await target.remove_reaction(react, ctx.message.author)
            if   react == "⏮️": index = 0
            elif react == "⬅️": index = max(0, index-1)
            elif react == "➡️": index = min(len(pages)-1, index+1)
            elif react == "⏭️": index = len(pages)-1
            elif react == "⏹️": break
        else: break

        await target.edit(embed=draw(pages, index))

    for r in ["⏮️", "⬅️", "➡️", "⏭️", "⏹️"]:
        await target.clear_reaction(r)