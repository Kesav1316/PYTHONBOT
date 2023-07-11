import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?" , intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Success: Bot is connected to discord")

'''@client.command()   #To send in server
async def ping(ctx):
    await ctx.send("Pong") 

@client.command()   #To send to author
async def pong(ctx):
    await ctx.author.send("Pong") 

@client.command(aliases = ["hello"]) # Any string inside the list of aliases can be used after prefix
async def any(ctx , * , question): # * - space ; question - anything can be done
    await ctx.send("ok")'''

with open("E:\\BOT\\PYTHON BOT\\token.txt") as f:
    TOKEN = f.readline()

client.run(TOKEN)