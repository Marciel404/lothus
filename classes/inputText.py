import discord

from discord.ui import InputText, Modal
from db.members import *
from funcs.defs import *

class perfil(Modal):

    def __init__(self, ctx) -> None:

        infos = perf.find_one({'_id': ctx.id})

        super().__init__(title = 'Profile')

        self.add_item(
            InputText(
                label = 'Idade',
                placeholder = 'Sua idade', 
                value = infos['r0']['value'],
                style = discord.InputTextStyle.singleline,
                min_length = 1,
                max_length = 2,
                required = False
            )
        ),
        self.add_item(
            InputText(
                label = 'Genero',
                placeholder = 'Seu genero',
                value = infos['r1']['value'],
                style = discord.InputTextStyle.singleline,
                required = False
            )
        ),
        self.add_item(
            InputText(
                label = 'País',
                placeholder = 'País que está morando',
                value = infos['r2']['value'],
                style = discord.InputTextStyle.singleline,
                required = False
            )
        ),
        self.add_item(
            InputText(
                label = 'Cidade',
                placeholder = 'Cidade onde mora',
                value = infos['r3']['value'],
                style = discord.InputTextStyle.singleline,
                required = False
            )
        ),
        self.add_item(
            InputText(
                label = 'Descrição',
                placeholder = 'Descrição do perfil',
                value = infos['r4']['value'],
                style = discord.InputTextStyle.paragraph,
                required = False
            )
        )
    async def callback(self, interaction: discord.Interaction):

        i = 0

        while True:

            if self.children[i].value == '':

                dbmember.upPerfil(interaction.user,f'r{i}',self.children[i].placeholder,None)
            
            else:

                dbmember.upPerfil(interaction.user,f'r{i}',self.children[i].placeholder,self.children[i].value)

            if i == 4:

                break

            else:

                i +=1
            
        i2 = 0

        embed = discord.Embed(title = 'Perfil')

        embed.set_thumbnail(url =interaction.user.display_avatar)

        while True:

            per = perf.find_one({'_id': interaction.user.id})

            if per[f'r{i2}']['value'] != None:

                embed.add_field(name = per[f'r{i2}']['name'], value = per[f'r{i2}']['value'])

            if per[f'r0']['value'] == None\
            and per[f'r1']['value'] == None\
            and per[f'r2']['value'] == None\
            and per[f'r3']['value'] == None\
            and per[f'r4']['value'] == None\
            and per[f'r5']['value'] == None:

                embed.add_field(name = 'error', value = 'Você não possue registro')

                break

            if i2 == 5:

                break

            else:

                i2 += 1

        await interaction.response.edit_message(embed = embed)