import discord,random

from discord.ext import commands
from discord import slash_command, option
from utils.defs import *
from classes.buttons import *
from db.economy import *

class economia(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(
        name = 'roll', 
        description = 'You can win from 0 to 2000 lothcoins',
        guild_only = True,
        name_localizations = {
            'en-US': 'roll',
            'en-GB': 'roll',
            'es-ES': 'rodar',
            'pt-BR': 'rolar',
            'fr': 'rouler'
        },
        description_localizations = {
            'en-US': 'You can win from 0 to 2000 lothcoins',
            'en-GB': 'You can win from 0 to 2000 lothcoins',
            'es-ES': 'Puedes ganar de 0 a 2000 lothcoins',
            'pt-BR': 'Voce pode ganhar de 0 a 2000 lothcoins',
            'fr': 'Vous pouvez gagner de 0 à 2000 lothcoins'
        })
    @commands.cooldown(5, 7200, commands.BucketType.user)
    async def rolar(self, ctx):

        t = await translate(ctx.guild)

        rand = random.randint(0,10)

        if rand == 10:

            await update_bank(ctx.author, + 2000)

            await ctx.respond(f'Parabens {ctx.author.name}, {t["args"]["gan"]} 2000 LothCoins')

        elif rand == 8 or 9:

            r = random.randint(100,900)

            await update_bank(ctx.author,r)

            await ctx.respond(f'{ctx.author.name}, {t["args"]["gan"]} {r} LothCoins')

        elif rand == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7:

            r = random.randint(0,100)         

            await update_bank(ctx.author, + r)

            await ctx.respond(f'{ctx.author.name}, {t["args"]["gan"]} {r} LothCoins')

    @slash_command(
        name = 'lothcoins',
        description = 'Mostra quantas LothCoins uma pessoa tem',
        guild_only = True,
        name_localizations = {
            'en-US': 'wallet',
            'en-GB': 'wallet',
            'es-ES': 'cartera',
            'pt-BR': 'carteira',
            'fr': 'portefeuille'
        },
        description_localizations = {
            'en-US': 'Shows how many lothcoins you have or from the mentioned member',
            'en-GB': 'Shows how many lothcoins you have or from the mentioned member',
            'es-ES': 'Muestra cuántos lothcoins tienes o del miembro mencionado',
            'pt-BR': 'Mostra quantos lothcoins você tem ou do membro mencionado',
            'fr': 'Montre combien de lothcoins vous avez ou du membre mentionné'
        })
    @option(name = 'member', description = 'Escolha um membro')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def LOTHCOINS(self, ctx, member: discord.Member = None):

        t = await translate(ctx.guild)
            
        if member == None:

            member = ctx.author

        if member.bot:

            ctx.respond(t['args']['economy']['botacount'], ephemeral = True)

            return

        if bank.count_documents({"_id": member.id}) == 0:

            await update_bank(member,0)

        bal = bank.find_one({"_id": member.id})
        
        em = discord.Embed(title = f"{member.name} LothCoins", color = discord.Color.red())

        em.add_field(name ='LothCoin', value = bal["LOTHCOINS"])

        await ctx.respond(embed = em)

    @slash_command(
        name = 'transfer',
        description = 'Transfer LothCoins for outher member',
        guild_only = True,
        name_localizations = {
            'en-US': 'transfer',
            'en-GB': 'transfer',
            'es-ES': 'transferir',
            'pt-BR': 'transferir',
            'fr': 'trasférer'
        },
        description_localizations = {
            'en-US': 'You can transfer lothcoins to other people',
            'en-GB': 'You can transfer lothcoins to other people',
            'es-ES': 'Puedes transferir lothcoins a otras personas',
            'pt-BR': 'Trafere lothcoins para um membro',
            'fr': "Vous pouvez transférer des lothcoins à d'autres personnes"
        })
    @option(name = 'member', description = 'Ecolha o membro a transferir')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Transferir(self, ctx, member: discord.Member, lothcoins: int):

        t = await translate(ctx.guild)

        if member.bot:

            await ctx.respond(t['args']['economy']['bottransfer'], ephemeral = True)

            return
        
        if member == ctx.author:

            await ctx.respond(t['args']['economy']['notself'], ephemeral = True)

            return

        if bank.count_documents({"_id": member.id}) == 0:

            await update_bank(member,0)

        if bank.count_documents({"_id": ctx.author.id}) == 0:

            await update_bank(ctx.author,0)

        bal = bank.find_one({"_id": ctx.author.id})

        b1 = bal["LOTHCOINS"]

        if lothcoins > b1:

            await ctx.respond(t['args']['economy']['notmoney'], ephemeral = True)

            return

        elif lothcoins == 0:

            await ctx.respond(t['args']['economy']['>0'], ephemeral = True)

            return

        elif lothcoins < 0:

            await ctx.respond(t['args']['economy']['<0'], ephemeral = True)

            return

        await update_bank(ctx.author,- lothcoins)

        await update_bank(member,+ lothcoins)

        await ctx.respond(t['args']['economy']['vct'].format(lothcoins,member.mention))

    @slash_command(
        name = 'slot_machine',
        description = 'Slot machine bet',
        guild_only = True,
        name_localizations = {
            'en-US': 'slot_machine',
            'en-GB': 'slot_machine',
            'es-ES': 'tragamonedas',
            'pt-BR': 'caça-niquel',
            'fr': 'machine_à_sous'
        },
        description_localizations = {
            'en-US': 'Slot machine bet',
            'en-GB': 'Slot machine bet',
            'es-ES': 'Apuesta de tragamonedas',
            'pt-BR': 'Aposta no caça-niquel',
            'fr': "Pari de machine à sous"
        })
    @option(name = 'lothcoins', description = 'Escolha a quantidade a jogar')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loteria(self, ctx, lothcoins:int):

        t = await translate(ctx.guild)
            
        if bank.count_documents({"_id": ctx.author.id}) == 0:

            await update_bank(ctx.author,0)

        bal = bank.find_one({"_id": ctx.author.id})

        if lothcoins > bal["LOTHCOINS"]:

            await ctx.respond(t['args']['economy']['notmoney'], ephemeral = True)

            return

        elif lothcoins == 0:

            await ctx.respond(t['args']['economy']['>0'], ephemeral = True)
        
            return

        elif lothcoins < 0:

            await ctx.respond(t['args']['economy']['<0'], ephemeral = True)

            return

        final = []

        for i in range(3):

            a = random.choice([':pineapple:',':grapes:',':kiwi:',])

            final.append(a)

        await ctx.respond(str(final))

        if final[0] == final[1] == final[2]:

            await update_bank(ctx.author,4*lothcoins)

            await ctx.respond(f'{t["args"]["gan"]} {4*lothcoins} LOTHCOINS!!')

        else:

            await update_bank(ctx.author,-1*lothcoins)

            await ctx.respond( t['args']['economy']['lost'] + f' {lothcoins} LothCoins', ephemeral = True)

    @slash_command(
        name = 'lothcoins_top', 
        description = 'Shows the rank of richest people', 
        guild_only = True,
        description_localizations = {
            'en-US': 'Shows the rank of richest people',
            'en-GB': 'Shows the rank of richest people',
            'es-ES': 'Muestra el rango de las personas más ricas',
            'pt-BR': 'Mostra o rank de pessoas mais ricas',
            'fr': "Affiche le rang des personnes les plus riches"
        })
    @commands.cooldown(1,5, commands.BucketType.user)
    async def LOTHCOINSTOP(self, ctx):

        t = await translate(ctx.guild)

        rankings = bank.find().sort("LOTHCOINS",-1)

        i=1

        embed = discord.Embed(title = f"***{t['args']['economy']['top']}***")

        for x in rankings:

            loth = x["LOTHCOINS"]

            embed.add_field(name=f"{i}: {x['Nome']}", value=f"{loth}", inline=False)

            if i == 10:

                break

            else:

                i += 1

        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon}")

        await ctx.respond(embed=embed)

    @rolar.error
    async def error(self, ctx, error):

        t = await translate(ctx.guild)

        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

            if cd == 0:

                cd = 1

            await ctx.respond(f':x: || {t["args"]["mod"]["cooldown"].format(better_time(cd))}', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))