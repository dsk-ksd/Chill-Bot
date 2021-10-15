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

    await client.process_commands(message)

    #to reply to some specific messages sent by users
    if (message.content()).lower() == "hello there" : print("General Kenobi!")
    if (message.content()).lower() == "understandable" : print("Have a nice day!")
    if (message.content()).lower() == "dhruv" : print("You mean Supreme Leader Signor Fuhrer Thalapathy Dhruv Sama")
    if (message.content()).lower() == "naruto" : print("SASUKE!")
    if (message.content()).lower() == "69" : print("nice ( ͡° ͜ʖ ͡°)")


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")


# running the bot
client.run("ODk4NTcwMzU0OTA0MTU0MTYy.YWmI2w.NZtpa5f83RJrJouULNytn9bynEU")
