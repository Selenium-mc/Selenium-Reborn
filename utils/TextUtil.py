import asyncio
from fuzzywuzzy import process

from utils.GlobalUtil import Globals


# Calculate Levenshtein distance
def find_closest(string, options, margin=75, debug=False):
    match = process.extractOne(string, [*options])
    if debug: print("{} => {}  {} ({}%)".format(string, options, match[0], match[1]))
    return match[0] if match[1] >= margin else False


# Safe filename
def parse_filename(fn):
    return ''.join(c for c in fn if c.isalnum())


# Wait for a user to react
async def wait_react(ctx, msg, emojis, delete=False, existing=False, wait=10.0): # Simplify args
    target = msg if existing else await ctx.send(msg)
    for e in emojis: await target.add_reaction(e)

    def check(reaction, user):
        return reaction.message.id == target.id and user == ctx.message.author and str(reaction.emoji) in emojis

    try:
        reaction, user = await Globals.bot.wait_for('reaction_add', timeout=wait, check=check)
    except asyncio.TimeoutError:
        return False
    else:
        if delete: await target.delete()
        return reaction.emoji
    

# Blink a message
async def blink(ctx, blink, wait=3):
    msg = await ctx.channel.send(blink)
    await asyncio.sleep(wait)
    await msg.delete()


# Shortcut for loading emoji
async def send_loading(channel):
    return await channel.send("<a:discord_loading:779085179657781251>")