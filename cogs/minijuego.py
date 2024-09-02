import discord
from discord.ext import commands
import random
import requests
import json

class Minijuego(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://raw.githubusercontent.com/Fernando2603/AzurLane/main/skin.json"
        self.personajes = self.cargar_datos()

    def cargar_datos(self):
        response = requests.get(self.url)
        return response.json()  # Carga el JSON completo

    @commands.command(name="az")
    async def drop_personaje(self, ctx):
        skin_id = random.choice(list(self.personajes.keys()))  # Selecciona un ID de skin al azar
        skin = self.personajes[skin_id]  # Obtén los datos de la skin usando el ID

        embed = discord.Embed(title=f"{skin['name']} - {skin['type']}", description=skin['desc'], color=0x00ff00)
        embed.set_image(url=skin['painting'])  # Usa la URL de la imagen en el embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Minijuego(bot))