import discord, time, random,platform

from discord.ext import commands
from discord import slash_command, option
from utils.defs import *
from classes.selectbuttons import *
from db.economy import *
from db.members import *

class gerais(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(guild_only = True, name = 'hello_world', description = 'Comandos de teste do Lothus')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hello(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t["args"]["hello"])

    @slash_command(guild_only = True,name = 'help', description = 'Envia minha lista de comandos')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):

        t = await translate(ctx.guild)

        h = discord.Embed(title =  t['help']['extras']['commands'],
        description = t['help']['extras']['init']
        )
        h.set_thumbnail(url = self.bot.user.avatar)

        await ctx.respond(embed = h, view = discord.ui.View(selecthelp(self.bot,ctx.author,t)))

    @slash_command(guild_only = True,name = 'random', description = 'Escolhe um numero aleatorio')
    @option(name = 'number', description = 'Coloque um numero')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, ctx,numero: int):

        t = await translate(ctx.guild)
        
        dado = random.randint(0,int(numero))

        await ctx.respond(f'{t["args"]["random"]} {dado}')

    @slash_command(guild_only = True,name = 'ping', description = 'Envia meu ping')
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

    @slash_command(guild_only = True,name = 'servers', description = "Envia em quantos servers eu esrou")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servers(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t["args"]["servers"]["s"].format(str(len(self.bot.guilds))))

    @slash_command(guild_only = True,name = 'server_info', description = 'Envia algumas informações do server')
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

    @slash_command(guild_only = True,name = 'user_info', description = 'Envia algumas informações de um membro')
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
        
def setup(bot:commands.Bot):
    bot.add_cog(gerais(bot))