import discord
import os
import requests
from discord.ext import commands
import asyncio
import aiohttp


client = commands.Bot(command_prefix='$')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('help'):
        await message.channel.send(f'Heyaa {message.author.name} ❤\nYou can have a look at simple stats of your GitHub profile by a simple command ✨\nThe command: $info yourGitHubusername\n\nHave fun 😁')
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Heyaa {member.name} ❤\nWelcome to our channel 🎉🎊\n \nGreetings from my boss , Mukheem 👨‍💻\n You can have a look at simple stats of your GitHub profile by a simple command ✨\nThe command: $info yourGitHubusername\n\nHave fun 😁'
    )
    
@client.command()
async def echo(ctx,arg):
    await ctx.send(arg)


@client.command()
async def info(ctx,username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/users/{username}") as r:
            if r.status == 200:
                resp = await r.json()
                datatext = f"Name: {resp['name']}\nBio: {resp['bio']}\nPublic Repos: {resp['public_repos']}\nFollowers: {resp['followers']}\nFollowing: {resp['following']} "
                await ctx.send(datatext)
            else:
                await ctx.send("No such user found")
                



client.run(os.environ['TOKEN'])


