import discord
from discord import Intents
from discord.ext import commands

intents = Intents.default()
bot = commands.Bot(command_prefix='>', description="Help Bot", intents=intents)

@bot.command()
#el comando ping envia una señal y recibe una respuesta
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, num1=int, num2=int):
    await ctx.send(num1 + num2)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Información del bot", description="Este es el bot que se encuentra en el servidor", color=0x00ff00)
    embed.add_field(name="Nombre", value=bot.user.name, inline=False)
    embed.add_field(name="ID", value=bot.user.id, inline=False)
    embed.add_field(name="Bot", value=bot.user.bot, inline=False)
    embed.add_field(name="Version", value=discord.__version__, inline=False)
    embed.add_field(name="Prefix", value=bot.command_prefix, inline=False)
    await ctx.send(embed=embed)

#Evento
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutoriales",
    url="https://twitch.tv/accountname"))
    print('Bot_ready')
    # print(bot.user.name)
    # print(bot.user.id)
    # print('------')

#token
bot.run('MTA5NjU1MDU4ODA5Mjc4ODc5Ng.G3jMHl.j0mxKEnssalbVbV-Usvgug2l36qosPjSdmwyTY')