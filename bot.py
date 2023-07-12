import discord
import responses

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    with open("E:\\BOT\\PYTHONBOT\\token.txt") as f:
        TOKEN = f.readline()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author) # Retrieves the author from the message
        user_message = str(message.content) # Retrieves the content from the message
        channel = str(message.channel) #Retrieves the channel from the message

        print("{} said '{}' ({})".format(username , user_message , channel))

'''@client.command()   #To send in server
async def ping(ctx):
    await ctx.send("Pong") 

@client.command()   #To send to author
async def pong(ctx):
    await ctx.author.send("Pong") 

@client.command(aliases = ["hello"]) # Any string inside the list of aliases can be used after prefix
async def any(ctx , * , question): # * - space ; question - anything can be done
    await ctx.send("ok")

with open("E:\\BOT\\PYTHONBOT\\token.txt") as f:
    TOKEN = f.readline()

client.run(TOKEN)'''