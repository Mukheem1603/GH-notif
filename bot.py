import discord
import os
import requests
from discord.ext import commands


bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def info(ctx, arg):
    r = requests.get(f"https://api.github.com/users/{arg}")
    resp = r.json()
    if r:
        await ctx.send(resp['name'])
    else:
        await ctx.send("No such user found")

    
    

bot.run(os.environ['TOKEN'])


