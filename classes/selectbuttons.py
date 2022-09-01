import discord
from discord import Interaction
from discord.ui import View, Select
from utils.defs import *

class buttonkick(View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmkick(self, button: discord.Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.ctx.id:

            try:
        
                l1 = self.bot.get_channel(mod.find_one({"_id": interaction.guild.id})['lmod']['id'])

                E = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.ctx.mention,self.motivo,self.membro.id))

                await l1.send(embed = E)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}', ephemeral = True)

                await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                self.stop()

            except:

                E = discord.Embed(title = 'kick', description = t["args"]["mod"]["logkick"].format(self.ctx.mention,self.motivo,self.membro.id))

                await l1.send(embed = E)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["kicksucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                await interaction.guild.kick(user = self.membro ,reason = self.motivo)

                self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        t = await translate(interaction.guild)

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
    async def confirmkick(self, button: discord.Button, interaction: Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.ctx.id:

            try:
        
                l1 = self.bot.get_channel(int(mod.find_one({"_id": interaction.guild.id})['lmod']['id']))

                E = discord.Embed(title = 'Ban', description =  t["args"]["mod"]["logban"].format(self.ctx.mention,self.motivo,self.membro.id))

                await l1.send(embed = E)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}', ephemeral = True)

                await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                self.stop()

            except:

                E = discord.Embed(title = 'Ban', description = t["args"]["mod"]["logban"].format(self.ctx.mention,self.motivo,self.membro.id))

                await l1.send(embed = E)

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} {t["args"]["mod"]["bansucess"]}\n{t["args"]["mod"]["lognotfound"]}', ephemeral = True)

                await interaction.guild.ban(user = self.membro ,reason = self.motivo)

                self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denykick(self, button: discord.ui.Button, interaction: discord.Interaction):

        t = await translate(interaction.guild)

        if interaction.user.id == self.ctx.id:

            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message(f'{t["args"]["mod"]["notpermission"]}', ephemeral = True)

class selecthelp(Select):

    def __init__(self, bot, ctx, guild):

        self.bot = bot

        self.ctx = ctx

        t = translates(guild)

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

            t = await translate(interaction.guild)

            if self.values[0] == '0':

                m = discord.Embed(title = t['help']['extras']['commands'],
                description = t['help']['mod']['description'],
                color = 000000)

                m.add_field(
                    name = t['help']['mod']['name1'],
                    value = t['help']['mod']['content'],
                    inline = False)
                m.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed = m)

            elif self.values[0] == '1':

                g = discord.Embed(title = t['help']['extras']['commands'],
                color = 000000)

                g.add_field(
                    name = t['help']['general']['description'],
                    value = t['help']['general']['content'],
                    inline = False)
                g.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=g)

            elif self.values[0] == '2':

                e = discord.Embed(title = t['help']['extras']['commands'],
                color = 000000)

                e.add_field(
                    name = t['help']['economy']['description'], 
                    value = t['help']['economy']['content'],
                    inline = False)
                e.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=e)

            elif self.values[0] == '3':

                s = discord.Embed(title = t['help']['extras']['commands'],
                color = 000000)

                s.add_field(
                    name = t['help']['suport']['description'], 
                    value = t['help']['suport']['content'],
                    inline = False)
                s.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=s)

            elif self.values[0] == '4':

                i = discord.Embed(title = t['help']['extras']['commands'],
                color = 000000)

                i.add_field(
                    name= t['help']['image']['description'], 
                    value = t['help']['image']['content'],
                    inline = False)
                i.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=i)
            
            elif self.values[0] == '5':

                a = discord.Embed(title = t['help']['extras']['commands'],
                color = 000000)

                a.add_field(
                    name= t['help']['actions']['description'], 
                    value = t['help']['actions']['content'],
                    inline = False)
                a.set_thumbnail(url = f'{self.bot.user.avatar}')

                await interaction.response.edit_message(embed=a)

class setlang(Select):

    def __init__(self, bot, ctx, guild):

        self.bot = bot

        self.ctx = ctx

        t = translates(guild)

        super().__init__(
        placeholder= t['args']['lang']['lang'],
        options = [
            discord.SelectOption(
                label = 'pt-br',
                description = t['args']['lang']['ptbr'],
            ),
            discord.SelectOption(
                label = 'en-us',
                description = t['args']['lang']['eng']
            )
        ])
    async def callback(self, interaction : discord.Interaction):

        t = await translate(interaction.guild)

        if self.values[0] == 'pt-br':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(t['args']['lang']['langequal'], ephemeral = True)

                return

            await lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('Okay, agora falarei português', ephemeral = True)

        if self.values[0] == 'en-us':

            if self.values[0] == mod.find_one({'_id':interaction.guild.id})['lang']:

                await interaction.response.send_message(t['args']['lang']['langequal'], ephemeral = True)

                return

            await lang('lang',self.values[0],interaction.guild)

            await interaction.response.send_message('ok now i will speak english', ephemeral = True)

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
    async def callback(self, interaction : discord.Interaction):

        t = await translate(interaction.guild)

        if self.values[0] == 'ativar':

            await interaction.response.send_message(t['args']['sendid'], ephemeral = True)

            def check50(m):
                
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            id = interaction.guild.get_channel(int(msg50.content))

            await msg50.delete()

            await interaction.channel.send(t['args']['sucessdef'], delete_after = 3)

            await logs(self.log,True,interaction.guild,id.id)
        
        if self.values[0] == 'desativar':

            await interaction.response.send_message(t['args']['undef'], ephemeral = True)

            await logs(self.log,False,interaction.guild,None)

class setlog(Select):

    def __init__(self, bot, ctx, guild):

        self.bot = bot

        self.ctx = ctx

        t = translates(guild)

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

                    label = 'txt',
                    description = t['args']['mod']['ltxt'],
                    value = 'txt'

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