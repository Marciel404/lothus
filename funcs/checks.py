import requests

from discord.ext import commands
from db.moderation import *
from funcs.defs import translates
from main import configData

class NoVote(commands.CheckFailure):
    pass

def vote():

    async def check(ctx):

        t = translates(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 0:
            raise NoVote(t['args']['notvote'])
        
        return True

    return commands.check(check)