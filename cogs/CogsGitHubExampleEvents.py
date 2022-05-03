import discord
from discord.ext import commands
from main import prefix

class CogsGitHubExampleEventsBySynthax(commands.cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f"<@{self.user.id}>":
            await message.reply("Meu prefixo nesse servidor é: ` {prefix} ` !")

def setup(client):
    client.add_cog(CogsGitHubExampleEventsBySynthax(client))
