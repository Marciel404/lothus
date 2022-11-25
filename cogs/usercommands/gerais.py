import discord, hexacolors

from discord.ext import commands
from funcs.defs import translates
from db.moderation import mod
from db.economy import dbeconomy, bank

class usergerais(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @commands.user_command(
        guild_only = True,
        name = 'user_info'
    )
    async def userinfo(self, ctx: discord.Interaction, member:discord.Member):

        idemoji = self.bot.get_emoji(1045112581062393946)
        roleemoji = self.bot.get_emoji(1045369720666333224)
        dolaremoji = self.bot.get_emoji(1045370164306247811)
        inviteemoji = self.bot.get_emoji(1044747249378414612)

        t = translates(ctx.guild)

        dbeconomy.update_bank(member,0)

        user = bank.find_one({"_id": member.id})

        embed = discord.Embed(colour=hexacolors.string('indigo'))

        embed.set_author(name=f"User Info - {member}"),

        embed.set_thumbnail(url=member.display_avatar),

        if mod.find_one({'_id':ctx.guild.id})['lang'] != 'pt-br':

            membercreate = member.created_at.strftime(f"%Y %m %d")

            memberjoin = member.joined_at.strftime(f"%Y %m %d")

        else:

            membercreate = member.created_at.strftime(f"%d %m %Y")

            memberjoin = member.joined_at.strftime(f"%d %m %Y")

        embed.add_field(name = f'{idemoji}{t["args"]["ui"]["name"]}:',
        value = member.display_name, inline = True)
        embed.add_field(name = f'{idemoji}ID:', value = member.id, inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f'📅{t["args"]["ui"]["cc"]}:', value = membercreate, inline = True)
        embed.add_field(name = f'{inviteemoji}{t["args"]["ui"]["js"]}:', value = memberjoin, inline = True)

        embed.add_field(name = '════════════', value = '════════════', inline = False)

        embed.add_field(name = f'{roleemoji}{t["args"]["ui"]["toprole"]}:', value = member.top_role.mention, inline = True)
        embed.add_field(name = f'{dolaremoji}LothCoins', value = user["LOTHCOINS"], inline = True)

        await ctx.response.send_message(embed=embed, ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(usergerais(bot))