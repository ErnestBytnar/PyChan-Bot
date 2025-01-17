import discord
from discord.ext import commands
from Core.Commands.Science.Maths.Functions.graphs_functions import *
import os


class Graphs(commands.Cog):
    def __init__(self, bot):
        """
        The class contains Graphs method
        """
        self.bot = bot

    @commands.command(
        pass_context=True,
        name="prufer",
        category="Nauka",
        help_={
            "title": "Prufer",
            "description": "Funkcja do rysowania drzewa z kodu Prüfera.",
            "fields": [
                {
                    "name": "Składnia",
                    "value": "`prufer <kod>`",
                },
            ],
        },
    )
    async def prufer(self, ctx, *, code):
        """
        Sends the reply message to the user with graph image

        :param ctx: The context in which a command is called
        :type ctx: discord.ext.commands.Context

        :param code: Tree Prufer code
        :type code: string

        :raises commands.errors.BadArgument: User entered wrong arguments
        """
        # convert code string to list
        code = code.strip().split(",")
        for i in range(len(code)):
            try:
                code[i] = int(code[i])
            except ValueError:
                raise discord.ext.commands.BadArgument
        # generate graph and send it to user
        tree = tree_from_prufer(code.copy())
        if tree is not None:
            nx.draw(
                tree,
                with_labels=True,
                font_weight="bold",
                font_size=16,
                width=3,
                node_color="#e530e8",
                node_size=800,
            )
            plt.savefig("tree.png")
            plt.clf()
            file = discord.File("tree.png")
            embed = discord.Embed(
                title="Drzewo z kodu Prüfera:",
                description=f"```{code}```",
                color=discord.Color.dark_purple(),
            )
            embed.set_image(url="attachment://tree.png")
            await ctx.send(file=file, embed=embed)
            # remove temp file
            os.remove("tree.png")
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="Niepoprawny Kod Prüfera!",
                    description="Kod zawiera liczbę większą niż długość kodu + 2.",
                    color=discord.Color.dark_purple(),
                )
            )

    @commands.group(
        invoke_without_command=True,
        pass_context=True,
        name="graf",
        aliases=["g"],
        category="Nauka",
        help_={
            "title": "Graf",
            "description": "Funkcja do rysowania grafów nieskierowanych.",
            "fields": [
                {
                    "name": "Składnia",
                    "value": "`graf rysuj [lista wierzchołków] [lista krawędzi]` - wyświetla informacje o permutacji.",
                },
                {
                    "name": "Aliasy komendy",
                    "value": "`graf`, `g`",
                },
                {
                    "name": "Dodatkowe informacje",
                    "value": "W liście wierzchołków nie trzeba uwzględniać tych, które są wymienione w liście krawędzi.\nPrzykład użycia: `g rysuj [] [(1,2)(1,3)(2,3)]` - generuje graf pełny K3",
                },
            ],
        },
    )
    async def graf(self, ctx):
        """
        Sends the reply message to the user with supported graphs functions

        :param ctx: The context in which a command is called
        :type ctx: discord.ext.commands.Context
        """
        await ctx.send(
            embed=discord.Embed(
                title="Wspierane polecenia to ```^g rysuj```. Więcej informacji pod ```^help graf```",
                color=discord.Color.dark_purple(),
            )
        )

    @graf.command(name="rysuj")
    async def rysuj(self, ctx, *, args):
        """
        Sends the reply message to the user with graph image

        :param ctx: The context in which a command is called
        :type ctx: discord.ext.commands.Context

        :param args: List of vertices and edges as string
        :type args: string
        """
        args = args.replace(" ", "").replace("[", "").split("]")

        if len(args) < 3:
            await ctx.send(
                embed=discord.Embed(
                    title="Musisz podać 2 parametry",
                    description="Aby uzyskać pomoc wpisz `^help graf`",
                    color=discord.Color.dark_purple(),
                )
            )
            return

        # create lists from string input
        if len(args[0]) == 0:
            vertices = None
        else:
            vertices = args[0].split(",")

        if len(args[1]) == 0:
            edges = None
        else:
            edges = args[1].rstrip(")").replace("(", "").split(")")
            edges = [n.lstrip(",").split(",") for n in edges]

        # get tree and send it
        tree = create_tree(vertices, edges)
        if tree is not None:
            nx.draw(
                tree,
                with_labels=True,
                font_weight="bold",
                font_size=16,
                width=3,
                node_color="#e530e8",
                node_size=800,
            )
            plt.savefig("graph.png")
            plt.clf()
            file = discord.File("graph.png")
            embed = discord.Embed(
                title="Graf nieskierowany:",
                description=f"",
                color=discord.Color.dark_purple(),
            )
            embed.set_image(url="attachment://graph.png")
            await ctx.send(file=file, embed=embed)
            # remove temp file
            os.remove("graph.png")
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="Błędny zapis listy wierzchołków lub/i krawędzi",
                    description="Aby uzyskać pomoc wpisz `^help graf`",
                    color=discord.Color.dark_purple(),
                )
            )
