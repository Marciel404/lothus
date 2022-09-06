import discord,os

from discord.ext import commands
from .configs import configData

class loadcogs():

    def __init__(self, bot):

        self.bot = bot

        pass

    def load(self):

        for filename in os.listdir('./plugins'):

            if filename.endswith('.py'):

                self.bot.load_extension('plugins.{0}'.format(filename[:-3]))

        for filename in os.listdir('./commands'):

            if filename.endswith('.py'):

                self.bot.load_extension('commands.{0}'.format(filename[:-3]))

class Client(commands.Bot):

    def __init__(self, token):

        self.token = token
        
        super().__init__(

            command_prefix = configData['prefix'],

            help_command = None,

            intents = discord.Intents.all(),

            case_insensitive = True
        )

    async def on_connect(self):

        await self.change_presence(activity=discord.Game(name="/help"))

        print(f'Eu estou online como {self.user}')

        print(discord.__version__)

    def __run__(self):

        loadcogs(self).load()

        self.run(self.token)