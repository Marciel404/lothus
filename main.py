import discord,os, json
from discord.ext.commands import Bot as BotBase

with open("config.json", 'r') as f:
    configData = json.load(f)

__title__ = "LothusBot"
__author__ = "Marciel404"
__license__ = "MIT"
__copyright__ = "Copyright 2022-present Marciel404"
__version__ = "3.5.0"

client = BotBase(command_prefix = '!',help_command=None,intents=discord.Intents.all(),case_insensitive = True)

pastaname = 'cogs'
for filename in os.listdir(f'./{pastaname}'):
    for commands in os.listdir(f'./{pastaname}/{filename}'):
        if commands.endswith('.py') and not commands.startswith('__'):
            client.load_extensions(f'{pastaname}.{filename}.{commands[:-3]}')

client.run(configData['token'])