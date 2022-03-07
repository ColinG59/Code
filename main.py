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
    #de = pytz.timezone('Europe/Berlin')
    #zeit = datetime.now().astimezone(tz=de).strftime("%d.%m.%Y - %H:%M Uhr")
  activity1 = disnake.Activity(type=disnake.ActivityType.watching, name="auf Pubg Mobile DE")
  await bot.change_presence(status=disnake.Status.idle, activity=activity1)
    #await bot.change_presence(activity=disnake.Game("Befehlsübersicht: ?cmds"))
    #await asyncio.sleep(5)
   # await bot.change_presence(activity=disnake.Game(zeit))
   # await asyncio.sleep(5)


 


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
#STOP Nur Kommentare ab hier!
#-----------------------------------------------------------------------------------------------------------------------------------------------

#__KOPIERHILFEN__

#Embed.add_field(name='', value=f'', inline=False)
#Nachricht in einen anderen Kanal senden--
#applychannel = bot.get_channel(782935710130241557)
#await applychannel.send(f'> <@{ctx.author.id}> hat ein Bewerbungsschreiben Angefordert')
#ZEIT---
#strftime("%d.%m.%Y - %H:%M Uhr")
#botstatus
#await asyncio.sleep(4)
#await  bot.change_presence(activity=discord.Game('Der FEARLESS Bot'))
#AKTIVITÄTSSTATUS
#async def status_task():
#	while True:

	#	await bot.change_presence(activity=discord.Game('Der FEARLESS Bot'))
    #await asyncio.sleep(4)
    #wait bot.change_presence(activity=discord.Game(''))
    #await bot.change_presence(activity=discord.Streaming('Mogli_Pubg', url='https://www.twitch.tv/mogli_pubg'))


#Custom Emoji= <:emoji_name:emoji_id>