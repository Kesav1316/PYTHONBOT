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

        #Assigning details of user to a variable
        username = str(message.author)      # Retrieves the author from the message.
        user_message = str(message.content) # The command given by user.
        channel = str(message.channel)      # Retrieves the channel from the message.
        print("{} said '{}' ({})".format(username , user_message , channel)) # Prints the information in terminal
        
        #Writing the name of user in a file 
        with open("E:\\BOT\\PYTHONBOT\\idkigspfmig.txt" , "w") as f: 
            f.write(username) 
        
        #Sending player pfp
        with open("E:\\BOT\\PYTHONBOT\\url.txt" , "w") as f1:
            url = message.author.avatar.url  # Here url = "https://cdn.discordapp.com/avatars/580355433257107458/41a10abb44bf518433b60c917cfee6e2.png?size=1024" where the number is user id
            f1.write(url)

        '''with open("E:\\BOT\\PYTHONBOT\\embed.txt" , "w") as f2:
            if message.content.startswith('!hello'):
                embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
                embedVar.add_field(name="Field1", value="hi", inline=False)
                embedVar.add_field(name="Field2", value="hi2", inline=False)
                await message.channel.send(embed=embedVar)
                f2.write(embedVar)'''
        

        # Setting prefix
        if user_message[0] == "?":                                          # Sets prefix as "?".
            user_message = user_message[1:]                                 # The message without prefix using slicing.
            await send_message(message , user_message , is_private = True)  # Here the variable message given by bot will be sent to author DM.
        elif user_message[0] =="!":
            user_message = user_message[1:]
            await send_message(message , user_message , is_private = False) # Here the variable message given by bot will be sent in channel.

        
        # Responses from main file
        if user_message.startswith('hello'):
            embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
            embedVar.add_field(name="Field1", value="hi", inline=False)
            embedVar.add_field(name="Field2", value="hi2", inline=False)
            await message.channel.send(embed=embedVar)

        #To print avatar of user

        if user_message.startswith("url"):
            avatar = message.author.avatar.url
            await message.channel.send(avatar)
            x = avatar.split("=")
            if user_message == "url_128":
                size_128 = x 
                size_128[1] = "128" # Changes the size to 128
                size_128 = size_128[0] + size_128[1] # Converts the list of strings into a string 
                await message.channel.send(size_128)
            
            elif user_message == "url_256":
                size_256 = x 
                size_256[1] = "256" # Changes the size to 128
                size_256 = size_256[0] + size_256[1] # Converts the list of strings into a string 
                await message.channel.send(size_256)
            
            elif user_message == "url_512":
                size_512 = x 
                size_512[1] = "512" # Changes the size to 128
                size_512 = size_512[0] + size_512[1] # Converts the list of strings into a string 
                await message.channel.send(size_512)

        elif user_message == "name":
            await message.channel.send(username)

        elif user_message == "react":
            message = await message.channel.send("test")
            emoji = '\N{THUMBS UP SIGN}'
            await message.add_reaction(emoji)























   #Running using token

    with open("E:\\BOT\\PYTHONBOT\\token.txt") as f1:  # Opening the file token.txt in read.
        TOKEN = f1.readline()                          # Stores the first line from the file token.txt in the form of string.
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