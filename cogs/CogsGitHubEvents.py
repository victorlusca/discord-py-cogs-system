import discord, json
from discord.ext import commands

class CogsGitHubEventsBySynthax(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        with open("./database/configs.json", "r") as p:
            bot_prefix = json.load(p)

            prefix = bot_prefix["prefix"]

        if message.content == f"<@{self.client.user.id}>":
            await message.reply(f"**Meu prefixo nesse servidor é: ` {prefix} `**")

def setup(client):
    client.add_cog(CogsGitHubEventsBySynthax(client))
