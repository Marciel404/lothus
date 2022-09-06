import discord

from discord.ext import commands
from db.moderation import *
from utils.defs import *

class eventslogs(commands.Cog):
    
    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):

        if message.guild == None:
            
            return

        t = await translate(message.guild)

        try:

            db = mod.find_one({'_id': message.guild.id})

            if db['ltxt']['True?'] == True:

                channel = self.bot.get_channel(db['ltxt']['id'])

                e = discord.Embed(

                description = t["args"]["logs"]["messaged"].format(message.author.mention, message.channel.mention),

                color = 0xff0000

                )
                e.add_field(name = f'{t["args"]["logs"]["msg"]}:', value = f'{message.content}', inline=False)

                e.set_author(name = f'{message.author.name}#{message.author.discriminator}', icon_url = message.author.display_avatar)

                try:

                    w = await self.bot.fetch_webhook(db['ltxt']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log')

                    await logs('ltxt',True,message.guild,db['ltxt']['id'], webhook.id)

                    w = await self.bot.fetch_webhook(db['ltxt']['webhook'])

                    await w.send(embed = e)
            
        except:

            None
    
    @commands.Cog.listener()
    async def on_message_edit(self, antes:discord.Message, depois:discord.Message):

        if antes.guild == None:
            
            return

        t = await translate(antes.guild)

        try:

            db = mod.find_one({'_id':antes.guild.id})

            if db['ltxt']['True?'] == True:

                channel = self.bot.get_channel(db['ltxt']['id'])

                e = discord.Embed(

                    description = t["args"]["logs"]["edit"].format(antes.author.mention,antes.channel.mention),

                    color = 0xfff000

                )
                e.add_field(name = f'{t["args"]["logs"]["old"]}:', value = f'{antes.content}', inline=False)

                e.add_field(name = f'{t["args"]["logs"]["new"]}:', value =  f'{depois.content}', inline=False)

                e.set_author(name = f'{antes.author.name}#{antes.author.discriminator}', icon_url = antes.author.display_avatar)

                try:

                    w = await self.bot.fetch_webhook(db['ltxt']['webhook'])

                    await w.send(embed = e)
                
                except:

                    webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                    await logs('ltxt',True,antes.guild,db['ltxt']['id'], webhook.id)

                    w = await self.bot.fetch_webhook(db['ltxt']['webhook'])

                    await w.send(embed = e)
        except:

            None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member:discord.Member, antes:discord.VoiceState, depois:discord.VoiceState):

        if antes.guild == None:
            
            return

        try:

            db = mod.find_one({'_id':member.guild.id})

            if db['lvoice']['True?'] == True:

                t = await translate(member.guild)

                channel = self.bot.get_channel(db['lvoice']['id'])

                if antes.channel == None:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["enter"]} `{depois.channel}`',

                    color = 0x00ff19

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    try:

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                        await logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)

                    return

                if depois.channel == None:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["exit"]} `{antes.channel}`',

                    color = 0xff0000

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    try:

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                        await logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)

                    return
                
                if antes.channel != depois.channel:

                    e = discord.Embed(

                    description = t['args']['logs']['semove'].format(member.mention, antes.channel.mention, depois.channel.mention),

                    color = 0xfff000

                    )
                    
                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    try:

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                        await logs('lvoice',True,member.guild,db['lvoice']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lvoice']['webhook'])

                        await w.send(embed = e)

                    return

            if db['lmic']['True?'] == True:

                t = await translate(member.guild)

                if antes.self_mute:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["sedesmute"]} `{depois.channel}`',

                    color = 0x00ff19

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    try:

                        w = await self.bot.fetch_webhook(db['lmic']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                        await logs('lmic',True,member.guild,db['lmic']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lmic']['webhook'])

                        await w.send(embed = e)

                elif depois.self_mute:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["semute"]} `{depois.channel}`',

                    color = 0xfff000

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    try:

                        w = await self.bot.fetch_webhook(db['lmic']['webhook'])

                        await w.send(embed = e)
                    
                    except:

                        webhook = await channel.create_webhook(name = 'Lothus', avatar = await self.bot.user.avatar.read(), reason = f'Log ')

                        await logs('lmic',True,member.guild,db['lmic']['id'], webhook.id)

                        w = await self.bot.fetch_webhook(db['lmic']['webhook'])

                        await w.send(embed = e)

        except:

            None

def setup(bot:commands.Bot):
    bot.add_cog(eventslogs(bot))