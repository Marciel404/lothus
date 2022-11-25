import discord, hexacolors
from discord import Interaction
from discord.ui import View, Select
from funcs.defs import *

class buttonkick(View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmkick(self, button: discord.Button, interaction: Interaction):

        t = translates(interaction.guild)

        if interaction.user.id == self.ctx.id:

            try:

                e = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}', ephemeral = True)

                await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                channel = self.bot.get_channel(mod.find_one({'_id': interaction.guild.id})['lmod']['id'])

                try:

                    w = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                    dbmoderation.logs('lmod',True,interaction.guild,mod.find_one({'_id': interaction.guild.id})['lmod']['id'], webhook.id)

                    w = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                    await w.send(embed = e)

                self.stop()

            except:

                e = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                await interaction.channel.send(embed = e)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denykick(self, button: discord.ui.Button, interaction: discord.Interaction):

        t = translates(interaction.guild)

        if interaction.user.id == self.ctx.id:

            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

class buttonban(View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmban(self, button: discord.Button, interaction: Interaction):

        t = translates(interaction.guild)

        if interaction.user.id == self.ctx.id:

            try:

                e = discord.Embed(title = 'Ban', description =  t["args"]["mod"]["logban"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}', ephemeral = True)

                await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                channel = self.bot.get_channel(mod.find_one({'_id': interaction.guild.id})['lmod']['id'])

                try:

                    w = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                    dbmoderation.logs('lmod',True,interaction.guild,mod.find_one({'_id': interaction.guild.id})['lmod']['id'], webhook.id)

                    w = await self.bot.fetch_webhook(mod.find_one({'_id': interaction.guild.id})['lmod']['webhook'])

                    await w.send(embed = e)

                self.stop()

            except:

                E = discord.Embed(title = 'Ban', description = t["args"]["mod"]["logban"].format(self.membro.name, self.ctx.mention,self.motivo,self.membro.id))

                await interaction.channel.send(embed = E)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        t = translates(interaction.guild)

        if interaction.user.id == self.ctx.id:

            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

class selecthelp(Select):

    def __init__(self, bot, ctx, t):

        self.bot = bot

        self.ctx = ctx

        self.t = t

        super().__init__(
        placeholder = t['help']['extras']['commands'],
        options = [
            discord.SelectOption(
                label =  t['help']['mod']['name1'],
                description =  t['help']['mod']['name2'],
                value = '0'
            ),
            discord.SelectOption(
                label =  t['help']['general']['name'],
                description =  t['help']['general']['description'],
                value = '1'
            ),
            discord.SelectOption(
                label = t['help']['economy']['name'],
                description = t['help']['general']['description'],
                value = '2'
            ),
            discord.SelectOption(
                label = t['help']['suport']['name'],
                description = t['help']['suport']['description'],
                value = '3'
            ),
            discord.SelectOption(
                label = t['help']['image']['name'],
                description = t['help']['image']['description'],
                value = '4'
            ),
            discord.SelectOption(
                label = t['help']['actions']['name'],
                description = t['help']['actions']['description'],
                value = '5'
            )
        ]
    )
    async def callback(self, interaction: discord.Interaction):

        if interaction.user.id == self.ctx.id:

            if self.values[0] == '0':

                m = discord.Embed(title = self.t['help']['extras']['commands'],
                description = self.t['help']['mod']['description'],
                color = hexacolors.string('indigo'))

                m.add_field(
                    name = self.t['help']['mod']['name1'],
                    value = self.t['help']['mod']['content'],
                    inline = False)
                m.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed = m)

            elif self.values[0] == '1':

                g = discord.Embed(title = self.t['help']['extras']['commands'],
                color = hexacolors.string('indigo'))

                g.add_field(
                    name = self.t['help']['general']['description'],
                    value = self.t['help']['general']['content'],
                    inline = False)
                g.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=g)

            elif self.values[0] == '2':

                e = discord.Embed(title = self.t['help']['extras']['commands'],
                color = hexacolors.string('indigo'))

                e.add_field(
                    name = self.t['help']['economy']['description'], 
                    value = self.t['help']['economy']['content'],
                    inline = False)
                e.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=e)

            elif self.values[0] == '3':

                s = discord.Embed(title = self.t['help']['extras']['commands'],
                color = hexacolors.string('indigo'))

                s.add_field(
                    name = self.t['help']['suport']['description'], 
                    value = self.t['help']['suport']['content'],
                    inline = False)
                s.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=s)

            elif self.values[0] == '4':

                i = discord.Embed(title = self.t['help']['extras']['commands'],
                color = hexacolors.string('indigo'))

                i.add_field(
                    name= self.t['help']['image']['description'], 
                    value = self.t['help']['image']['content'],
                    inline = False)
                i.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=i)
            
            elif self.values[0] == '5':

                a = discord.Embed(title = self.t['help']['extras']['commands'],
                color = hexacolors.string('indigo'))

                a.add_field(
                    name= self.t['help']['actions']['description'], 
                    value = self.t['help']['actions']['content'],
                    inline = False)
                a.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=a)

