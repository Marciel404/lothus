import discord, requests

from discord.ext import commands
from discord import slash_command
from db.economy import update_bank
from utils.configs import configData

class dono(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'givelothcoins',guild_ids = [929181582571503658])
    async def SetM(self,ctx, id,dindin: int):

        user = self.bot.get_user(id)

        await update_bank(user, + dindin)

        try:

            await user.send(f'Seus {dindin} LothCoins foram setados <@{id}>')

            await ctx.send(f'Foram dados {dindin} LothCoins para <@{id}>')

        except:

            await ctx.send(f'Foram dados {dindin} LothCoins para <@{id}>')

    @slash_command(name = 'removelothcoins',guild_ids = [929181582571503658])
    async def RmvM(self,ctx, id: int, dindin: int):

        user = self.bot.get_user(id)
            
        await ctx.send(f'Foram removidos {dindin} LothCoins para <@{id}>')

        await update_bank(user, - dindin)

    @slash_command(name = 'stats', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stats(self, ctx, bot):
        
        if bot == 'lthc':

            bot = 1010629199159107665
        
        elif bot == 'lth':

            bot = 1012121641947517068

        res = requests.get(f'https://api.squarecloud.app/v1/public/status/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        embed = discord.Embed()

        embed.add_field(name = 'HOST', value = f'<@{bot}>')
        embed.add_field(name = 'CPU', value = res['response']['cpu'])
        embed.add_field(name = 'RAM', value = res['response']['ram'])
        embed.add_field(name = 'SSD', value = res['response']['storage'])
        embed.add_field(name = 'NETWORK', value = res['response']['network'])
        embed.add_field(name = 'REQUESTS', value = res['response']['requests'])

        await ctx.respond(embed = embed)

    @slash_command(name = 'backup', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def backup(self, ctx):

        res = requests.get(f'https://api.squarecloud.app/v1/public/backup/{self.bot.user.id}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.author.send(res['response']['downloadURL'])

    @slash_command(name = 'init', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def init(self, ctx, bot):

        if bot == 'lthc':

            bot = 1010629199159107665
        
        elif bot == 'lth':

            bot = 1012121641947517068

        requests.post(f'https://api.squarecloud.app/v1/public/start/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.author.send(f'{bot} iniciado')

    @slash_command(name = 'stop', guild_ids = [929181582571503658])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stop(self, ctx, bot):

        if bot == 'lthc':

            bot = 1010629199159107665
        
        elif bot == 'lth':

            bot = 1012121641947517068

        requests.post(f'https://api.squarecloud.app/v1/public/stop/{bot}', headers = {'Authorization': configData['squarekey']}).json()

        await ctx.author.send(f'{bot} iniciado')

def setup(bot:commands.Bot):
    bot.add_cog(dono(bot))