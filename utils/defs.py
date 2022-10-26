from db.members import *
from db.moderation import *
from translate.ptBR import *
from translate.enUS import *
from translate.frFR import *
from translate.esES import *

def better_time(cd: int):

    time = f"{cd} s"

    if cd > 60:

        minutes = cd - (cd % 60)

        seconds = cd - minutes

        minutes = int(minutes / 60)

        time = f"{minutes}min {seconds}s"

        if minutes > 60:

            hoursglad = minutes - (minutes % 60)

            hours = int(hoursglad / 60)

            minutes = minutes - (hours*60)

            time = f"{hours}h {minutes}min {seconds}s"

    return time

async def translate(guild):

    if mod.find_one({'_id': guild.id})['lang'] == 'pt-br':

        lang = ptBR

    if mod.find_one({'_id': guild.id})['lang'] == 'en-us':

        lang = enUS
    
    if mod.find_one({'_id': guild.id})['lang'] == 'fr-fr':

        lang = frFR

    if mod.find_one({'_id': guild.id})['lang'] == 'es-es':

        lang = esES

    return lang

def translates(guild):

    if mod.find_one({'_id': guild.id})['lang'] == 'pt-br':

        lang = ptBR

    if mod.find_one({'_id': guild.id})['lang'] == 'en-us':

        lang = enUS
    
    if mod.find_one({'_id': guild.id})['lang'] == 'fr-fr':

        lang = frFR

    if mod.find_one({'_id': guild.id})['lang'] == 'es-es':

        lang = esES

    return lang