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
            await ctx.send(f"{month}: {highest_reaction_message}")
            """paginator = commands.Paginator()
                                    for message in highest_reaction_message:
                                        paginator.add_line(str(message))
                            
                                    for page in paginator.pages:
                                        await ctx.send(page)"""
        else:
            await ctx.send(f"{month}: No messages found within the given criteria.")
        

async def find_highest_reaction_message(client, channel, year, limits, after_datetime,before_datetime):
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
