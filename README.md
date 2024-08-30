# Jotihunt Telegram Forwarder

This is a simple python script that forwards telegram messages to a specified channel in Discord.

## Installation

The easiest way to run this script on a server is using Docker.

1. Copy the `docker-compose.yml` file to your server
2. Edit the environment variables in the `docker-compose.yml` file, or create a `.env` file with the same variables and set the `env_file` variable in the `docker-compose.yml` file to the path of the `.env` file
3. Run `docker-compose up -d`
4. The script will run in the background and will forward messages to the Discord channel specified in the `DISCORD_CHANNEL_ID` environment variable.
5. Happy forwarding!

## Retrieving the Telegram API key

1. Go to [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Create a new app
3. Save the api_id and api_hash

## Generating a Telegram session string

1. Go to [Telegram.tools](https://telegram.tools/session-string-generator#telethon)
2. Make sure environment is set to Production
3. Make sure Account Type is set to Bot.
4. Fill the api_id and api_hash you stored
5. Fill in the phone number of the account that's linked to the Jotihunt bot
6. Generate the session string and save it

## Creating and inviting a Discord bot

1. Go to the [Discord Developer Portal](https://discordapp.com/developers/applications/)
2. Create a new application
3. Go to the bot tab
4. Click on "Reset Token"
5. Save the token
6. Go to the OAuth2 tab
7. Click on "Add redirect" and enter any URL, save changes
8. Select scopes "bot" and "identify" in the URL generator
9. Pick your previously created redirect URL
10. Select needed permissions for the bot (at least "Send Messages", but "Administrator" will definitely work)
11. Open the URL in a browser and add the bot to your server

## Retrieving the Discord channel ID

1. Go to the Discord channel you want to forward messages to
2. Right click on the channel name and select "Copy ID" (might need Developer mode)
