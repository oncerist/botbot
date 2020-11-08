from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(ctx):
        await ctx.send('Hi pakyu')


def setup(bot):
    bot.add_cog(Test(bot))
