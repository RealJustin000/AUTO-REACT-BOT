import discord
import asyncio

TOKEN = 'YOUR_USER_TOKEN_HERE'  # Replace with your Discord user token
EMOJI = "💀"
REACTION_COUNT = 20
TARGET_MESSAGE_ID = YOUR_TARGET_MESSAGE_ID_HERE  # Replace with the ID of the message you want to react to
TARGET_CHANNEL_ID = YOUR_TARGET_CHANNEL_ID_HERE  # Replace with the ID of the channel containing the message

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    await react_to_message()
    await client.close()  # Close the connection after reacting

async def react_to_message():
    try:
        channel = client.get_channel(TARGET_CHANNEL_ID)
        if channel is None:
            print(f"Could not find channel with ID: {TARGET_CHANNEL_ID}")
            return

        message = await channel.fetch_message(TARGET_MESSAGE_ID)
        if message is None:
            print(f"Could not find message with ID: {TARGET_MESSAGE_ID}")
            return

        for _ in range(REACTION_COUNT):
            await message.add_reaction(EMOJI)
            await asyncio.sleep(0.3)  # Delay to avoid rate limiting
        print(f"Successfully added {REACTION_COUNT} {EMOJI} reactions to message {TARGET_MESSAGE_ID} in channel {TARGET_CHANNEL_ID}")

    except discord.HTTPException as e:
        print(f"Failed to react: {e}")
    except discord.NotFound:
        print("Could not find the specified channel or message.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

client.run(TOKEN, bot=False)
