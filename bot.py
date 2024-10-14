import discord
from discord.ext import commands

# intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?', intents=intents)

# event
@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

# comando prefix
@bot.command()
async def ping(ctx):
    await ctx.send(f"pong")

# Token do bot
client.run('TOKEN')
