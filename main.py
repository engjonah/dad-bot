import os
import discord
from discord.ext import commands
import keep_alive
from smtplib import SMTP

intents = discord.Intents.default()
intents.message_content = True

#different prefixes as workaround to capitalization etc.
client = commands.Bot(command_prefix = ('I', 'i', 'Dad ', 'dad '), intents=intents)

@client.event
async def on_ready():
  print('Bot is ready.')

#Many different aliases to make most cases work 
@client.command(aliases=['\'m', 'm', '’m', 'I\'m', 'im','i\'m', 'Im', 'IM', 'M'])
#@commands.has_permissions(administrator=False)
async def dad_trigger(ctx, *x):
  message = ' '.join(x)
  await ctx.send('Hi ' + message + ', I\'m dad')

@client.command(aliases=['needhelp'])
#@commands.has_permissions(administrator=False)
async def need_help(ctx, *x):
  message = ' '.join(x)
  await ctx.send('Hi, I\'m dad bot. I reply to people\'s messages')


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
