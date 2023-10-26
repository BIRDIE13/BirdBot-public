import nextcord
from nextcord.ext import commands
from static import *
import asyncio

class TradeAndChillCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test_command')
    async def test_command(self, ctx: commands.Context):
        if ctx.guild.id == self.guild_id:
            await ctx.send('This is a test command!')

def setup(bot):
    bot.add_cog(TradeAndChillCog(bot))
