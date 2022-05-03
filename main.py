import discord, os, json
from discord.ext import commands


with open("./database/configs.json", "r") as p:
    bot_prefix = json.load(p)

    prefix = bot_prefix["prefix"]

class MyBotUsingCogsSystem(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = prefix,
            case_insensitive = False,
            help_command = None, 
            intents = discord.Intents.all())
        self.synced = False

    async def on_ready(self):

        activity = discord.Game(name = "github/synthax-c")
        await client.change_presence(
        status = discord.Status.idle, activity = activity)
        
        print(f"{client.user.name} now is online.")

client = MyBotUsingCogsSystem()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[: - 3]}")

with open("./database/configs.json", "r") as token:
    bot_token = json.load(token)

    TOKEN = bot_token["token"]

client.run(TOKEN)
