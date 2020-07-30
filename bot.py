import discord
import os
import requests
from discord.ext import commands,tasks
import asyncio
import aiohttp
from itertools import cycle


client = commands.Bot(command_prefix='$')
status = cycle(['PUBG','VALORANT','MINECRAFT','PACMAN','FORTNITE'])

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def clear(ctx,n=1):
    await ctx.channel.purge(limit=n)

@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))

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

async def followers():
    await client.wait_until_ready()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/users/Mukheem1603/followers") as r1:
            if r1.status == 200:
                resp1 = await r1.json()
                oldcount = len(resp1)
                oldcount = int(oldcount)
        await asyncio.sleep(7)
        async with session.get(f"https://api.github.com/users/Mukheem1603/followers") as r2:
            if r2.status == 200:
                resp2 = await r2.json()
                newcount = len(resp2)
                newcount = int(newcount)
                if newcount > oldcount :
                    channel = client.get_channel(737208902961201174)
                    nfollower = resp2[newcount-1]['login']
                    await channel.send(f"Boss , your following count has been increased.\n{nfollower} started following you.\nOld followers count={oldcount}\nNew followers count={newcount}")
                    await followers()
                elif oldcount > newcount :
                    channel = client.get_channel(737208902961201174)
                    ofollower = resp1[oldcount-1]['login']
                    await channel.send(f"Boss , your following count has been decreased.\n{ofollower} unfollowed you.\nOld followers count={oldcount}\nNew followers count={newcount}")
                    await followers()
                else :
                    await followers()
    
    await followers()

async def fc():
    await client.wait_until_ready()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.github.com/users/Mukheem1603/followers") as r1:
            if r1.status == 200:
                resp1 = await r1.json()
                oldcount = len(resp1)
                oldcount = int(oldcount)
                newcount = oldcount
        while newcount == oldcount:
            async with session.get(f"https://api.github.com/users/Mukheem1603/followers") as r2:
                if r2.status == 200:
                    resp2 = await r2.json()
                    newcount = len(resp2)
                    newcount = int(newcount)
        if newcount > oldcount :
            channel = client.get_channel(737208902961201174)
            nfollower = resp2[newcount-1]['login']
            await channel.send(f"Boss , your following count has been increased.\n{nfollower} started following you.\nOld followers count={oldcount}\nNew followers count={newcount}")
            await followers()       
        elif oldcount > newcount :
            channel = client.get_channel(737208902961201174)
            ofollower = resp1[oldcount-1]['login']
            await channel.send(f"Boss , your following count has been decreased.\n{ofollower} unfollowed you.\nOld followers count={oldcount}\nNew followers count={newcount}")
            await followers()
        

client.loop.create_task(followers())

client.run(os.environ['TOKEN'])


