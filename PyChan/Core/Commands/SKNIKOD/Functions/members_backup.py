import discord
from discord.ext import commands
import os


class MembersBackup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name='backupCzlonkow')
    async def members_backup(self, ctx):
        myfile = "listaCzlonkow.txt"
        message = await ctx.send(f'Trwa pobieranie czlonkow {1}/{len(ctx.guild.members)}')

        with open("listaCzlonkow.txt", "w", encoding='utf-8') as f:
            for i, member in enumerate(ctx.guild.members):
                await message.edit(content=f'Trwa pobieranie czlonkow {i}/{len(ctx.guild.members)}')

                if member.bot:
                    continue

                f.write(f'{member.display_name};{member.name};\n')

        await message.delete()
        with open("listaCzlonkow.txt", "rb") as file:
            await ctx.send(file=discord.File(file, "listaCzlonkow.txt"))

        os.remove('listaCzlonkow.txt')
