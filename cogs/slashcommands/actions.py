import discord
import requests
import random

from discord.ext import commands
from discord import slash_command, option
from funcs.defs import *
from classes.buttons import *

class actions(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(
        name = 'flip_coin', 
        description = 'Flip a coin', 
        guild_only = True,
        name_localizations = {
            'en-US': 'flip_coin',
            'en-GB': 'flip_coin',
            'es-ES': 'tirar_la_moneda',
            'pt-BR': 'girar_moeda',
            'fr': 'pièce_de_monnaie'
        },
        description_localizations = {
            'en-US': 'Play heads or tails',
            'en-GB': 'Play heads or tails',
            'es-ES': 'Juega cara o cruz',
            'pt-BR': 'Joga cara ou coroa',
            'fr': 'Jouer à pile ou face'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    async def flipcoin(self, ctx):

        t = translates(ctx.guild)

        c = random.choice([1,2])

        if c == 1:

            await ctx.response.send_message(t['args']['actions']['flip1'])

        elif c == 2:

            await ctx.response.send_message(t['args']['actions']['flip2'])

    @slash_command(
        name = 'hug',
        description = 'hug one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'hug',
            'en-GB': 'hug',
            'es-ES': 'abrazo',
            'pt-BR': 'abraço',
            'fr': 'câliner'
        },
        description_localizations = {
            'en-US': 'Hug a member',
            'en-GB': 'Hug a member',
            'es-ES': 'Abrazar a un miembro',
            'pt-BR': 'Abraça um membro',
            'fr': 'Embrasser un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def hug(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        r = requests.get(

        'https://api.otakugifs.xyz/gif?reaction=hug&format=gif')

        res = r.json()
        
        kiss = discord.Embed(title = t["args"]["actions"]["hug"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionhug"]} <@{member.id}>',
        color = hexacolors.string('indigo'))

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = huges(member,ctx.author))

    @slash_command(
        name = 'kiss',
        description = 'kiss one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'kiss',
            'en-GB': 'kiss',
            'es-ES': 'beso',
            'pt-BR': 'beijar',
            'fr': 'embrasser'
        },
        description_localizations = {
            'en-US': 'Kiss a member',
            'en-GB': 'Kiss a member',
            'es-ES': 'Beso a un miembro',
            'pt-BR': 'Beija um membro',
            'fr': 'Embrasser un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def kiss(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        if member == self.bot.user:

            await ctx.response.send_message(f'{t["args"]["actions"]["notkiss"]}')

        else:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=kiss&format=gif')

            res = r.json()

            kiss = discord.Embed(title = t["args"]["actions"]["kiss"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionkiss"]} <@{member.id}>',
            color = hexacolors.string('indigo'))

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = kisses(member,ctx.author))

    @slash_command(
        name = 'slap',
        description = 'Slap one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'slap',
            'en-GB': 'slap',
            'es-ES': 'bofetada',
            'pt-BR': 'tapa',
            'fr': 'gifler'
        },
        description_localizations = {
            'en-US': 'slap a member',
            'en-GB': 'slap a member',
            'es-ES': 'bofetada a un miembro',
            'pt-BR': 'Estapeia um membro',
            'fr': 'Gifler un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def slap(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        r = requests.get(

        'https://api.otakugifs.xyz/gif?reaction=slap&format=gif')

        res = r.json()
        
        if member == self.bot.user:

            kiss = discord.Embed(title = t["args"]["actions"]["slap"],

            description = f'<@{member.id}> {t["args"]["actions"]["actionslap"]} <@{ctx.author.id}>',
            
            color = hexacolors.string('indigo'))

            kiss.set_image(url = res['url'])

            await ctx.response.send_message(embed = kiss)

        else:

            kiss = discord.Embed(title = t["args"]["actions"]["pat"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpat"]} <@{member.id}>',
            color = hexacolors.string('indigo'))

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = slaps(member,ctx.author))

    @slash_command(
        name = 'punch',
        description = 'Punch one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'punch',
            'en-GB': 'punch',
            'es-ES': 'golpear',
            'pt-BR': 'soco',
            'fr': 'gifler'
        },
        description_localizations = {
            'en-US': 'Punch a member',
            'en-GB': 'Punch a member',
            'es-ES': 'Golpea a un miembro',
            'pt-BR': 'Soca um membro',
            'fr': 'Gifler un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def punch(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=punch&format=gif')

        res = r.json()

        if member == self.bot.user:

            kiss = discord.Embed(title = t["args"]["actions"]["punch"],

            description = f'<@{member.id}>{t["args"]["actions"]["actionpunch"]} <@{ctx.author.id}>',
            color = hexacolors.string('indigo'))

            kiss.set_image(url = res['url'])

            await ctx.response.send_message(embed = kiss)

        else:

            kiss = discord.Embed(title = t["args"]["actions"]["punch"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpunch"]} <@{member.id}>',
            color = hexacolors.string('indigo'))

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = punches(member,ctx.author))

    @slash_command(
        name = 'bite',
        description = 'Bite one member',
        guild_only = True,
        name_localizations = {
            'en-US': 'bite',
            'en-GB': 'bite',
            'es-ES': 'morder',
            'pt-BR': 'morder',
            'fr': 'mordre'
        },
        description_localizations = {
            'en-US': 'Bite a member',
            'en-GB': 'Bite a member',
            'es-ES': 'Morder a un miembro',
            'pt-BR': 'Morde um membro',
            'fr': 'Mordre un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Select one member')
    async def bite(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=bite&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["bite"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionbite"]} <@{member.id}>',
        color = hexacolors.string('indigo'))

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = bites(member,ctx.author))

    @slash_command(
        name = 'lick',
        description = 'Lick a member',
        guild_only = True,
        name_localizations = {
            'en-US': 'lick',
            'en-GB': 'lick',
            'es-ES': 'lamer',
            'pt-BR': 'lamber',
            'fr': 'lécher'
        },
        description_localizations = {
            'en-US': 'Lick a member',
            'en-GB': 'Lick a member',
            'es-ES': 'Lamer a un miembro',
            'pt-BR': 'Lambe um membro',
            'fr': 'Lécher un membre'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Mention member')
    async def lick(self, ctx: discord.Interaction, member: discord.Member):

        t = translates(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=lick&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["lick"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionlick"]} <@{member.id}>',
        color = hexacolors.string('indigo'))

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = lickes(member,ctx.author))

    @slash_command(name = 'cafune',description = 'Faz um cafune em alguem',guild_only = True)
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Mencione um member')
    async def pat(self, ctx: discord.Interaction, member: discord.Member):

        if ctx.guild == None:

            return

        t = translates(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=pat&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["pat"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpat"]} <@{member.id}>',
        color = hexacolors.string('indigo'))

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.response.send_message(content = f'{member.mention}',embed = kiss, view = cafunes(member,ctx.author))

def setup(bot:commands.Bot):
    bot.add_cog(actions(bot))