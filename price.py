import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
from replit import db
from threading import Timer
import json
import string
from time import sleep

client = discord.Client()
bot = Bot("!")


@client.event
async def on_message(message):
    if message.content == 'price':
        r = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd').text
        r = json.loads(r)

        price = float(r['ripple']['usd'])
        await message.guild.me.edit(nick='XRP ' + str(price) + '$')


BOT_TOKEN = 'token'
client.run(BOT_TOKEN)
