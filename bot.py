import discord
import os
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Heyaa {member.name}, welcome!!!'
    )

@commands.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.add_command(test)

client.run(os.environ['TOKEN'])
