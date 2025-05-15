import discord
import asyncio

TOKEN = 'YOUR_USER_TOKEN_HERE'  # Replace with your Discord user token
EMOJI = "💀"
KEYWORDS = ["keyword1", "pattern2", "another word"]  # Add the keywords or patterns you want to trigger the reaction
TARGET_CHANNEL_ID = YOUR_TARGET_CHANNEL_ID_HERE  # Optional: Limit to a specific channel, remove if you want to listen everywhere

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if TARGET_CHANNEL_ID:
        if message.channel.id != TARGET_CHANNEL_ID or message.author == client.user:
            return
    elif message.author == client.user:
        return

    content = message.content.lower()  # Convert to lowercase for case-insensitive matching
    for keyword in KEYWORDS:
        if keyword.lower() in content:
            try:
                await message.add_reaction(EMOJI)
                print(f"Reacted to message in {message.channel.name} by {message.author.name}: '{message.content}' (matched '{keyword}')")
                # Optionally, add a delay here to avoid rapid reactions if multiple keywords are found quickly
                # await asyncio.sleep(0.5)
                break  # React only once per message if multiple keywords match (optional)
            except discord.HTTPException as e:
                print(f"Failed to react: {e}")
            break  # Stop checking other keywords after reacting (optional)

client.run(TOKEN)
