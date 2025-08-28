import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f"{bot.user.name} tá on!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.startswith("!ping"):
        await message.channel.send("Pong!")


print(f"Token carregado? {DISCORD_BOT_TOKEN is not None}")
bot.run(DISCORD_BOT_TOKEN)
