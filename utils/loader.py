import discord,os
from discord import Bot as BotBase

__title__ = "LothusBot"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "Copyright 2022-present Marciel404"
__version__ = "3.0.0"

class loadcogs():

    def __init__(self, bot):
        
        self.bot = bot

    def load(self):

        for filename in os.listdir('./plugins'):

            if filename.endswith(".py"):

                self.bot.load_extension('plugins.{0}'.format(filename[:-3]))

        for filename in os.listdir('./commands'):
            
            if filename.endswith(".py"):

                self.bot.load_extension('commands.{0}'.format(filename[:-3]))

class client(BotBase):

    def __init__(self, token):

        self.token = token

        super().__init__(

            help_command=None,

            intents=discord.Intents.all(),
        )

    async def on_ready(self):
        
        await self.change_presence(activity=discord.Game(name="/help"))

        print(f'Eu estou online como {self.user}')

        print(__version__)

    def __run__(self):

        loadcogs(self).load()

        self.run(self.token)
