import discord
from discord.ext import commands
from Core.Commands.Science.Maths.Functions.maths_functions import *
from Core.Decorators.decorators import Decorator


class Ieee754x64(commands.Cog):
    """
    The class contains ieee754_64 method
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        pass_context=True,
        name="ieee754_64",
        category="Nauka",
        help_={
            "title": "IEEE754 64bit",
            "description": "Zamienia dowolną liczbę w systemie dziesiętnym w liczbę binarną przy użyciu zapisu liczby zmiennoprzecinkowej w standarcie IEEE754 64bit",
            "fields": [
                {
                    "name": "Składnia",
                    "value": "`ieee754_64 <liczba>`",
                }
            ],
        },
    )
    @Decorator.pychan_decorator
    async def ieee754_64(self, ctx, number: float):
        """
        Sends the reply message to the user

        :param ctx: The context in which a command is called
        :type ctx: discord.ext.commands.Context

        :param number: Number to change
        :type number: float
        """
        data = ieee754_64(str(number))
        embed = discord.Embed(
            title="IEEE 754/64BIT", description="", color=discord.Color.dark_purple()
        )
        embed.add_field(name="Sign", value=data[0], inline=False)
        embed.add_field(name="Exponent", value=data[1], inline=False)
        embed.add_field(name="Significand", value=data[2], inline=False)
        embed.add_field(name="IEEE 754/64BIT", value=data[3], inline=False)

        await ctx.send(embed=embed)
