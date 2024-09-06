import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import MessageEntityBold
import discord
from dotenv import load_dotenv
import os

load_dotenv()

# Read environment variables with a default value for bot_username
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
session_string = os.getenv('TELEGRAM_SESSION_STRING')
bot_username = os.getenv('TELEGRAM_BOT_USERNAME', '@Jotihunt_bot')  # Default to "@Jotihunt_bot"
discord_token = os.getenv('DISCORD_BOT_TOKEN')
discord_channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))

# Initialize Telegram client
telegram_client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Initialize Discord client
intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)

def convert_telegram_formatting(message):
    entities = message.entities or []
    text = message.message
    
    # Sort entities in reverse order by their offset
    entities.sort(key=lambda entity: entity.offset, reverse=True)
    
    for entity in entities:
        if isinstance(entity, MessageEntityBold):
            # Wrap the text with ** for bold
            text = text[:entity.offset] + '**' + text[entity.offset:entity.offset + entity.length] + '**' + text[entity.offset + entity.length:]
           
    return text

@telegram_client.on(events.NewMessage(from_users=bot_username))
async def handler(event):
    # Log in console
    print(f'Telegram: Received message from {event.message.from_id}, content: {event.message.message}')
    # Convert formatting
    formatted_message = convert_telegram_formatting(event.message)
    
    # Send formatted message to Discord
    channel = discord_client.get_channel(discord_channel_id)
    if channel:
        await channel.send(formatted_message)

@discord_client.event
async def on_ready():
    print(f'Discord: Logged in as {discord_client.user}')
    # Start the Telegram client
    await telegram_client.start()
    await telegram_client.run_until_disconnected()

async def main():
    # Start both Telegram and Discord clients
    await discord_client.start(discord_token)
    await discord_client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())