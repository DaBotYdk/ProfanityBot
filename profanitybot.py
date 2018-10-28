import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os

swears = ['fuck','shit','bitch','dick','ass','tit']

pfnt = ["Watch your profanity, ","Don't swear on my Christian Discord server, "]

Client = discord.Client()

client = commands.Bot(command_prefix = "$")


@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    for swr in swears:
        if swr in message.content.lower():
            await client.send_message(message.channel, (random.choice(pfnt) + str(message.author) + '!'))

client.run(os.getenv("TOKEN"))
