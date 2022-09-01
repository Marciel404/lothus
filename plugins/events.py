import discord
from discord.ext import commands
from db.moderation import *
from utils.defs import *

class events(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):

        print(f'Eu estou online como {self.bot.user}')

        print(discord.__version__)
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):

        await lang('lang', 'en-us', guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild:discord.Guild):

        mod.find_one_and_delete({'_id':guild.id})

        if (advdb.count_documents({ "_id": guild.id}) == 1):

            advdb.find_one_and_delete({"_id": guild.id})

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        t = await translate(member.guild)

        try:

            db = mod.find_one({'_id':member.guild.id})

            if db['autorole']['true'] == True:

                try:

                    await member.add_roles(discord.utils.get(member.guild.roles, id = db['autorole']['id']))
                
                except:

                    try:

                        l = self.bot.get_channel(mod.find_one({'_id':member.guild.id})['chatlogs'])

                        await l.send(f"{t['args']['error']['autorole']['notpermission']} {discord.utils.get(member.guild.roles, id = db['autorole']['id']).mention}")
                    
                    except:

                        try:

                            await member.guild.owner.send(f"{t['args']['error']['autorole']['notpermission']} ''{discord.utils.get(member.guild.roles, id = db['autorole']['id'])}'' {t['args']['error']['autorole']['notpermission2']}")

                        except:

                            await member.guild.text_channels[0].send(f"{t['args']['error']['autorole']['notpermission']} {discord.utils.get(member.guild.roles, id = db['autorole']['id']).mention} {t['args']['error']['autorole']['notpermission2']}")
        except:

            None
        
    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):

        t = await translate(message.guild)

        try:

            db = mod.find_one({'_id':message.guild.id})

            if db['ltxt']['True?'] == True:

                channel = self.bot.get_channel(db['ltxt']['id'])

                e = discord.Embed(

                description = f'{t["args"]["logs"]["message"]} {message.author.mention} {t["args"]["logs"]["message"]} {message.channel.mention}',

                color = 0xff0000

                )
                e.add_field(name = f'{t["args"]["logs"]["msg"]}:', value = f'{message.content}', inline=False)

                e.set_author(name = f'{message.author.name}#{message.author.discriminator}', icon_url = message.author.display_avatar)

                await channel.send(embed = e)
            
        except:

            None
    
    @commands.Cog.listener()
    async def on_message_edit(self, antes:discord.Message, depois:discord.Message):

        t = await translate(antes.guild)

        try:

            db = mod.find_one({'_id':antes.guild.id})

            if db['ltxt']['True?'] == True:

                channel = self.bot.get_channel(db['ltxt']['id'])

                e = discord.Embed(

                    description = f'{t["args"]["logs"]["message"]} {antes.author.mention} {t["args"]["logs"]["edit"]} {antes.channel.mention}',

                    color = 0xfff000

                )
                e.add_field(name = f'{t["args"]["logs"]["old"]}:', value = f'{antes.content}', inline=False)

                e.add_field(name = f'{t["args"]["logs"]["new"]}:', value =  f'{depois.content}', inline=False)

                e.set_author(name = f'{antes.author.name}#{antes.author.discriminator}', icon_url = antes.author.display_avatar)

                await channel.send(embed = e)
        
        except:

            None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member:discord.Member, antes:discord.VoiceState, depois:discord.VoiceState):

        if antes.channel != depois.channel:

            t = await translate(member.guild)

            try:

                db = mod.find_one({'_id':member.guild.id})

                if db['lvoice']['True?'] == True:

                    channel = self.bot.get_channel(db['lvoice']['id'])

                if antes.channel == None:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["enter"]} `{depois.channel}`',

                    color = 0x00ff19

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    await channel.send(embed = e)

                    return

                if depois.channel == None:

                    e = discord.Embed(

                    description = f'{member.mention} {t["args"]["logs"]["exit"]} `{antes.channel}`',

                    color = 0xff0000

                    )

                    e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                    await channel.send(embed = e)

                    return

                e = discord.Embed(

                description = t['args']['logs']['semove'].format(member.mention, antes.channel.mention, depois.channel.mention),

                color = 0xfff000

                )
                
                e.set_author(name = f'{member.name}#{member.discriminator}', icon_url = member.display_avatar)

                await channel.send(embed = e)

            except:

                None

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))