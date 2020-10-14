import os
import discord
from discord.ext import commands
import keep_alive
from smtplib import SMTP

client = commands.Bot(command_prefix = ('I', 'i', 'Dad ', 'dad '))

@client.event
async def on_ready():
  print('Bot is ready.')

@client.command(aliases=['\'m', 'm', '’m', 'I\'m', 'im','i\'m'])
@commands.has_permissions(administrator=True)
async def dad_trigger(ctx, *x):
  message = ' '.join(x)
  await ctx.send('Hi ' + message + ', I\'m dad')

@client.command(aliases=['needhelp'])
@commands.has_permissions(administrator=True)
async def need_help(ctx, *x):
  message = ' '.join(x)
  await ctx.send('Hi, I\'m dad bot. I reply to people\'s messages')


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))