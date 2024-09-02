import discord
from discord.ext import commands

class PrivateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def crear_canal_privado(self, ctx):
        # Verificar si ya existe un canal privado para el usuario
        canal_existente = discord.utils.get(ctx.guild.text_channels, name=f'alice-{ctx.author.name}')
        if canal_existente:
            await ctx.send(f"{ctx.author.mention}, ya tienes un canal privado: {canal_existente.mention}")
        else:
            # Crear un canal privado solo para el usuario y el bot
            guild = ctx.guild
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            canal_privado = await guild.create_text_channel(f'alice-{ctx.author.name}', overwrites=overwrites)
            await canal_privado.send(f"{ctx.author.mention} ¡Bienvenido a tu canal privado con Alice! 🎉")


    @commands.command()
    async def salir(self, ctx):
        # Verificar si el canal es privado
        if ctx.channel.name.startswith('alice-'):
            await ctx.channel.delete()
        else:
            await ctx.send("Este comando solo puede ser usado en un canal privado.")


async def setup(bot):
    await bot.add_cog(PrivateCog(bot))
