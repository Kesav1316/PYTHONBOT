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

#   The parameters in the function header are as follows:
#1) message = The output which will be sent by bot.
#2) user_message = The message sent by user after the prefix.
#3) is_private = Ensures whether the message from bot will be sent in channel or to authot directly.

def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!') # Displays this message when the bot is turned on.
    
    @client.event
    async def on_message(message):
        if message.author == client.user:       # Prevents looping of bot messages when output is set the same as input.
            return

        username = str(message.author)      # Retrieves the author from the message.
        user_message = str(message.content) # The command given by user.
        channel = str(message.channel)      # Retrieves the channel from the message.

        print("{} said '{}' ({})".format(username , user_message , channel))

        # Setting prefix
        if user_message[0] == "?":                                          # Sets prefix as "?".
            user_message = user_message[1:]                                 # The message without prefix using slicing.
            await send_message(message , user_message , is_private = True)  # Here the variable message given by bot will be sent to author DM.
        elif user_message[0] =="!":
            user_message = user_message[1:]
            await send_message(message , user_message , is_private = False) # Here the variable message given by bot will be sent in channel.
   
    #Running using token
    with open("E:\\BOT\\PYTHONBOT\\token.txt") as f:  # Opening the file token.txt in read.
        TOKEN = f.readline()                          # Stores the first line from the file token.txt in the form of string.
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