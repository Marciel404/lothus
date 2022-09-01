import discord,os
from discord.ext import commands
from .configs import configData

def __run__(token):

    client = commands.Bot(

    command_prefix = configData['prefix'],

    help_command = None,

    intents = discord.Intents.all(),

    case_insensitive = True)

    for filename in os.listdir('./plugins'):

        if filename.endswith('.py'):

            client.load_extension('plugins.{0}'.format(filename[:-3]))

    for filename in os.listdir('./commands'):

        if filename.endswith('.py'):

            client.load_extension('commands.{0}'.format(filename[:-3]))

    client.run(token)