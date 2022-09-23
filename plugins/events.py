import discord

from discord.ext import commands
from db.moderation import *
from utils.defs import *

class events(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):

        await lang('lang', 'en-us', guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild:discord.Guild):

        mod.find_one_and_delete({'_id':guild.id})

    @commands.Cog.listener()
    async def on_member_ban(self, guild:discord.Guild, user:discord.User):

        if (advdb.count_documents({ "_id": f'{guild.id}_{user.id}'}) == 1):

            advdb.find_one_and_delete({"_id": f'{guild.id}_{user.id}'})

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        try:

            db = mod.find_one({'_id':member.guild.id})

            if db['autorole']['True?'] == True:

                try:

                    await member.add_roles(discord.utils.get(member.guild.roles, id = db['autorole']['id']))
                
                except:

                    t = translates(member.guild)

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
            
def setup(bot:commands.Bot):
    bot.add_cog(events(bot))