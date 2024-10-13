import discord

# intents em all
intents = discord.Intents.all()

# client intents
client = discord.Client(intents=intents)

# evento bot
@client.event
async def on_ready():
    print(f'Logado como {client.user}')

# Token do bot
client.run('TOKEN')
