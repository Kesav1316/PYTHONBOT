import random

def handle_response(message) -> str:
    p_message = message.lower()

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
    
    # Reading username from a file
    if p_message == "name":
        with open("E:\\BOT\\PYTHONBOT\\idkigspfmig.txt") as f:
            s = f.read()
            return s
    
    # To print avatar url of user
    if p_message.startswith("url"):
        with open("E:\\BOT\\PYTHONBOT\\url.txt") as f1:
            z = f1.read()
            x = z.split("=") # Returns a list with strings seperated by seperator
            if p_message == "url_128":
                size_128 = x 
                size_128[1] = "128" # Changes the size to 128
                size_128 = size_128[0] + size_128[1] # Converts the list of strings into a string 
                return size_128
            
            elif p_message == "url_256":
                size_256 = x 
                size_256[1] = "256" # Changes the size to 128
                size_256 = size_256[0] + size_256[1] # Converts the list of strings into a string 
                return size_256
            
            elif p_message == "url_512":
                size_512 = x 
                size_512[1] = "512" # Changes the size to 128
                size_512 = size_512[0] + size_512[1] # Converts the list of strings into a string 
                return size_512
            
            else:
                return z
    