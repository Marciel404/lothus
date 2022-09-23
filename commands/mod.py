import discord, requests

from discord.ext import commands
from discord import slash_command, option
from db.moderation import *
from utils.defs import *
from classes.selectbuttons import *

class moderation(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(guild_only = True, name = 'setlang', description = 'Define o idioma do bot')
    @commands.has_guild_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlang(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t['args']['lang']['select'], view = discord.ui.View(setlang(self.bot, ctx.author,t)), ephemeral = True)

    @slash_command(guild_only = True, name = 'setlogs', description = 'Define um canal de logs')
    @commands.has_guild_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlogs(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond('',view = discord.ui.View(setlog(self.bot,ctx.author,t)), ephemeral = True)

    @slash_command(guild_only = True, name = 'autorole', description = 'Define um cargo para o auto role')
    @option(name = 'role', description = 'Escolha o cargo')
    @commands.has_guild_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def autorole(self, ctx, role: discord.Role = None):

        t = await translate(ctx.guild)

        if role == None:

            await autorole('autorole',False,ctx.guild,None)

            await ctx.respond(t['args']['mod']['unsetautorole'])

            return

        await autorole('autorole',True,ctx.guild,role.id)

        await ctx.respond(f"{t['args']['mod']['setautorole']} {role.mention}")

    @slash_command(guild_only = True, name = 'kick', description = 'Expulsa uma pessoa do server')
    @option(name = 'member', description = 'Escolha o membro a expulsar')
    @option(name = 'reason', description = 'Motivo para banir')
    @commands.has_guild_permissions(kick_members = True)
    @commands.bot_has_guild_permissions(kick_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *,reason=None):

        t = await translate(ctx.guild)

        if reason == None:

            reason = t["args"]["mod"]["notreason"]

        await ctx.respond(t["args"]["mod"]["confirmkick"].format(member.mention),view = buttonkick(self.bot,member,reason, ctx.author))

    @slash_command(guild_only = True, name = 'ban', description = 'Bane um membro do server')
    @option(name = 'member', description = 'Escolha um membro a banir')
    @option(name = 'reason', description = 'Motivo de banir')
    @commands.has_guild_permissions(ban_members = True)
    @commands.bot_has_guild_permissions(ban_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Ban(self, ctx, member: discord.Member, *,reason=None):

        t = await translate(ctx.guild)

        if reason == None:

            reason = t["args"]["mod"]["notreason"]

        await ctx.respond(t["args"]["mod"]["confirmban"].format(member.mention),view = buttonban(self.bot,member,reason,ctx.author))

    @slash_command(guild_only = True, name = 'clear', description = 'Limpa o chat')
    @option(name = 'qnt', description = 'Escolha uma quantidade de mensagem a limpar')
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx, qnt: int):

        t = await translate(ctx.guild)
            
        if qnt > 1000:

            await ctx.respond(t["args"]["mod"]["limiteclear1"])

        elif qnt == 0:

            await ctx.respond(t["args"]["mod"]["limiteclear2"])

        elif qnt < 0:

            await ctx.respond(t["args"]["mod"]["limiteclear3"])

        else:

            purge = await ctx.channel.purge(limit=qnt)

            await ctx.respond(t["args"]["mod"]["clearchat"].format(len(purge), ctx.author.mention))

    @slash_command(guild_only = True, name = 'unban', description = 'Desbane um membro')
    @option(name = 'id', description = 'Id do membro')
    @option(name = 'reason', description = 'Motivo de desbanir')
    @commands.has_guild_permissions(ban_members = True)
    @commands.bot_has_guild_permissions(ban_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unban(self, ctx, id: int, *, reason = None):

        l1 = self.bot.get_channel(self.bot.get_channel(mod.find_one({"_id": ctx.guild.id})["logmod"]))

        t = await translate(ctx.guild)

        if reason == None:

            reason = t["args"]["mod"]["notreason"]

        e = discord.Embed(title = 'UnBan',

        description = t["args"]["mod"]["logunban"].format(id,{ctx.author},reason,id))

        try:

            user = await self.bot.fetch_user(id)

            await ctx.guild.unban(user)

            await l1.send(embed = e)

            await ctx.respond(f'{id} {t["args"]["mod"]["unbansucess"]}')
            
        except:

            user = await self.bot.fetch_user(id)

            await ctx.guild.unban(user)

            await ctx.respond(embed = e)

    @slash_command(guild_only = True, name = 'add_warning', description = 'Da uma advertencia para um membro')
    @option(name = 'member', description = 'Mencione o membro')
    @option(name = 'reason', description = 'Motivo da advertencia')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(kick_members = True)
    async def adv(self, ctx, member: discord.Member, reason):

        t = await translate(ctx.guild)

        e = discord.Embed(

        title = t['args']['adv'],

        description = t['args']['mod']['adv'].format(member.mention,ctx.author.mention,reason))

        e.set_footer(text = f'id: {member.id}')

        try:

            db = mod.find_one({'_id':ctx.guild.id})

            if db['lmod']['True?'] == True:

                advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':+1}}, upsert = True )

                await adcadvdb(ctx.guild,ctx.author,member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']}",reason)

                await ctx.respond(t['args']['advsucess'].format(member.mention), ephemeral = True)

                channel = self.bot.get_channel(db['lmod']['id'])

                try:

                    w = await self.bot.fetch_webhook(db['lmod']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                    await logs('lmod',True,ctx.guild,db['lmod']['id'], webhook.id)

                    w = await self.bot.fetch_webhook(db['lmod']['webhook'])

                    await w.send(embed = e)
            
        except:

            advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':+1}}, upsert = True )

            await adcadvdb(ctx.guild,ctx.author,member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']}",reason)

    @slash_command(guild_only = True, name = 'remove_warning', description = 'Remove uma advertencia de um membro')
    @option(name = 'member', description = 'Mencione o membro')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(kick_members = True)
    async def rmvadv(self, ctx, member: discord.Member):

        t = await translate(ctx.guild)

        try:

            if advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt'] == 0:

                await ctx.respond(t['args']['notadv'], ephemeral = True)

                return

            e = discord.Embed(

            title = t['args']['rmvadv'],

            description = t['args']['mod']['rmvadv'].format(member.mention,ctx.author.mention))

            e.set_footer(text = f'id: {member.id}')

            rankings = advdb.find_one({'_id': f'{ctx.guild.id}_{member.id}'})

            hgc = rankings[f'{t["args"]["adv"]}{advdb.find_one({ "_id":f"{ctx.guild.id}_{member.id}"})["qnt"]}']

            try:

                db = mod.find_one({'_id':ctx.guild.id})

                if db['lmod']['True?'] == True:

                    advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':-1}}, upsert = True )

                    await rmvadvdb(ctx.guild,hgc[0],member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']+1}",hgc[2])

                    await ctx.respond(t['args']['rmvadvsucess'].format(member.mention), ephemeral = True)

                    channel = self.bot.get_channel(db['lmod']['id'])

                    try:

                        w = await self.bot.fetch_webhook(db['lmod']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                        await logs('lmod',True,ctx.guild,db['lmod']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lmod']['webhook'])

                        await w.send(embed = e)
                
            except:

                advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':-1}}, upsert = True )

                await rmvadvdb(ctx.guild,hgc[0],member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']+1}",hgc[2])

        except:

            await ctx.respond(t['args']['notadv'],ephemeral = True)

    @slash_command(guild_only = True, name = 'force_move', description = 'Move um membro para a sua call privada')
    @option(name = 'membro', description = 'Escolha o membro para mover para uma call')
    @option(name = 'canal', description = 'Escolha o canal para mover o membro')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(move_members = True)
    async def fmv(self, ctx, member: discord.Member, canal: discord.VoiceChannel):

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

            call = self.bot.get_channel(canal.id)

            if member.voice == None:

                await ctx.respond(t['args']['mod']['notcall'].formmat(member.mention), ephemeral = True)

                return

            await member.move_to(call)

            await ctx.respond(t['args']['mod']['mvcall'].formart(member.mention, call.mention), ephemeral = True)
        
        else:

            await ctx.respond(t['args']['notvote'])

    @slash_command(guild_only = True, name = 'force_disconnect', description = 'Desconecta uma pessoa da call')
    @option(name = 'member', description = 'Escolha o membro para desconectar da call')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(move_members = True)
    async def fdsc(self, ctx, member: discord.Member):

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

            if member.voice == None:

                await ctx.respond(t['args']['mod']['notcall'].formmat(member.mention), ephemeral = True)

                return

            await member.move_to(None)

            await ctx.respond(t['args']['mod']['dsccall'].formart(member.mention), ephemeral = True)
        
        else:

            await ctx.respond(t['args']['notvote'])

    @slash_command(guild_only = True, name = 'embed', description = 'Envia uma embed em um chat desejado')
    @option(name = 'channel', description = 'Escolha o chat para enviar a embed')
    @option(name = 'title', description = 'Escreva o titulo da embed')
    @option(name = 'link_image', description = 'Escolha a imagem da embed')
    @option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @option(name = 'content', description = 'Escreva o conteudo da embed')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(manage_channels = True)
    async def embed(self, ctx, channel: discord.TextChannel = None, title = None, img = None, mention: discord.Role = None, content = None):

        if channel == None:

            channel = ctx.channel

        if title == None:

            title = ''

        if img == None:

            img = ''

        if content == None:

            content = ''

        if mention == None:

            mention == ''

        else: 

            mention = mention.mention

        e = discord.Embed(title = title, description = content, colour = 0x4B0082)

        e.set_image(url = img)

        e.set_footer(text = f'{ctx.guild.name}, author: {ctx.author.name}', icon_url = ctx.guild.icon)

        channel2 = self.bot.get_channel(channel.id)

        await channel2.send(mention,embed = e)

    @slash_command(guild_only = True,name = 'editembed', description = 'Edita uma embed já enviada')
    @option(name = 'channel', description = 'Envie o id do canal')
    @option(name = 'embedid', description = 'Envie o id da embed')
    @option(name = 'title', description = 'Escreva o titulo da embed')
    @option(name = 'img', description = 'Escolha a imagem da embed')
    @option(name = 'mention', description = 'Mencione um cargo para mencionar na embed')
    @option(name = 'content', description = 'Escreva o conteudo da embed')
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_guild_permissions(manage_channels = True)
    async def editembed(self, ctx, embedid, title = None, img = None, mention: discord.Role = None, content = None, channel: discord.TextChannel = None):

        if channel == None:

            channel = ctx.channel

        if title == None:

            title = ''

        if img == None:

            img = ''

        if content == None:

            content = ''

        if mention == None:

            mention == ''

        else: 

            mention = mention.mention

        mensagem = await channel.fetch_message(int(embedid))

        e = discord.Embed(title = title, description = content, colour = 0x4B0082)

        e.set_image(url = img)

        e.set_footer(text = f'{ctx.guild.name} author: {ctx.author.name}', icon_url = ctx.guild.icon)

        await mensagem.edit(mention,embed = e)

    @fmv.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @fdsc.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @editembed.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @embed.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @setlang.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @adv.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @rmvadv.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @autorole.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)
    
    @setlogs.error
    async def setlogs_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)


        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)

    @Ban.error
    async def ban_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.respond(f':x: || {t["args"]["mod"]["botnotpermission1"]} "Ban_Members" {t["args"]["mod"]["botnotpermission2"]}')

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @unban.error
    async def unban_error(self,ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.respond(f':x: || {t["args"]["mod"]["botnotpermission1"]} "Ban_Members" {t["args"]["mod"]["botnotpermission2"]}')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)

        if isinstance(error, commands.MemberNotFound):

            await ctx.respond(f':x: || {t["args"]["mod"]["bannotfound"]}')

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

    @clear.error
    async def clear_error(self,ctx, error):

        t = await translate(ctx.guild)
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.respond(f':x: || {t["args"]["mod"]["botnotpermission1"]} "Manage_chennels" {t["args"]["mod"]["botnotpermission2"]}')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.respond(f":x: || {t['args']['mod']['notpermission']}", ephemeral = True)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(moderation(bot))