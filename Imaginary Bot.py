# Import Discord Package
import discord

# Client
client = discord.Client()

@client.event
# DO STUFF....
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello There!')

  if message.content.startswith('friend'):
   await message.channel.send('m-me?')

  if message.content.startswith('crystal'):
   await message.channel.send('WHO MENTIONED MY SCRIPTER???')


  if message.content.startswith('*help'):
   await message.channel.send('Still In Development')
# Run The Client
client.run('ODE1ODU0NjM1NzE3MzYxNjY0.YDyd1w.bkKeaAfC9EARTCkL9Ni66ETAAPQ')
