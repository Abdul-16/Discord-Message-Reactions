# Discord-Message-Reactions
This program is a Discord bot written in Python using the Discord.py library. It is designed to retrieve the messages from a specified Discord text channel that have the highest number of reactions within a given year, and output the URLs of those messages.

To use the bot, you will need to have a Discord account and create a bot by following the steps in the Discord Developer Portal. You will also need to invite the bot to your Discord server and give it the necessary permissions to read and send messages.

The bot has a single command, `!check`, which takes three arguments:
`channel`: the Discord text channel that you want to retrieve messages from. You can specify the channel by mentioning it (e.g. #general) or by its ID.
`year`: the year that you want to retrieve messages from.
`limit` (optional): the minimum number of reactions that a message must have in order to be included in the output. If no limit is specified, the default value is 0.

The `!check` command will output the URLs of the messages in the specified channel that have the highest number of reactions within the given year. The URLs are formatted as `https://discord.com/channels/<guild id>/<text channel id>/<message id>`, where `<guild id>` is the ID of the Discord server that the channel belongs to, `<text channel id>` is the ID of the text channel, and `<message id>` is the ID of the message.

The `find_highest_reaction_message()` function is called by the `!check` command and is responsible for finding the messages with the highest number of reactions. It does this by retrieving all of the messages in the specified channel within the given year, and storing them in a dictionary along with their reaction counts. The dictionary is then sorted by reaction count and the messages with the highest reaction counts are selected. Finally, the URLs of the selected messages are returned.

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
