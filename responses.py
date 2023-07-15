from bot import username
import random

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == "name":
        return username

    if p_message == "hello":
        return "Hey there!"
    
    
    if p_message == "roll":
        return str(random.randint(1,6))
    
    if p_message == "help":
        return "This is a bot used to perform basic python operations \n Use '?' as prefix to send the output in your DM \n Use '!' as prefix to send the output in the channel"
    
    if p_message == "react":
        x = print("test")
        emoji = "\N{THUMBS UP SIGN}"
        return x.add_reaction("\:thumbsup:")
    
    