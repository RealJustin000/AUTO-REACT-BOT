const { Client, GatewayIntentBits } = require('discord.js');
const dotenv = require('dotenv'); // For securely storing your token
dotenv.config();

const TOKEN = process.env.DISCORD_USER_TOKEN; // Set your user token in a .env file
const EMOJI = '💀';
const KEYWORDS = ["hi", "bye", "nigga"]; // Add your keywords
const TARGET_CHANNEL_ID = process.env.TARGET_CHANNEL_ID; // Optional: Set in .env for a specific channel

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent, // Required to read message content
    ],
});

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', async (message) => {
    if (TARGET_CHANNEL_ID && message.channel.id !== TARGET_CHANNEL_ID) {
        return;
    }

    if (message.author.id === client.user.id) {
        return;
    }

    const content = message.content.toLowerCase();

    for (const keyword of KEYWORDS) {
        if (content.includes(keyword.toLowerCase())) {
            try {
                await message.react(EMOJI);
                console.log(`Reacted to message in ${message.channel.name} by ${message.author.tag}: '${message.content}' (matched '${keyword}')`);
                // Optional: Add a delay here to avoid rate limiting
                // await new Promise(resolve => setTimeout(resolve, 500));
                break; // React only once per message (optional)
            } catch (error) {
                console.error('Failed to react:', error);
            }
            break; // Stop checking other keywords after reacting (optional)
        }
    }
});

client.login(TOKEN);
