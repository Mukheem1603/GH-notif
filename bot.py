import discord
import os
import requests
from discord.ext import commands
import asyncio


client = commands.Bot(command_prefix='$')

@client.command()
async def echo(ctx,arg):
    await ctx.send(arg)

@client.command()
async def info(ctx,username):
    r = requests.get(f"https://api.github.com/users/{username}")
    resp = r.json()
    if r:
        datatext = f"Name: {resp['name']}\nBio: {resp['bio']}\nPublic Repos: {resp['public_repos']}\nFollowers: {resp['followers']}\nFollowing: {resp['following']} "
        await ctx.send(datatext)
    else:
        await ctx.send("No such user found")


client.run(os.environ['TOKEN'])


