import discord
from discord.ext import commands
import os
import asyncio
from config import BOT_TOKEN, COMMAND_PREFIX

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print(f'Cogs cargados: {list(bot.cogs.keys())}')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_cogs()
    await bot.start(BOT_TOKEN)  # Usar el token desde config.py

asyncio.run(main())