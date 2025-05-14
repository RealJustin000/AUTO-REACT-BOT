README.md# Discord Emoji Reactor Self-Bot

## Warning: Use at Your Own Risk

**This script uses a self-bot, which is against Discord's Terms of Service and may result in your account being suspended or banned.** I strongly advise against using this on your primary Discord account. This code is for educational purposes only.

## Description

This Python script is a self-bot that adds a specific emoji reaction to a target message in a Discord channel a specified number of times.

## Features

* Reacts to a specified message with a given emoji.
* Includes a delay to help avoid rate limits.
* Requires the user to input the Discord user token, target message ID, and target channel ID.

## Prerequisites

* Python 3.6 or higher
* `discord.py` library
* Discord account
* Developer Mode enabled in Discord

## Setup

1.  **Install Python:** Ensure you have Python 3.6 or a later version installed on your system.
2.  **Install `discord.py`:**
    ```bash
    pip install discord.py
    ```
    or
    ```bash
    python3 -m pip install discord.py
    ```
3.  **Enable Developer Mode in Discord:**
    * Open Discord.
    * Go to User Settings (the gear icon near the bottom left).
    * Click on "Advanced."
    * Toggle "Developer Mode" to the on position.
4.  **Get your User Token:**
    * Open your browser's developer tools (e.g., Ctrl+Shift+I in Chrome/Firefox).
    * Log in to Discord in your browser.
    * Go to the Network tab.
    * Look for a request to `https://discord.com/api/v*/users/@me`.
    * Find the `Authorization` header in the request headers. Your user token is the long string of characters after `Bearer `.
    * **Keep your user token secret! Do not share it with anyone.**
5.  **Get the Target Message ID and Channel ID:**
    * In Discord, with Developer Mode enabled, right-click on the target message.
    * Select "Copy ID." This is the Message ID.
    * Right-click on the channel containing the message.
    * Select "Copy ID." This is the Channel ID.
6.  **Download the script:** Save the provided Python code (given in previous response) to a file, e.g., `react.py`.
7.  **Configure the script:**
    * Open the `react.py` file in a text editor.
    * Replace `'YOUR_USER_TOKEN_HERE'` with your actual user token.
    * Replace `'YOUR_TARGET_MESSAGE_ID_HERE'` with the ID of the message you want to react to.
    * Replace `'YOUR_TARGET_CHANNEL_ID_HERE'` with the ID of the channel containing the message.
    * Modify the `EMOJI` variable if you want to use a different emoji.
    * Modify the `REACTION_COUNT` variable to change the number of times the script will react.

## Usage

1.  Open a terminal or command prompt.
2.  Navigate to the directory where you saved the `react.py` file.
3.  Run the script:
    ```bash
    python react.py
    ```

## Disclaimer

This script is intended for educational purposes only. Self-bots violate Discord's Terms of Service, and using them may result in account termination. The author is not responsible for any consequences that may arise from using this script.  You are using this at your own risk.
requirements.txtdiscord.py
