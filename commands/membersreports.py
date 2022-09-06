import discord, requests

from discord.ext import commands
from discord import slash_command, option
from db.moderation import *
from utils.defs import *

class membersreport(commands.Cog):

    def __init__(self, bot:commands.Bot):
        
        self.bot = bot

    @slash_command(name = 'warns', description = 'Mostra as advs de um membro')
    @option(name = 'membro', description = 'Escolha o membro a remover a advertencia')
    async def veradv(self, ctx, member: discord.Member):

        if ctx.guild == None:
            
            return

        t = await translate(ctx.guild)

        o = requests.get(headers = {"Authorization": configData['topauth']},url = f'https://top.gg/api/bots/1012121641947517068/check?userId={ctx.author.id}')

        if o.json()['voted'] == 1:

            try:

                if advdb.count_documents({ "_id":f'{ctx.guild.id}_{member.id}'}) == 1:

                    rankings = advdb.find_one({'_id': f'{ctx.guild.id}_{member.id}'})

                    embed = discord.Embed(title = f"***{member.name}***")

                    i = 1

                    while True:

                        hgc = rankings[f'{t["args"]["adv"]}{i}']

                        embed.add_field(name=f"{t['args']['adv']}{i}", value=t["args"]["mod"]["logadv"].format(hgc[0],hgc[1],hgc[2]), inline=False)

                        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon}")

                        if i == advdb.find_one({'_id': f'{ctx.guild.id}_{member.id}'})['qnt']:

                            break

                        else:

                            i += 1

                    await ctx.respond(embed=embed)

                else: 

                    await ctx.respond(t['args']['notadv'], ephemeral = True)
                    
            except: 

                await ctx.respond(t['args']['notadv'], ephemeral = True)

        else:

            await ctx.respond(t['args']['notvote'])
            
def setup(bot:commands.Bot):
    bot.add_cog(membersreport(bot))