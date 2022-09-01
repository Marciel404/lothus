from db.moderation import *
from translate.ptbr import *
from translate.engus import *

def better_time(cd:int):

    time = f"{cd} s"

    if cd > 60:

        minutes = cd - (cd % 60)

        seconds = cd - minutes

        minutes = int(minutes/ 60)

        time = f"{minutes}min {seconds}s"

        if minutes > 60:

            hoursglad = minutes -(minutes % 60)

            hours = int(hoursglad/ 60)

            minutes = minutes - (hours*60)

            time = f"{hours}h {minutes}min {seconds}s"

    return time

async def translate(guild):

    if mod.find_one({'_id':guild.id})['lang'] == 'pt-br':

        lang = ptbr

    if mod.find_one({'_id':guild.id})['lang'] == 'en-us':

        lang = eng

    return lang

def translates(guild):

    if mod.find_one({'_id':guild.id})['lang'] == 'pt-br':

        lang = ptbr

    if mod.find_one({'_id':guild.id})['lang'] == 'en-us':

        lang = eng

    return lang