# bot.py
import os
from dotenv import load_dotenv
import random
from discord import File
from discord.ext import commands

spray_bottle_gifs = ['spray_bottle1.gif', 'spray_bottle2.gif',
'spray_bottle3.gif']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='spray', help='Spray a user who is acting out of line')
@commands.has_role('management')
async def spray_bottle(ctx):
    if len(ctx.message.mentions) != 1:
        await ctx.send("Command message must contain one (1) user mention.")
    else:
        if ctx.message.mentions[0].name == "Kuyashi":
            await ctx.send("You've probably posted something horny, " + ctx.message.mentions[0].mention + ".", file=File("kuyashi_exception.gif"))
        elif ctx.message.mentions[0].name == "David":
            await ctx.send("Carry on, sir. " + ctx.message.mentions[0].mention, file=File("david_exception.gif"))
        elif ctx.message.mentions[0].name == "tangent":
            await ctx.send("Carry on, sir. " + ctx.message.mentions[0].mention, file=File("tangent_exception.gif"))
        else:
            await ctx.send("Stop posting cringe, " + ctx.message.mentions[0].mention + ".", file=File(random.choice(spray_bottle_gifs)))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(str(ctx.author.mention) + ' does not have permission to use this command.')

bot.run(TOKEN)