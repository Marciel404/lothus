import discord, requests

from PIL import ImageDraw, ImageFont, Image
from io import BytesIO
from discord.ext import commands
from utils.defs import *
from discord import slash_command, option

class images(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(guild_only = True, name = 'wanted', description = 'Cria um cartaz de procurado')
    @option(name = 'member', description = 'Mencione um membro')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def procurado(self, ctx, member: discord.Member = None):

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

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

                await ctx.respond(file = discord.File('./images/img/Procurado.jpg'))

                return

            procurado = Image.open('./images/images/procurado.png')

            asset = member.avatar.replace(size = 128)

            data = BytesIO(await asset.read())

            pfp = Image.open(data)

            pfp = pfp.resize((193,149))

            procurado.paste(pfp, (18,71))

            procurado.save('./images/img/Procurado.jpg')

            await ctx.respond(file = discord.File('./images/img/Procurado.jpg'))
        
        else:

            await ctx.respond(t['args']['notvote'])

    @slash_command(guild_only = True,name = 'achievement_minecraft', description = 'Cria uma conquista do minecraft')
    @option(name = 'item', description = 'Escolha o item da conquista')
    @option(name = 'line1', description = 'Escreva o titulo da conquista')
    @option(name = 'line2', description = 'Escreva a conquista')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def conquistamine(self ,ctx, line1, *, line2, item = None):
        
        if item == None:

            item = 'diamond'

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

            await ctx.respond(f'https://minecraft-api.com/api/achivements/{item}/{line1}/{line2}')
        
        else:

            await ctx.respond(t['args']['notvote'])

    @slash_command(guild_only = True,name = 'perfection', description = 'Cria um memme de "perfeição"')
    @option(name = 'member', description = 'Mencione um membro')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def perfeição(self, ctx, member: discord.Member = None):

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

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

            await ctx.respond(file = discord.File('./images/img/perfeicao.png'))
        
        else:

            await ctx.respond(t['args']['notvote'])

    @slash_command(guild_only = True,name = 'cat', description = 'Envia uma imagem de gato aleatoria')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cat(self,ctx):

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.thecatapi.com/v1/images/search')

        res = r.json()

        cat = discord.Embed(title = f"🐱{t['args']['images']['cat']}")
        cat.set_image(url = res[0]['url'])

        await ctx.respond(embed = cat)
    
    @slash_command(guild_only = True,name = 'body_minecraft', description = 'Envia o corpo de um player')
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def body(self, ctx, player):

        t = await translate(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.respond(f'https://crafatar.com/renders/body/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await ctx.respond(t['args']['miecraft']['errorbody'])

    @slash_command(guild_only = True,name = 'head_minecraft', description = 'Envia a cabeça de um player')
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def head(self, ctx, player):

        t = await translate(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.respond(f'https://crafatar.com/renders/head/{r.json()["id"]}/?size=128&overlay')

        except:

            await ctx.respond(t['args']['miecraft']['errorhead'])

    @slash_command(guild_only = True,name = 'skin_minecraft', description = 'Envia uma skin de um player')
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def skin(self, ctx, player):

        t = await translate(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.respond(f'https://crafatar.com/skins/{r.json()["id"]}')
        
        except:

            await ctx.respond(t['args']['miecraft']['errorskin'])

    @slash_command(guild_only = True,name = 'avatar_player_minecraft', description = 'Envia a cabeça de um player')
    @option(name = 'player', description = 'Nickname')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def avatar(self, ctx, player):

        t = await translate(ctx.guild)

        try:

            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}')

            await ctx.respond(f'https://crafatar.com/avatars/{r.json()["id"]}/?size=128&overlay')
        
        except:

            await ctx.respond(t['args']['miecraft']['erroravatar'])

    @perfeição.error
    async def perfição_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
        
    @body.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @head.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
        
    @avatar.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @skin.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @cat.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @procurado.error
    async def procurado_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @conquistamine.error
    async def body_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(images(bot))