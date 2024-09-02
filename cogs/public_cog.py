import discord
from discord.ext import commands
import random

class PublicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def alice(self, ctx):
        # Embed con opciones principales
        embed = discord.Embed(title="¡Hola! Soy Alice",
                              description="¿Qué te gustaría hacer?\n"
                                          "1️⃣ Interactuar en privado.\n"
                                          "2️⃣ Interacciones públicas.",
                              color=discord.Color.pink())
        mensaje = await ctx.send(embed=embed)

        # Añadir reacciones como opciones
        await mensaje.add_reaction('1️⃣')
        await mensaje.add_reaction('2️⃣')

        # Esperar la respuesta del usuario
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

        reaction, user = await self.bot.wait_for('reaction_add', check=check)

        if str(reaction.emoji) == '1️⃣':
            private_cog = self.bot.get_cog('PrivateCog')
            await private_cog.crear_canal_privado(ctx)
        elif str(reaction.emoji) == '2️⃣':
            await self.interacciones_publicas(ctx)

    async def interacciones_publicas(self, ctx):
        # Embed con opciones adicionales
        embed = discord.Embed(title="Interacciones Públicas",
                              description="¿Qué te gustaría hacer ahora?\n"
                                          "1️⃣ Saber la hora.\n"
                                          "2️⃣ Escuchar un chiste.",
                              color=discord.Color.green())
        mensaje = await ctx.send(embed=embed)
        await mensaje.add_reaction('1️⃣')
        await mensaje.add_reaction('2️⃣')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

        reaction, user = await self.bot.wait_for('reaction_add', check=check)

        if str(reaction.emoji) == '1️⃣':
            await self.decir_hora(ctx)
        elif str(reaction.emoji) == '2️⃣':
            await self.contar_chiste(ctx)

    async def decir_hora(self, ctx):
        from datetime import datetime
        hora_actual = datetime.now().strftime('%H:%M:%S')
        embed = discord.Embed(title="La Hora Actual", description=f"🕒 {hora_actual}", color=discord.Color.orange())
        await ctx.send(embed=embed)

    async def contar_chiste(self, ctx):
        chistes = [
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Cuál es el colmo de Aladdín? Tener mal genio."
        ]
        chiste = random.choice(chistes)
        embed = discord.Embed(title="Chiste", description=chiste, color=discord.Color.purple())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(PublicCog(bot))
