import discord
import requests
import hexacolors

from PIL import ImageDraw, ImageFont, Image
from io import BytesIO
from discord.ext import commands
from funcs.defs import *
from funcs.checks import *
from discord import slash_command, option

class images(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(
        guild_only = True,
        name = 'wanted',
        description = 'Create a wanted poster',
        name_localizations = {
            'en-US': 'wanted',
            'en-GB': 'wanted',
            'es-ES': 'búsqueda',
            'pt-BR': 'procurado',
            'fr': 'recherché'
        },
        description_localizations = {
            'en-US': 'Create a wanted poster',
            'en-GB': 'Create a wanted poster',
            'es-ES': 'Crear un cartel de búsqueda',
            'pt-BR': 'Cria um cartaz de procurado',
            'fr': 'Créer une affiche recherchée'
        }
    )
    @option(name = 'member', description = 'Mencione um membro')
    @vote()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def procurado(self, ctx: discord.Interaction, member: discord.Member = None):

        if member == None:

            member = ctx.author

        if mod.find_one({'_id':ctx.guild.id})['lang'] != 'pt-br':

            procurado = Image.open('./images/images/wanted.jpg')

            asset = member.avatar.replace(size = 128)

            data = BytesIO(await asset.read())

            pfp = Image.open(data)

            pfp = pfp.resize((398,307))

            procurado.paste(pfp, (34,217))

            procurado.save('./images/img/Procurado.jpg')

            await ctx.response.send_message(file = discord.File('./images/img/Procurado.jpg'))

            return

        procurado = Image.open('./images/images/procurado.png')

        asset = member.avatar.replace(size = 128)

        data = BytesIO(await asset.read())

        pfp = Image.open(data)

        pfp = pfp.resize((193,149))

        procurado.paste(pfp, (18,71))

        procurado.save('./images/img/Procurado.jpg')

        await ctx.response.send_message(file = discord.File('./images/img/Procurado.jpg'))

    @slash_command(
        guild_only = True,
        name = 'achievement_minecraft',
        description = 'Create a achievement of minecraft',
        name_localizations = {
            'pt-BR': 'conquista_minecraft',
        },
        description_localizations = {
            'pt-BR': 'Cria uma conquista do minecraft',
        }
    )
    @option(name = 'item', description = 'Escolha o item da conquista')
    @option(name = 'line1', description = 'Escreva o titulo da conquista')
    @option(name = 'line2', description = 'Escreva a conquista')
    @vote()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def conquistamine(self ,ctx: discord.Interaction, line1, line2):

        conquista1 = Image.open('./images/images/mineconquista.png').convert("RGBA")
    
        draw = ImageDraw.Draw(conquista1)

        icons = Image.open('./images/images/iconsminecraft/logo.png')

        icons = icons.resize((40,40)).convert("RGBA")

        font = ImageFont.truetype("./images/fonts/Minecraft.ttf",size=18)

        draw.text((70,15), line1 ,font = font,fill=(255,255,0))

        draw.text((70,35), line2 ,font = font)

        conquista1.paste(icons,(20,20))

        conquista1.save('./images/img/conquista.png')

        await ctx.response.send_message(file = discord.File('./images/img/conquista.png'))  

    @slash_command(
        guild_only = True,
        name = 'perfection',
        description = 'Cria um memme de "perfeição"',
        )
    @option(name = 'member', description = 'Mencione um membro')
    @vote()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def perfeição(self, ctx: discord.Interaction, member: discord.Member = None):

        t = translates(ctx.guild)

        if member == None:

            member = ctx.author

        perfeição = Image.open('./images/images/perfeicao.jpeg')

        draw = ImageDraw.Draw(perfeição)

        font = ImageFont.truetype("./images/fonts/LeagueGothic-Regular-VariableFont_wdth.ttf",size=20)

        draw.text((9,6), t['args']['images']['perfection'] , fill= (0,0,0) ,font = font)
        
        asset = member.avatar.replace(size = 128)

        data = BytesIO(await asset.read())

        pfp = Image.open(data)

        pfp = pfp.resize((150,150))

        perfeição.paste(pfp, (144,52))
        
        perfeição.save('./images/img/perfeicao.png')

        await ctx.response.send_message(file = discord.File('./images/img/perfeicao.png'))

    @slash_command(
        guild_only = True,
        name = 'cat',
        description = 'Envia uma imagem de gato aleatoria',
        )
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cat(self,ctx: discord.Interaction):

        t = translates(ctx.guild)

        r = requests.get(

            'https://api.thecatapi.com/v1/images/search')

        res = r.json()

        cat = discord.Embed(title = f"🐱{t['args']['images']['cat']}",
        color = hexacolors.string('indigo'))
        cat.set_image(url = res[0]['url'])

        await ctx.response.send_message(embed = cat)
    
    @slash_command(
        guild_only = True,
        name = 'body_minecraft',
        description = 'Envia o corpo de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def body(self, ctx: discord.Interaction, player):

        t = translates(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.response.send_message(f'https://crafatar.com/renders/body/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await ctx.response.send_message(t['args']['miecraft']['errorbody'])

    @slash_command(
        guild_only = True,
        name = 'head_minecraft',
        description = 'Envia a cabeça de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def head(self, ctx: discord.Interaction, player):

        t = translates(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.response.send_message(f'https://crafatar.com/renders/head/{r.json()["id"]}/?size=128&overlay')

        except:

            await ctx.response.send_message(t['args']['miecraft']['errorhead'])

    @slash_command(
        guild_only = True,
        name = 'skin_minecraft',
        description = 'Envia uma skin de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def skin(self, ctx: discord.Interaction, player):

        t = translates(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.response.send_message(f'https://crafatar.com/skins/{r.json()["id"]}')
        
        except:

            await ctx.response.send_message(t['args']['miecraft']['errorskin'])

    @slash_command(
        guild_only = True,
        name = 'avatar_player_minecraft',
        description = 'Envia a cabeça de um player',
        )
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def avatar(self, ctx: discord.Interaction, player):

        t = translates(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.response.send_message(f'https://crafatar.com/avatars/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await ctx.response.send_message(t['args']['miecraft']['erroravatar'])

    @perfeição.error
    async def perfição_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, NoVote):

            await ctx.response.send_message(error, ephemeral = True)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
        
    @body.error
    async def body_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @head.error
    async def body_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
        
    @avatar.error
    async def body_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @skin.error
    async def body_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @cat.error
    async def body_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @procurado.error
    async def procurado_error(self, ctx: discord.Interaction, error):

        t = translates(ctx.guild)

        if isinstance(error, NoVote):

            await ctx.response.send_message(error, ephemeral = True)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.response.send_message(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(images(bot))