# Bot News

This is a simple Discord bot built with Python that provides various news-related functionalities. The bot can fetch news articles related to AI, cybersecurity, and video games from the News API. Additionally, it can provide inspirational quotes using the ZenQuotes API and respond to basic commands.

## Features

- **News**: The bot can fetch the latest news articles related to AI, cybersecurity, and video games.
- **Quotes**: Get inspirational quotes by sending the `!quote` command.
- **Greetings**: The bot responds to a `!hello` command with a greeting.

## Prerequisites

Before you can use this bot, you need to set up the following:

- **Discord Bot Token**: You will need a Discord bot token, which you can obtain by creating a new bot on the [Discord Developer Portal](https://discord.com/developers/applications).
- **News API Key**: You will need an API key from the [News API](https://newsapi.org/) to fetch news articles.
- **ZenQuotes API**: The bot uses the ZenQuotes API to get inspirational quotes.

## Installation

1. Clone this repository or download the code to your machine.
2. Install the required Python packages using pip (ideally in a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the same directory as `bot.py` and add your Discord bot token and News API key:

   ```
   TOKEN=your_discord_bot_token_here
   API_Key=your_news_api_key_here
   ```

## Usage

1. Run the bot by executing the following command in your terminal:

   ```bash
   python bot.py
   ```

2. Invite the bot to your Discord server using the bot's OAuth2 URL generated in the Discord Developer Portal.

3. You can now interact with the bot on your Discord server using the following commands:

   - `!hello`: The bot responds with a greeting.
   - `!quote`: Get an inspirational quote.
   - `!ai`: Get the latest news article related to AI.
   - `!sec`: Get the latest news article related to cybersecurity.
   - `!vg`: Get the latest news article related to video games.
   - `!test`: Get the top 5 news articles related to AI.
