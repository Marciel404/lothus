import discord

from discord.ext import commands
from discord import slash_command, option
from db.moderation import *
from db.economy import *
from utils.defs import *
from classes.selectbuttons import *

class moderation(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @slash_command(name = 'setlang', description = 'Define o idioma do bot')
    @commands.has_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlang(self, ctx):

        t = await translate(ctx.guild)

        await ctx.respond(t['args']['lang']['select'], view = discord.ui.View(setlang(self.bot, ctx.author,ctx.guild)), ephemeral = True)

    @slash_command(name = 'setlogs', description = 'Define um canal de logs')
    @commands.has_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def setlogs(self, ctx):

        await ctx.respond('',view = discord.ui.View(setlog(self.bot,ctx.author,ctx.guild)), ephemeral = True)

    @slash_command(name = 'autorole', description = 'Define um cargo para o auto role')
    @option(name = 'role', description = 'Escolha o cargo')
    @commands.has_permissions(manage_guild = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def autorole(self, ctx, role: discord.Role = None):

        t = await translate(ctx.guild)

        if role == None:

            await autorole('autorole',False,ctx.guild,None)

            await ctx.respond(t['args']['mod']['unsetautorole'])

            return

        await autorole('autorole',True,ctx.guild,role.id)

        await ctx.respond(f"{t['args']['mod']['setautorole']} {role.mention}")

    @slash_command(name = 'kick', description = 'Expulsa uma pessoa do server')
    @option(name = 'member', description = 'Escolha o membro a expulsar')
    @option(name = 'reason', description = 'Motivo para banir')
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *,reason=None):

        t = await translate(ctx.guild)

        if reason == None:

            reason = t["args"]["mod"]["notreason"]

        await ctx.respond(t["args"]["mod"]["confirmkick"].format(member.mention),view = buttonkick(self.bot,member,reason, ctx.author))

    @slash_command(name = 'ban', description = 'Bane um membro do server')
    @option(name = 'member', description = 'Escolha um membro a banir')
    @option(name = 'reason', description = 'Motivo de banir')
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Ban(self, ctx, member: discord.Member, *,reason=None):

        t = await translate(ctx.guild)

        if reason == None:

            reason = t["args"]["mod"]["notreason"]

        await ctx.respond(t["args"]["mod"]["confirmban"].format(member.mention),view = buttonban(self.bot,member,reason,ctx.author))

    @slash_command(name = 'clear', description = 'Limpa o chat')
    @option(name = 'qnt', description = 'Escolha uma quantidade de mensagem a limpar')
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_permissions(manage_channels = True)
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

    @slash_command(name = 'unban', description = 'Desbane um membro')
    @option(name = 'id', description = 'Id do membro')
    @option(name = 'reason', description = 'Motivo de desbanir')
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
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

    @slash_command(name = 'add_warning', description = 'Da uma advertencia para um membro')
    @option(name = 'member', description = 'Mencione o membro')
    @option(name = 'reason', description = 'Motivo da advertencia')
    @commands.has_permissions(kick_members = True)
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

                await self.bot.get_channel(db['lmod']['id']).send(embed = e)
            
        except:

            advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':+1}}, upsert = True )

            await adcadvdb(ctx.guild,ctx.author,member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']}",reason)

    @slash_command(name = 'remove_warning', description = 'Remove uma advertencia de um membro')
    @option(name = 'member', description = 'Mencione o membro')
    @commands.has_permissions(kick_members = True)
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

                    await self.bot.get_channel(db['lmod']['id']).send(embed = e)
                
            except:

                advdb.update_one( { "_id":f'{ctx.guild.id}_{member.id}'}, {'$inc':{f'qnt':-1}}, upsert = True )

                await rmvadvdb(ctx.guild,hgc[0],member,f"{t['args']['adv']}{advdb.find_one({ '_id':f'{ctx.guild.id}_{member.id}'})['qnt']+1}",hgc[2])

        except:

            await ctx.respond(t['args']['notadv'],ephemeral = True)

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