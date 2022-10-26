import discord, time, random,platform

from discord.ext import commands
from discord import slash_command, option
from classes.buttons import profile
from utils.defs import *
from classes.selectbuttons import *
from db.economy import *
from db.members import *

class gerais(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(
        guild_only = True,
        name = 'hello_world',
        description = 'Lothus test command',
        name_localizations = {
            'en-US': 'hello_world',
            'en-GB': 'hello_world',
            'es-ES': 'hola_mundo',
            'pt-BR': 'ola_mundo',
            'fr': 'bonjour_le_monde'
        },
        description_localizations = {
            'en-US': 'Lothus test command',
            'en-GB': 'Lothus test command',
            'es-ES': 'Comando de prueba de Lothus',
            'pt-BR': 'Comando de teste do Lothus',
            'fr': 'Commande de test Lothus'
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hello(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t["args"]["hello"])

    @slash_command(
        guild_only = True,
        name = 'help',
        description = 'Help command lothus',
        name_localizations = {
            'en-US': 'help',
            'en-GB': 'help',
            'es-ES': 'ayuda',
            'pt-BR': 'ajuda',
            'fr': 'aider'
        },
        description_localizations = {
            'en-US': 'Help command Lothus',
            'en-GB': 'Help command Lothus',
            'es-ES': 'Comando de ayuda de Lotus',
            'pt-BR': 'Comando de ajuda do Lothus',
            'fr': 'Commande de aider Lothus'
        })
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):

        t = await translate(ctx.guild)

        h = discord.Embed(title =  t['help']['extras']['commands'],
        description = t['help']['extras']['init']
        )
        h.set_thumbnail(url = self.bot.user.avatar)

        await ctx.respond(embed = h, view = discord.ui.View(selecthelp(self.bot,ctx.author,t)))

    @slash_command(
        guild_only = True,
        name = 'random',
        description = 'Choose a random number for you',
        name_localizations = {
            'en-US': 'random',
            'en-GB': 'random',
            'es-ES': 'aleatorio',
            'pt-BR': 'aleatorio',
            'fr': 'aléatoire'
        },
        description_localizations = {
            'en-US': 'Choose a random number for you',
            'en-GB': 'Choose a random number for you',
            'es-ES': 'Elija un número aleatorio para usted',
            'pt-BR': 'Escolhe um numero aleatorio para você',
            'fr': 'Choisissez un nombre aléatoire pour vous'
        })
    @option(name = 'number', description = 'Coloque um numero')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, ctx,numero: int):

        t = await translate(ctx.guild)
        
        dado = random.randint(0,int(numero))

        await ctx.respond(f'{t["args"]["random"]} {dado}')

    @slash_command(
        guild_only = True,
        name = 'ping',
        description = 'Shows my ping and discord api',
        description_localizations = {
            'en-US': 'Shows my ping and discord api',
            'en-GB': 'Shows my ping and discord api',
            'es-ES': 'Mostrar mi api de ping y discord',
            'pt-BR': 'Mostra o meu ping e da api do discord',
            'fr': 'Afficher mon ping et discord api'
        })
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        
        start_time = time.time()

        t = await translate(ctx.guild)

        Ping = round(self.bot.latency * 1000)

        end_time = time.time()

        p4 = discord.Embed(title = 'Ping', 

        description = f'''
{t["args"]["ping"]}: {Ping}ms
API: {round((end_time - start_time) * 1000)}ms
''', 

        color = 0x2ecc71)

        await ctx.respond(embed = p4)

    @slash_command(
        guild_only = True,
        name = 'servers',
        description = "Tells how many servers I'm on",
        description_localizations = {
            'en-US': "Tells how many servers I'm on",
            'en-GB': "Tells how many servers I'm on",
            'es-ES': 'Dime en cuántos servidores estoy',
            'pt-BR': 'Diz em quantos servers eu estou',
            'fr': 'Dites-moi sur combien de serveurs je suis'
        })
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servers(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t["args"]["servers"]["s"].format(str(len(self.bot.guilds))))

    @slash_command(
        guild_only = True,
        name = 'server_info',
        description = 'Pulls information from the server',
        description_localizations = {
            'en-US': "Pulls information from the server",
            'en-GB': "Pulls information from the server",
            'es-ES': 'Extraer la información del servidor',
            'pt-BR': 'Puxa as informações do server',
            'fr': 'Obtenir les informations du serveur'
        })
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(name = 'server', description = 'Envie o id do server')
    async def serverInfo(self, ctx, server: discord.Guild = None):

        t = await translate(ctx.guild)

        if server == None:

            server = ctx.guild
        
        if mod.find_one({'_id':ctx.guild.id})['lang'] != 'pt-br':

            servercreate = server.created_at.strftime(f"%Y %m %d")

        else:

            servercreate = server.created_at.strftime(f"%d %m %Y")

        embed = discord.Embed(title = f'**{server.name}**',

        color = random.randint(00000, 99999))

        embed.add_field(name = f':scroll: {t["args"]["si"]["name"]}:', 

        value = server.name,
        
        inline = True)
        
        embed.add_field(name = f':computer:  {t["args"]["si"]["id"]}:', 

        value = server.id,

        inline = True)

        embed.add_field(name = f':busts_in_silhouette: {t["args"]["si"]["members"]}:', 

        value = server.member_count,

        inline = True)

        embed.add_field(name = f':speech_balloon: {t["args"]["si"]["channels"]}:({len(server.text_channels)+len(server.voice_channels)})',

        value = f':keyboard: {t["args"]["si"]["text"]}: {len(server.text_channels)}\n :loud_sound: {t["args"]["si"]["voice"]}:{len(server.voice_channels)}',

        inline = True)

        embed.add_field(name = f':shield: {t["args"]["si"]["verify"]}:',

        value = '{}'.format(str(server.verification_level).upper()),

        inline = True)

        embed.add_field(name = f':crown: {t["args"]["si"]["own"]}:', 

        value = '<@{0}>\n ({0})'.format(server.owner_id),

        inline = True)

        embed.add_field(name = f':calendar_spiral:{t["args"]["si"]["create"]}:', 
        
        value = servercreate,

        inline = True)

        if server.icon == None:

            embed.set_thumbnail(url='')

        else:

            embed.set_thumbnail(url=server.icon)

        await ctx.respond(embed = embed)

    @slash_command(
        guild_only = True,
        name = 'user_info', 
        description = "pulls a member's information or their",
        description_localizations = {
            'en-US': "Pulls a member's information or their",
            'en-GB': "Pulls a member's information or their",
            'es-ES': 'Extrae la información de un miembro o su',
            'pt-BR': 'Puxa as informações de algum membro ou as suas',
            'fr': "Obtenir les informations d'un membre ou leur"
        })
    @commands.cooldown(1, 5, commands.BucketType.user)
    @option(name = 'member', description = 'Escolha um membro')
    async def userinfo(self, ctx, member: discord.Member = None):

        t = await translate(ctx.guild)
        
        if member == None:

            member = ctx.author

        await update_bank(member,0)

        user = bank.find_one({"_id": member.id})

        embed = discord.Embed(colour=member.color)

        embed.set_author(name=f"User Info - {member}"),

        if member.avatar == None:

            embed.set_thumbnail(url=''),

        else:

            embed.set_thumbnail(url=member.avatar),

        if mod.find_one({'_id':ctx.guild.id})['lang'] != 'pt-br':

            membercreate = member.created_at.strftime(f"%Y %m %d")

            memberjoin = member.joined_at.strftime(f"%Y %m %d")

        else:

            membercreate = member.created_at.strftime(f"%d %m %Y")

            memberjoin = member.joined_at.strftime(f"%d %m %Y")

        embed.add_field(name = f'{t["args"]["ui"]["name"]}:',

        value = member.display_name,inline=True)

        embed.add_field(name = f'ID:',

        value = member.id,inline=True)

        embed.add_field(name = f'{t["args"]["ui"]["cc"]}:',

        value = membercreate,inline=True)

        embed.add_field(name = f'{t["args"]["ui"]["js"]}:',

        value = memberjoin,inline=True)

        embed.add_field(name = f'{t["args"]["ui"]["toprole"]}:',

        value = member.top_role.mention,inline=True)

        embed.add_field(name = 'LothCoins',

        value = user["LOTHCOINS"], inline = True)

        await ctx.respond(embed=embed)

    @slash_command(guild_only = True,name = 'avatar', description = 'Envia o avatar de um membro')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'member', description = 'Ecolha um membro')
    async def avatar(self, ctx, member: discord.Member = None):

        t = await translate(ctx.guild)

        if member == None:

            member = ctx.author

        if member.avatar == None:

            embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.default_avatar}) {t["args"]["avatar"]["click2"]}')

            embed.set_image(url = f'{member.default_avatar}')

        elif member.guild_avatar != None:

            embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.guild_avatar}) {t["args"]["avatar"]["click2"]}')

            embed.set_image(url = f'{member.guild_avatar}')

        else:

            embed = discord.Embed(title = f'Avatar {member}', 

            description = f'[{t["args"]["avatar"]["click1"]}]({member.avatar}) {t["args"]["avatar"]["click2"]}')
            embed.set_image(url = f'{member.avatar}')
        
        await ctx.respond(embed = embed)

    @slash_command(guild_only = True,name = 'invite', description = 'Encia o link para me convidar para seu server')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self, ctx):

        t = await translate(ctx.guild)
        
        e = discord.Embed(title = t['args']['invite']['invite'], 

        description = f'[{t["args"]["invite"]["dsc"]}](https://discord.com/api/oauth2/authorize?client_id=1012121641947517068&permissions=8&scope=bot%20applications.commands)')

        e.set_thumbnail(url = self.bot.user.avatar)

        await ctx.respond(embed=e)

    @slash_command(guild_only = True,name = 'vote', description = 'Envia o link para votar em mim no top.gg')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def Vote(self, ctx):

        if ctx.guild == None:

            return

        t = await translate(ctx.guild)

        e1 = self.bot.get_emoji(972895959191289886)

        server = '[Server Suport](https://discord.com/invite/USMVRUcDGa)'

        top = '[Top.gg](https://top.gg/bot/1012121641947517068)'

        inv = '[Invite](https://discord.com/api/oauth2/authorize?client_id=1012121641947517068&permissions=8&scope=bot%20applications.commands)'

        topgg = discord.Embed(title = 'Vote', 

        description = t['args']['topgg']['dsc'].format(ctx.author.mention))

        topgg.add_field(name = f':grey_question: {t["args"]["topgg"]["duvids"]}', value = server, inline = False)
        
        topgg.add_field(name = f'{e1} {t["args"]["topgg"]["cresc"]}', 
        
            value = top, inline = False)

        topgg.add_field(name = f':partying_face: {t["args"]["topgg"]["invite"]}', 

            value = inv, inline = False)

        topgg.set_thumbnail(url = self.bot.user.avatar.url)

        await ctx.respond(embed = topgg)

    @slash_command(guild_only = True,name = 'bot_info', description = 'Envia algumas informações minha')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def botinfo(self, ctx):

        t = await translate(ctx.guild)

        python = self.bot.get_emoji(971189876986884186)
        disocrd = self.bot.get_emoji(971212878763917362)
        Vs = self.bot.get_emoji(971571518532354118)
        name = self.bot.get_emoji(971487187361218620)

        e = discord.Embed(title = t["args"]["botinfo"]["mif"])
        e.set_thumbnail(url = self.bot.user.avatar.url)
        e.add_field(name = f'{name} {t["args"]["botinfo"]["name"]}', value = self.bot.user.name, inline = True)
        e.add_field(name = f'{Vs} {t["args"]["botinfo"]["language"]}', value = f'{python} Python', inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = f'{disocrd} {t["args"]["botinfo"]["version"]}', value = discord.__version__, inline = True)
        e.add_field(name = f'{python} {t["args"]["botinfo"]["pyversion"]}', value = platform.python_version(), inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = f':calendar_spiral: {t["args"]["botinfo"]["ii"]}', value = '2019', inline = True)
        e.add_field(name = f':calendar_spiral: {t["args"]["botinfo"]["rz"]}', value = '2022', inline = True)
        e.add_field(name = '════════════', value = '════════════', inline = False)
        e.add_field(name = 'Commands', value = self.bot.application_commands.count, inline = True)

        await ctx.respond(embed = e)
        
    @slash_command(guild_only = True,name = 'emoji_info', description = 'Envia algumas informações de um emoji')
    @commands.cooldown(1,5, commands.BucketType.user)
    @option(name = 'emoji', description = 'Escolha um emoji')
    async def EmojiInfo(self, ctx, emoji: discord.Emoji):

        t = await translate(ctx.guild)

        e1 = self.bot.get_emoji(971487187361218620)

        embed = discord.Embed(title = f'{emoji} Emoji Info')

        embed.set_thumbnail(url = emoji.url)

        embed.add_field(name = f':notepad_spiral: {t["args"]["emoji"]["name"]}', value = emoji.name, inline = True)
        
        embed.add_field(name = f'{e1} {t["args"]["emoji"]["id"]}', value = emoji.id, inline = True)

        embed.add_field(name = f':goggles: {t["args"]["emoji"]["mention"]}', value = f'`<:{emoji.name}:{emoji.id}>`', inline = True)

        embed.add_field(name = f':chains: Url', value = emoji.url, inline = True)

        embed.add_field(name = f':date: {t["args"]["emoji"]["adition"]}', value = emoji.created_at.strftime('%d %m %Y'), inline = True)

        embed.add_field(name = f':mag_right: {t["args"]["emoji"]["server"]}', value = emoji.guild, inline = True)

        await ctx.respond(embed = embed)

    @slash_command(guild_only = True,name = 'profile', description = 'Envia seu perfil')
    @option(name = 'member', description = 'Envia o perfil de um membro')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, member: discord.Member = None):

        if member == None:

            member = ctx.author

        if perf.count_documents({'_id': member.id}) == 0:

            await upPerfil(member,'r0','Idade',None)
            await upPerfil(member,'r1','Genero',None)
            await upPerfil(member,'r2',"País",None)
            await upPerfil(member,'r3','Cidade',None)
            await upPerfil(member,'r4', 'Descrição do perfil',"Lothus é um otimo Bot")
            await upPerfil(member,'r5', 'Casado com',None)
        
        i2 = 0

        embed = discord.Embed(title = 'Perfil')

        embed.set_thumbnail(url = member.display_avatar)

        while True:

            per = perf.find_one({'_id': member.id})

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
        
        if member.id == ctx.author.id:
    
            await ctx.respond(embed = embed, view = profile(ctx.author))

        else:

            await ctx.respond(embed = embed)

def setup(bot:commands.Bot):
    bot.add_cog(gerais(bot))