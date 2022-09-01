import discord, requests

from discord import Interaction, ButtonStyle
from discord.ui import button,Button, View
from db.economy import *
from utils.defs import *

class kisses(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=kiss&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["kiss"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionkiss"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class huges(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=hug&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["hug"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionhug"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class slaps(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=slap&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["slap"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionslap"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class punches(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=punch&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["punch"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionpunch"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class bites(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=bite&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["bite"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionbite"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class cafunes(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=pat&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["pat"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionpat"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()

class lickes(View):
    
    def __init__(self, membro, ctx):

        self.membro = membro

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = '🔁', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.membro.id:

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=lick&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["lick"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionlick"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()