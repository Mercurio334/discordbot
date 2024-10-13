import discord

# intents em default
intents = discord.Intents.default()

# client intents
client = discord.Client(intents=intents)

# resposta do bot
@client.event
async def on_ready():
    print(f'Logado como {client.user}')

# Token do bot
client.run('TOKEN')
