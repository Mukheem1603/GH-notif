import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@commands.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.add_command(test)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.environ['TOKEN'])