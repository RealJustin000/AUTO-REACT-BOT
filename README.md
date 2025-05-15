# Auto-React Selfbot (Discord.js)

This is a simple Discord selfbot that automatically reacts to messages containing specific keywords or patterns in a Discord channel or across all accessible channels.

**⚠️ Important: Use with Caution! ⚠️**

Using selfbots can violate Discord's Terms of Service and may lead to your account being suspended or terminated. Proceed with caution and understand the risks involved before using this script.

## Features

* **Keyword-based Reactions:** Automatically reacts with a specified emoji to messages containing defined keywords or patterns.
* **Optional Channel Targeting:** You can configure the bot to listen for keywords in a specific channel or across all channels your account can access.
* **Case-Insensitive Matching:** Keywords are matched regardless of the case of the letters in the message.
* **Rate Limit Considerations:** Includes optional delays to help avoid being rate-limited by Discord.

## Prerequisites

* **Node.js and npm:** You need Node.js and npm (Node Package Manager) installed on your system. You can download them from [https://nodejs.org/](https://nodejs.org/).

## Setup

1.  **Clone or Download:** Download the `selfbot.js` file (or the entire repository if you have it).
2.  **Install Dependencies:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    npm install discord.js dotenv
    ```
3.  **Create `.env` File:** Create a file named `.env` in the same directory as your script and add your Discord user token and (optional) target channel ID:
    ```
    DISCORD_USER_TOKEN=YOUR_USER_TOKEN_HERE
    TARGET_CHANNEL_ID=YOUR_OPTIONAL_CHANNEL_ID_HERE
    ```
    * Replace `YOUR_USER_TOKEN_HERE` with your actual Discord user token. See the previous instructions on how to obtain this (be careful not to share it).
    * Optionally, replace `YOUR_OPTIONAL_CHANNEL_ID_HERE` with the ID of the specific channel you want the bot to monitor. If you want to listen in all accessible channels, you can leave this line or comment it out.
4.  **Configure Keywords and Emoji:** Open the `selfbot.js` file and modify the `KEYWORDS` array and the `EMOJI` constant to your desired values:
    ```javascript
    const EMOJI = '💀'; // The emoji to react with
    const KEYWORDS = ["keyword1", "pattern2", "another word"]; // The keywords to trigger the reaction
    ```

## Running the Selfbot

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved `selfbot.js`.
3.  Run the script using Node.js:
    ```bash
    node selfbot.js
    ```

## Configuration

You can configure the following variables in the `selfbot.js` file:

* `TOKEN`: Your Discord user token (recommended to store in `.env` file).
* `EMOJI`: The emoji the bot will use to react to matching messages.
* `KEYWORDS`: An array of strings. If any of these strings (case-insensitive) are found in a message, the bot will react.
* `TARGET_CHANNEL_ID`: (Optional) The ID of a specific Discord channel to monitor. If left undefined or commented out, the bot will listen in all accessible channels.

## Disclaimer

This script is provided for informational and educational purposes only. Using selfbots may violate Discord's Terms of Service. The author is not responsible for any consequences that may arise from using this script, including account suspension or termination. Use at your own risk.
