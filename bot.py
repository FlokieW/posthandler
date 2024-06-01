import discord
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Replace this with your bot's token
TOKEN = os.getenv('YOUR_DISCORD_BOT_TOKEN')
PRESET_MESSAGE = os.getenv('PRESET_MESSAGE')

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is a DM and is not from the bot itself
    if isinstance(message.channel, discord.DMChannel) and message.author != client.user:
        await message.channel.send(PRESET_MESSAGE)

client.run(TOKEN)