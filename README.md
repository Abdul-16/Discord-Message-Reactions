# Discord-Message-Reactions
This Discord bot allows you to get the messages in a particular channel that have the highest number of reactions.

# Prerequisites

    Discord account and server
    Python 3.5 or higher
    Discord API wrapper for Python (e.g. Discord.py)
    A bot account on Discord

# Installation

    Install Discord.py by running pip install discord.py in your terminal.
    Clone this repository or download the script and save it to a local directory.
    Create a bot account on Discord and obtain its token.
    Replace TOKEN_HERE in the script with your bot's token.
    Invite your bot to your server by generating an invitation link here.

# Usage

    Run the script with python main.py.
    In your Discord server, type !check #channel-name year in a text channel where 
    the bot has permissions. Replace #channel-name with the name of the channel you 
    want to search and year with the year you want to search in.
    
    The bot will return a list of message URLs with the highest number of reactions 
    within the specified year, sorted by the number of reactions in descending order.
    Optionally, you can also specify a limit parameter after the year to only return 
    messages with at least a certain number of reactions. 
    For example, !check #channel-name year 100 will only return messages with at least 100 reactions.

# Note

    The bot will search for messages within the year specified, from January 1st to December 31st.
    The bot will only search for messages that it has access to, i.e. messages in channels that it can read.
    The bot will not return messages that have been deleted.
    
# License

This project is licensed under the MIT License - see the LICENSE file for details.