class setlang(Select):

    def __init__(self, bot, ctx, t):

        self.bot = bot

        self.ctx = ctx

        self.t = t

        super().__init__(
        placeholder= t['args']['lang']['lang'],
        options = [
            discord.SelectOption(
                label = 'pt-BR',
                description = t['args']['lang']['ptbr'],
                value = 'pt-br'
            ),
            discord.SelectOption(
                label = 'en-US',
                description = t['args']['lang']['eng'],
                value = 'en-us'
            ),
            discord.SelectOption(
                label = 'fr-FR',
                description = t['args']['lang']['fr'],
                value = 'fr-fr'
            ),
            discord.SelectOption(
                label = 'es-ES',
                description = t['args']['lang']['es'],
                value = 'es-es'
            )
        ])
    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == 'pt-br':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                return

            dbmoderation.lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('Okay, agora falarei português', ephemeral = True)

        if self.values[0] == 'en-us':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                return

            dbmoderation.lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('ok now i will speak english', ephemeral = True)

        if self.values[0] == 'fr-fr':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                return

            dbmoderation.lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('Bon, maintenant je vais parler français', ephemeral = True)

        if self.values[0] == 'es-es':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(self.t['args']['lang']['langequal'], ephemeral = True)

                return

            dbmoderation.lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('Bien, ahora hablaré español.', ephemeral = True)

class actvate(Select):

    def __init__(self, bot, ctx, guild, log):

        self.bot = bot

        self.ctx = ctx

        self.log = log

        t = translates(guild)

        super().__init__(

            placeholder= t['args']['mod'][log],
            
            options = [

                discord.SelectOption(

                    label = t['args']['act'],
                    value = 'ativar'

                ),

                discord.SelectOption(

                    label = t['args']['dsb'],
                    value = 'desativar'

                ),

            ]
        )
    async def callback(self, interaction: discord.Interaction):

        t = translates(interaction.guild)

        db = mod.find_one({'_id': interaction.guild.id})

        if self.values[0] == 'ativar':

            await interaction.response.send_message(t['args']['sendid'], ephemeral = True)

            def check50(m):
                
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            id = interaction.guild.get_channel(int(msg50.content))

            await msg50.delete()

            await interaction.channel.send(t['args']['sucessdef'], delete_after = 3)

            try:

                if db[self.log]['webhook'] != None:

                    w = await self.bot.fetch_webhook(db[self.log]['webhook'])

                    await w.edit(channel = id)

                    dbmoderation.logs(self.log,True,interaction.guild,id.id, db[self.log]['webhook'])
            
            except:

                webhook = await id.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                dbmoderation.logs(self.log,True,interaction.guild,id.id, webhook.id)     
        
        if self.values[0] == 'desativar':

            await interaction.response.send_message(t['args']['undef'], ephemeral = True)

            dbmoderation.logs(self.log,False,interaction.guild,None,None)

class setlog(Select):

    def __init__(self, bot, ctx, t):

        self.bot = bot

        self.ctx = ctx

        self.t = t

        super().__init__(
            placeholder= t['args']['mod']['log'],

            options = [

                discord.SelectOption(

                    label = 'Mod',
                    description = t['args']['mod']['lmod'],
                    value = 'mod'

                ),

                discord.SelectOption(

                    label = 'Vc',
                    description = t['args']['mod']['lvoice'],
                    value = 'voice'

                ),

                discord.SelectOption(

                    label = 'Txt',
                    description = t['args']['mod']['ltxt'],
                    value = 'txt'

                ),
                discord.SelectOption(

                    label = 'Mic',
                    description = t['args']['mod']['lmic'],
                    value = 'mic'

                ),

            ]
        )
    async def callback(self, interaction : discord.Interaction):

        if self.values[0] == 'mod':
            await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lmod')), ephemeral = True)
        if self.values[0] == 'voice':
            await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lvoice')), ephemeral = True)
        if self.values[0] == 'txt':
            await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'ltxt')), ephemeral = True)
        if self.values[0] == 'mic':
            await interaction.response.send_message(view = discord.ui.View(actvate(self.bot, interaction.user,interaction.guild,'lmic')), ephemeral = True)