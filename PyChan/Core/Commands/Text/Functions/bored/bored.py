import discord
from discord.ext import commands
from Core.Decorators.decorators import Decorator

from requests import get

class BoredAPI(commands.Cog):

    def __init__(self, bot):
        """Constructor method
        """
        self.bot = bot

    @commands.command(
        pass_context=True,
        name="nudzesie",
        category="Tekst",
        help_={
            "title": "nudzesie",
            "description": "Wysyła losowe zadanie poboczne",
        },
    )
    @Decorator.pychan_decorator
    async def bored(self, ctx):

        url = "https://www.boredapi.com/api/activity/"  # from api to json
        response = get(url)
        dic = response.json()
        activity = str(dic["activity"])
        await ctx.send("Let's " + activity.lower())
