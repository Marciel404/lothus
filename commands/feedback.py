import discord

from discord.ext import commands
from discord import slash_command, option
from utils.defs import *

class feedback(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @slash_command(name = 'sugest', description = 'Envia uma sugestão para meu dono')
    @option(name = 'sugest', description = 'Escreva a sugestão')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sugest(self, ctx, *, sugestão):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        user = self.bot.get_channel(int(1012123748637343756))

        embed = discord.Embed(title = 'Sugest', 
        description = f'**Enviado por:** \n {ctx.author} \n\n **Sugestão:** \n {sugestão} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

        await ctx.respond(t['args']['feedback']['sugest'], ephemeral = True)

        await user.send(embed=embed)

    @slash_command(name = 'report_bug', description = 'Envia um report para meu dono')
    @option(name = 'report', description = 'Escreva o report')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def report(self, ctx, *, report):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)
        
        user = self.bot.get_channel(int(1012123813070262312))

        embed = discord.Embed(title = 'report', 
        description = f'**Enviado por:** \n {ctx.author} \n\n **Report:** \n {report} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

        await ctx.respond(t['args']['feedback']['report'], ephemeral = True)

        await user.send(embed=embed)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(feedback(bot))