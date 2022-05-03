import discord
from discord.ext import commands

class CogsGitHubExampleCommandsBySynthax(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, message):
        latency = round(self.latency * 1000)

        send_message = await message.reply("Cauculando...")
        await send_message.edit(content = f"Meu ping atual é: {latency}ms")

def setup(client):
    client.add_cog(CogsGitHubExampleCommandsBySynthax(client))
