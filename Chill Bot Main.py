# importing necessary libraries
import discord
from discord.ext import commands


# initializing bot prefix
client = commands.Bot(command_prefix = "-")


# checking if bot is online
@client.event
async def on_ready():
    print("I am ready")


# checking messages
@client.event
async def on_message(message):

    # if a user replies to chill bot, chill bot will reply with "Fug off"
    if message.reference and message.author.id != 898570354904154162:
        for mention in message.mentions:
            if mention.id == 898570354904154162:
                await message.channel.send(
                    content="Fug off",
                    reference=message
                )

    await client.process_commands(message)


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")


# running the bot
client.run("ODk4NTcwMzU0OTA0MTU0MTYy.YWmI2w.lbLAofc_SPHmcy1VcS1Erta7-Yg")
