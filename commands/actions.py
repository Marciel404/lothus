import discord, requests, random, aiohttp

from discord.ext import commands
from discord import slash_command, option
from utils.defs import *
from classes.buttons import *

class actions(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'flip_coin', description = 'Joga uma moeda de cara ou coroa')
    async def flipcoin(self, ctx):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        c = random.choice([1,2])

        if c == 1:

            await ctx.respond(t['args']['actions']['flip1'])

        elif c == 2:

            await ctx.respond(t['args']['actions']['flip2'])

    @slash_command(name = 'hug', description = 'hug one member')
    @option(name = 'member', description = 'Select one member')
    async def hug(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        r = requests.get(

        'https://api.otakugifs.xyz/gif?reaction=hug&format=gif')

        res = r.json()
        
        kiss = discord.Embed(title = t["args"]["actions"]["hug"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionhug"]} <@{member.id}>')

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.respond(content = f'{member.mention}',embed = kiss, view = huges(member,ctx.author))

    @slash_command(name = 'kiss', description = 'kiss one member')
    @option(name = 'member', description = 'Select one member')
    async def kiss(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        if member == self.bot.user:

            await ctx.respond(f'{t["args"]["actions"]["notkiss"]}')

        else:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=kiss&format=gif')

            res = r.json()

            kiss = discord.Embed(title = t["args"]["actions"]["kiss"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionkiss"]} <@{member.id}>')

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.respond(content = f'{member.mention}',embed = kiss, view = kisses(member,ctx.author))

    @slash_command(name = 'slap', description = 'Slap one member')
    @option(name = 'member', description = 'Select one member')
    async def slap(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        r = requests.get(

        'https://api.otakugifs.xyz/gif?reaction=slap&format=gif')

        res = r.json()
        
        if member == self.bot.user:

            kiss = discord.Embed(title = t["args"]["actions"]["slap"],

            description = f'<@{member.id}> {t["args"]["actions"]["actionslap"]} <@{ctx.author.id}>')

            kiss.set_image(url = res['url'])

            await ctx.respond(embed = kiss)

        else:

            kiss = discord.Embed(title = t["args"]["actions"]["pat"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpat"]} <@{member.id}>')

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.respond(content = f'{member.mention}',embed = kiss, view = slaps(member,ctx.author))

    @slash_command(name = 'punch', description = 'Punch one member')
    @option(name = 'member', description = 'Select one member')
    async def punch(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=punch&format=gif')

        res = r.json()

        if member == self.bot.user:

            kiss = discord.Embed(title = t["args"]["actions"]["punch"],

            description = f'<@{member.id}> {t["args"]["actions"]["actionpunch"]} <@{ctx.author.id}>')

            kiss.set_image(url = res['url'])

            await ctx.respond(embed = kiss)

        else:

            kiss = discord.Embed(title = t["args"]["actions"]["punch"],

            description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpunch"]} <@{member.id}>')

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

            await ctx.respond(content = f'{member.mention}',embed = kiss, view = punches(member,ctx.author))

    @slash_command(name = 'bite', description = 'Bite one member')
    @option(name = 'member', description = 'Select one member')
    async def bite(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=bite&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["bite"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionbite"]} <@{member.id}>')

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.respond(content = f'{member.mention}',embed = kiss, view = bites(member,ctx.author))

    @slash_command(name = 'lick', description = 'Lick a member')
    @option(name = 'member', description = 'Mention member')
    async def lick(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=lick&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["lick"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionlick"]} <@{member.id}>')

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.respond(content = f'{member.mention}',embed = kiss, view = lickes(member,ctx.author))

    @slash_command(name = 'cafune', description = 'Faz um cafune em alguem')
    @option(name = 'member', description = 'Mencione um member')
    async def pat(self, ctx, member: discord.Member):

        if ctx.guild == None:

            return

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=pat&format=gif')

        res = r.json()

        kiss = discord.Embed(title = t["args"]["actions"]["pat"],

        description = f'<@{ctx.author.id}> {t["args"]["actions"]["actionpat"]} <@{member.id}>')

        kiss.set_image(url = res['url'])

        kiss.set_footer(text = f'{t["args"]["actions"]["return"]}')

        await ctx.respond(content = f'{member.mention}',embed = kiss, view = cafunes(member,ctx.author))

def setup(bot:commands.Bot):
    bot.add_cog(actions(bot))