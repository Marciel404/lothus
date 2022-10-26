import discord, requests, asyncio

from discord import Interaction, ButtonStyle
from discord.ui import button,Button, View
from .inputText import perfil
from db.economy import *
from utils.defs import translate

class adonticket2(discord.ui.View):

    def __init__(self, membro):

        self.membro = membro

        super().__init__(timeout = None)

    @discord.ui.button(label = '🔓 Abrir ticket', style = discord.ButtonStyle.blurple)
    async def abrir(self,  button: discord.ui.Button, interaction: discord.Interaction):

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

        suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=True),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            suporte: discord.PermissionOverwrite(read_messages=True),

        }

        await interaction.channel.edit(overwrites = overwrites)

        await interaction.message.delete()

        await interaction.channel.send('Ticket aberto 🔓', view = adonticket(self.membro))

    @discord.ui.button(label = '🛑 Deletar Ticket', style = discord.ButtonStyle.blurple)
    async def delete(self,  button: discord.ui.Button, interaction: discord.Interaction):

        await interaction.response.send_message('O ticket sera deletado em segundos')

        await asyncio.sleep(5)

        await interaction.channel.delete()

class adonticket(discord.ui.View):
    
    def __init__(self, membro):

        self.membro = membro

        super().__init__(timeout = None)

    @discord.ui.button(label = '🔒 Fechar ticket', style = discord.ButtonStyle.blurple)
    async def close(self,  button: discord.ui.Button, interaction: discord.Interaction):

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

        suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=False),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            suporte: discord.PermissionOverwrite(read_messages=True),

        }

        e = discord.Embed(description = f'🔒Ticket fechado por {interaction.user.mention} \nClique no 🔓 para abrir')

        await interaction.channel.edit(overwrites = overwrites)
        await interaction.message.delete()
        await interaction.channel.send(embed = e, view = adonticket2(member))

        self.stop()

class ticket(discord.ui.View):
    
    def __init__(self):

        super().__init__(timeout = None)
        
    @discord.ui.button(label = '📩 Criar ticket', style = discord.ButtonStyle.blurple)
    async def confirm(self,  button: discord.ui.Button, interaction: discord.Interaction):

        guild = interaction.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{interaction.user.id}')

        if Chat is None:

            ticket = f'ticket-{interaction.user.id}'

            member = interaction.user

            admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

            overwrites = {

                guild.default_role: discord.PermissionOverwrite(read_messages = False),

                member: discord.PermissionOverwrite(read_messages = True),

                admin: discord.PermissionOverwrite(read_messages = True),

                mod: discord.PermissionOverwrite(read_messages = True),

                suporte: discord.PermissionOverwrite(read_messages = True),

                }

            channel = await guild.create_text_channel(name=ticket, 
            overwrites = overwrites, 
            category = discord.utils.get(interaction.guild.categories, id = configData['catego']['ticket']))

            await interaction.response.send_message('Ticket criado com sucesso', ephemeral = True)

            await channel.send(view=adonticket(member))

            await channel.send(f'{interaction.user.mention} {suporte.mention}')
        
        else:

            await interaction.response.send_message('Ticket já existente, encerre o ultimo para criar outro', ephemeral = True)

class profile(View):
    
    def __init__(self,ctx):

        self.ctx = ctx

        super().__init__(timeout = 300)

    @button(label = 'Edit', style = ButtonStyle.blurple)
    async def ausente(self, button: Button, interaction: Interaction):

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

            t = await translate(interaction.guild)

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
    async def abraço(self, button: Button, interaction: Interaction):

        try:

            if interaction.user.id == self.membro.id:

                t = await translate(interaction.guild)

                r = requests.get(

                'https://api.otakugifs.xyz/gif?reaction=hug&format=gif')

                res = r.json()

                kiss2 = discord.Embed(title = t["args"]["actions"]["hug"],

                description = f'<@{self.membro.id}> {t["args"]["actions"]["actionhug"]} <@{self.ctx.id}>')

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
    async def ausente(self, button: Button, interaction: Interaction):

        if interaction.user.id == self.membro.id:

            t = await translate(interaction.guild)

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

        if interaction.user.id == self.membro.id:

            t = await translate(interaction.guild)

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

        if interaction.user.id == self.membro.id:

            t = await translate(interaction.guild)

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

        if interaction.user.id == self.membro.id:

            t = await translate(interaction.guild)

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

        if interaction.user.id == self.membro.id:

            t = await translate(interaction.guild)

            r = requests.get(

            'https://api.otakugifs.xyz/gif?reaction=lick&format=gif')

            res = r.json()

            kiss2 = discord.Embed(title = t["args"]["actions"]["lick"],

            description = f'<@{self.membro.id}> {t["args"]["actions"]["actionlick"]} <@{self.ctx.id}>')

            kiss2.set_image(url = res['url'])

            await interaction.response.send_message(content = f'{self.ctx.mention}',embed = kiss2)

            self.stop()