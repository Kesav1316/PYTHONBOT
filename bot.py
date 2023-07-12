import discord
import responses

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author) # Retrieves the author from the message
        user_message = str(message.content) # The command given by user
        channel = str(message.channel) #Retrieves the channel from the message

        print("{} said '{}' ({})".format(username , user_message , channel))

        # Setting prefix
        if user_message[0] == "?": #Sets prefix as "?"
            user_message = user_message[1:] # The message without prefix
            await send_message(message , user_message , is_private = True) # Here the variable message is the output given by bot and will be sent to the users DM
        else:
            await send_message(message , user_message , is_private = False) # Sends message in channel
    with open("E:\\BOT\\PYTHONBOT\\token.txt") as f:
        TOKEN = f.readline()
    client.run(TOKEN)

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