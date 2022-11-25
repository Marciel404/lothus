import discord

from discord.ext import commands
from discord import slash_command
from funcs.checks import NoVote, vote
from funcs.defs import translates
from funcs.videos import *

class videos(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @slash_command(name = 'lula_maromba', description = 'Um meme do lula maromba')
    @vote()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def lulamaromba(self, interaction:discord.Interaction, member: discord.Member = None):

        t = translates(interaction.guild)

        if member == None: member = interaction.user
            
        await member.display_avatar.replace(size = 128).save('./videos/img/membro.png')
        await interaction.response.send_message(t['args']['lulamaromba']['preparevideo'])
        await lulamaromba('./videos/img/membro.png')
        await interaction.channel.send(content = t['args']['lulamaromba']['herevideo'].format(interaction.user.mention),
        file = discord.File('./videos/save/lulamaromba.mp4'))

    @lulamaromba.error
    async def error(self, ctx: discord.Interaction, error):

        if isinstance(error, NoVote):
            await ctx.response.send_message(error, ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(videos(bot))