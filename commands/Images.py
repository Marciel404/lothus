import discord, random, requests

from PIL import ImageDraw, ImageFont, Image
from io import BytesIO
from discord.ext import commands
from utils.defs import *
from discord import slash_command, option

class images(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'wanted', description = 'Cria um cartaz de procurado')
    @option(name = 'member', description = 'Mencione um membro')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def procurado(self, ctx, member: discord.Member = None):
    
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

    @slash_command(name = 'achievement_minecraft', description = 'Cria uma conquista do minecraft')
    @option(name = 'achievement', description = 'Escreva a conquista')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def conquistamine(self ,ctx, name):

        conquista1 = Image.open('./images/images/conquista.jpeg')
        
        draw = ImageDraw.Draw(conquista1)

        font = ImageFont.truetype("./images/fonts/Minecrafter.Alt.ttf",size=15)

        draw.text((59,35), name ,font = font)

        conquista1.save('./images/img/conquista.png')

        await ctx.respond(file = discord.File('./images/img/conquista.png'))

    @slash_command(name = 'perfection', description = 'Cria um memme de "perfeição"')
    @option(name = 'member', description = 'Mencione um membro')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def perfeição(self, ctx, member: discord.Member = None):
    
        t = await translate(ctx.guild)

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

    @slash_command(name = 'naughty', description = 'Cria uma foto do meliodas safadão')
    @option(name = 'member', description = 'Mencione o membro')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def safadão(self, ctx, member: discord.Member):

        escolha = random.choice(['1','2','3','4'])

        safadão = Image.open(f'./images/images/{escolha}.jpeg')

        asset = ctx.author.avatar.replace(size = 128)

        data = BytesIO(await asset.read())

        pfp = Image.open(data)

        asset2 = member.avatar.replace(size = 128)

        data2 = BytesIO(await asset2.read())

        pfp2 = Image.open(data2)
        
        if escolha == '1':
            
            pfp = pfp.resize((50,50))

            safadão.paste(pfp, (142,53))

            pfp2 = pfp2.resize((50,50))

            safadão.paste(pfp2, (102,35))

            safadão.save('./images/img/safadao.png')

        elif escolha == '2':

            pfp = pfp.resize((100,100))

            safadão.paste(pfp, (139,20))

            pfp2 = pfp2.resize((20,20))

            safadão.paste(pfp2, (95,50))

            safadão.save('./images/img/safadao.png')

        elif escolha == '3':

            pfp = pfp.resize((81,81))

            safadão.paste(pfp, (339,51))
            
            pfp2 = pfp2.resize((79,79))

            safadão.paste(pfp2, (238,47))

            safadão.save('./images/img/safadao.png')

        elif escolha == '4':

            pfp = pfp.resize((100,100))

            safadão.paste(pfp, (135,70))
            
            pfp2 = pfp2.resize((100,100))
            
            safadão.paste(pfp2, (308,10))

            safadão.save('./images/img/safadao.png')

        await ctx.respond(file = discord.File('./images/img/safadao.png'))

    @slash_command(name = 'cat', description = 'Envia uma imagem de gato aleatoria')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cat(self,ctx):

        t = await translate(ctx.guild)

        r = requests.get(

            'https://api.thecatapi.com/v1/images/search')

        res = r.json()

        cat = discord.Embed(title = f"🐱{t['args']['images']['cat']}")
        cat.set_image(url = res[0]['url'])

        await ctx.respond(embed = cat)

    @perfeição.error
    async def beg_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @safadão.error
    async def beg_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @conquistamine.error
    async def beg_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @procurado.error
    async def beg_error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(images(bot))