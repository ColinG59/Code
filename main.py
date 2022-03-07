from os import listdir
from os.path import isfile, join
import disnake
from disnake.ext import commands
import asyncio
import pytz
from datetime import datetime

bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
  print('Bot is working...')
  bot.loop.create_task(status_task())

@bot.event
async def status_task():
  activity1 = disnake.Activity(type=disnake.ActivityType.watching, name="auf Pubg Mobile DE")
  await bot.change_presence(status=disnake.Status.idle, activity=activity1)


if __name__ == '__main__':
  path = 'extensions'
  extensions = [file for file in listdir(path) if isfile(join(path, file))]
  for extension in extensions:
    try:
      bot.load_extension(f'{path}.{extension[:-3]}')
      print("Geladene Extension:", extension)
    except Exception as exeption:
      print(f'Fehler in Abfragen: {extension}')



bot.run('OTMxMjEyMzUxNTczNzQ1Njc0.YeBJFQ.05EiLSpQ9ogAi36npfZkvm15V2I')
