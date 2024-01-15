import json
import logging
import os
import platform
import random
import sys

import aiosqlite
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

from database import DatabaseManager

# Bot setup
bot = commands.Bot(command_prefix='lucky ')
channel_id = YOUR_CHANNEL_ID  # Replace with your Discord channel ID

# Random messages for scheduled posting
lucky_thoughts = ["Time for a walk! ", "Is it dinner time yet?", "How about a treat?", "Nap time... "]

# Scheduled messages (Lucky's thoughts)
@tasks.loop(hours=2)  # Adjust the time as needed
async def post_lucky_thoughts():
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(random.choice(lucky_thoughts))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    post_lucky_thoughts.start()  # Start the loop

# Responding to messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    lower_message = message.content.lower()
    if 'hi lucky' in lower_message or 'hello lucky' in lower_message:
        await message.channel.send(f"Woof! Hello {message.author.name}!")
    elif 'good boy' in lower_message:
        await message.channel.send("Woof woof! 🐾")
    elif 'treat' in lower_message:
        await message.channel.send("Did someone say treats? 🦴")

    await bot.process_commands(message)

# Fetch command
@bot.command()
async def fetch(ctx):
    responses = ["Lucky runs to fetch the ball! 🎾", "Lucky is looking for the stick... 🌳", "Lucky brings back the ball! Good dog! 🐕"]
    await ctx.send(random.choice(responses))

# Help command
@bot.command()
async def help(ctx):
    help_text = "Woof! Need help? I can fetch, play, and do lots of tricks! Just say 'fetch' to play fetch!"
    await ctx.send(help_text)

# Run the bot
bot.run('MTE5NDY1NjI2NjAzNTk0MTUwNw.GZ-O1J.a7NGhqIJmWTDKtH_y7xsI984viAIXq22DMNr8c')
