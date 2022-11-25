import discord, requests,hexacolors

from discord import Interaction, ButtonStyle
from discord.ui import button,Button, View
from .inputText import perfil
from db.economy import *
from funcs.defs import translates

class changeavatar(discord.ui.View):

    def __init__(self, membro):

        self.member = membro

        super().__init__(timeout = 180, disable_on_timeout = True)

    @discord.ui.button(label = 'User Avatar',style = discord.ButtonStyle.blurple)
    async def useravatar(self, button: discord.ui.Button, interaction: discord.Interaction):

        membro = self.member
        t = translates(interaction.guild)
        embed = discord.Embed(title = f'Avatar {membro}', 
        description = f'[{t["args"]["avatar"]["click1"]}]({membro.avatar}) {t["args"]["avatar"]["click2"]}')
        embed.set_image(url = f'{membro.avatar}')
        await interaction.response.edit_message(embed = embed, View = guildavatar(membro))

class guildavatar(discord.ui.View):

    def __init__(self, membro):

        self.member = membro

        super().__init__(timeout = 180, disable_on_timeout = True)

    @discord.ui.button(label = 'User Avatar',style = discord.ButtonStyle.blurple)
    async def useravatar(self, button: discord.ui.Button, interaction: discord.Interaction):

        membro = self.member
        t = translates(interaction.guild)
        embed = discord.Embed(title = f'Avatar {membro}', 
        description = f'[{t["args"]["avatar"]["click1"]}]({membro.guild_avatar}) {t["args"]["avatar"]["click2"]}')
        embed.set_image(url = f'{membro.guild_avatar}')
        await interaction.response.edit_message(embed = embed, View = changeavatar(membro))

class profile(View):
    
    def __init__(self,ctx):

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = 'Edit', style = ButtonStyle.blurple)
    async def perfil(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.ctx.id:
            await interaction.response.send_modal(perfil(interaction.user))

class kisses(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def kiss(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=kiss&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["kiss"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionkiss"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()

class huges(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def abraço(self, button: Button, interaction: Interaction):

        try:
            if interaction.user.id == self.membro.id:
                t = translates(interaction.guild)
                r = requests.get(
                'https://api.otakugifs.xyz/gif?reaction=hug&format=gif')
                res = r.json()
                kiss2 = discord.Embed(title = t["args"]["actions"]["hug"],
                description = f'<@{self.membro.id}> {t["args"]["actions"]["actionhug"]} <@{self.ctx.id}>',
                color = hexacolors.string('indigo'))
                kiss2.set_image(url = res['url'])
                await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
                self.stop()
        except Exception as error:
            print(error)

class slaps(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def tapa(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=slap&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["slap"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionslap"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()

class punches(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def soco(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=punch&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["punch"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionpunch"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()

class bites(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def moder(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=bite&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["bite"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionbite"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()

class cafunes(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def cafune(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=pat&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["pat"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionpat"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()

class lickes(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def lambida(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:
            t = translates(interaction.guild)
            r = requests.get(
            'https://api.otakugifs.xyz/gif?reaction=lick&format=gif')
            res = r.json()
            kiss2 = discord.Embed(title = t["args"]["actions"]["lick"],
            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionlick"]} <@{self.ctx.id}>',
            color = hexacolors.string('indigo'))
            kiss2.set_image(url = res['url'])
            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)
            self.stop()