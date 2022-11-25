from db.members import *
from db.moderation import *
from json import load

with open('translate/enUS.json', encoding = 'utf-8') as f:
    enUS = load(f)
with open('translate/ptBR.json', encoding = 'utf-8') as f:
    ptBR = load(f)
with open('translate/esES.json', encoding = 'utf-8') as f:
    esES = load(f)
with open('translate/frFR.json', encoding = 'utf-8') as f:
    frFR = load(f)

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

def translates(guild):

    try:
        if mod.find_one({'_id': guild.id})['lang'] == 'pt-br':
            lang = ptBR

        if mod.find_one({'_id': guild.id})['lang'] == 'en-us':
            lang = enUS
        
        if mod.find_one({'_id': guild.id})['lang'] == 'fr-fr':
            lang = frFR

        if mod.find_one({'_id': guild.id})['lang'] == 'es-es':
            lang = esES

        return lang

    except:
        dbmoderation.lang('lang', 'en-us', guild)