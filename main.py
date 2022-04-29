import discord
import os
from weather import get_weather
client = discord.Client()



@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!! Please type "$weather" to know weather details of any city')
  
  if message.content.startswith('$weather'):
    city  = message.content.split(' ',8)[1:]
    #print(city)
    weather = get_weather(city[0])
    await message.channel.send(weather)


my_token = os.environ["TOKEN"]

client.run(my_token)