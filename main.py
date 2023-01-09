# PROGRAMMER: Abdullah Bharde
# DATE CREATED: 9th Jan 2023                    
# REVISED DATE: 
# PURPOSE: To find the messages in a specified Discord channel that have the most 
#          reactions within a specified year. The check function takes three required  
#          arguments: `ctx`, `channel`, and `year`, and one optional argument `limit`.
#          ctx is a context object that is passed to the function automatically when  
#          the command is run. `channel` is an object representing the Discord channel  
#          in which the messages are being searched for. `year` is an integer representing  
#          the year for which the messages are being searched for. `limit` is an integer 
#          representing the minimum number of reactions a message must have to be considered.
#          The function searches through the channel history for messages with reactions 
#          within the specified year and returns the messages with the highest number of reactions.

import discord
from discord.ext import commands
import os
from datetime import datetime

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
  print("Bot is ready!")


@client.command()
async def check(ctx, channel: discord.TextChannel, year: int, limit: int = 0):
  """
  This function searches for the highest reaction message in a given channel for each month 
  in a given year, within a given minimum reaction limit. It sends the URL of the highest 
  reaction message for each month to the Discord channel specified in the ctx parameter. 
  If no message is found that meets the criteria for a given month, it sends a message 
  indicating that no message was found to console.

  Inputs:
  - ctx: a Discord context object, used to specify the Discord channel to send the output to.
  - channel: a Discord channel object representing the channel to search for messages in.
  - year: an integer representing the year to search in.
  - limit: an integer representing the minimum number of reactions a message must have to be 
    considered the highest reaction message. If not specified, the default value is 0.

  Output:
  - Sends a message to the Discord channel specified in the ctx parameter for each month in the 
    given year, containing the URL of the highest reaction message for that month (if one was found) 
    or a message indicating that no message was found.
  """
  
    names_months={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',
                    9:'Sep', 10:'Oct',11:'Nov', 12:'Dec'}
    for month in range(1,13):    
        if month!=12 and month!=1:
            after_year = f"{year}-{month}-01"
            before_year = f"{year}-{month+1}-01"
            after_datetime = datetime.strptime(after_year, "%Y-%m-%d")
            before_datetime = datetime.strptime(before_year, "%Y-%m-%d")
        elif month ==1:
            after_year = f"{year-1}-12-31"
            before_year = f"{year}-{month+1}-01"
            after_datetime = datetime.strptime(after_year, "%Y-%m-%d")
            before_datetime = datetime.strptime(before_year, "%Y-%m-%d")
        elif month ==12:
            after_year = f"{year}-{month}-01"
            before_year = f"{year+1}-01-01"
            after_datetime = datetime.strptime(after_year, "%Y-%m-%d")
            before_datetime = datetime.strptime(before_year, "%Y-%m-%d")
    
        highest_reaction_message = await find_highest_reaction_message(client, channel, year, limit,after_datetime,before_datetime)
        if highest_reaction_message:
            await ctx.send(f"{names_months[month]}: {' '.join(highest_reaction_message)}")
        else:
            #await ctx.send(f"{month}: No messages found within the given criteria.")
            print(f"{month}: No messages found within the given criteria.")
            #pass
        

async def find_highest_reaction_message(client, channel, year, limits, after_datetime,before_datetime):
    """
    This function searches through the history of a given channel and returns 
    a list of URLs for messages that have a number of reactions equal to or 
    greater than a given limit, within a given time period.

    Inputs:
    - client: a Discord client object.
    - channel: a Discord channel object.
    - year: an integer representing the year to search in.
    - limits: an integer representing the minimum number of reactions a message 
      must have to be included in the output.
    - after_datetime: a datetime object representing the start of the time period 
      to search in.
    - before_datetime: a datetime object representing the end of the time period 
      to search in.

    Output:
    - A list of strings, where each string is a URL for a message that meets the 
    search criteria. If no messages meet the criteria, the function returns None.
    """
    
    message_reaction_counts = {}

    async for message in channel.history(limit=None, after=after_datetime, before=before_datetime):

      reaction_count = 0
      for reaction in message.reactions:
        reaction_count += reaction.count
 
        message_reaction_counts[message] = reaction_count
   
    sorted_message_reaction_counts = sorted(message_reaction_counts.values(), key=lambda item: item, reverse=True)    
    
    final_sorted_message_reaction_counts = {}
    for message, reaction_count in message_reaction_counts.items():
        if reaction_count >= limits:
            final_sorted_message_reaction_counts[message]= reaction_count
    
    message_urls = []
    for message in final_sorted_message_reaction_counts.keys():
        message_urls.append(f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
    return message_urls if message_urls else None

client.run("TOKEN_HERE")
