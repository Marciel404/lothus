import discord,os

from discord.ext.commands import Bot as BotBase
from .configs import configData

class loadcogs():

    def __init__(self, bot):

        self.bot = bot

    def __loader__(self):

        for filename in os.listdir('./plugins'):

            if filename.endswith(".py"):

                self.bot.load_extension('plugins.{0}'.format(filename[:-3]))

        for filename in os.listdir('./commands'):

            if filename.endswith(".py"):

                self.bot.load_extension('commands.{0}'.format(filename[:-3]))

class client(BotBase):

    def __init__(self, token):

        self.token = token
        
        super().__init__(command_prefix = configData['prefix'],  intents = discord.Intents.all())

    async def on_connect(self):
        
        await self.change_presence(activity=discord.Game(name="/help"))

        print(f'Eu estou online como {self.user}')

        print(discord.__version__)

    def __run__(self):

        loadcogs(self).__loader__()

        self.run(self.token)
