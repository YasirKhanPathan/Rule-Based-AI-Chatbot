def chatbot(message):
    message = message.lower()

    if message in ["hello", "hi", "hey"]:
        return "Bot: Hi!"

    elif message == "how are you":
        return "Bot: I am fine. Thank you for asking."

    elif message == "name":
        return "Bot: My name is Decodebot."

    elif message == "help":
        return "Bot: You can say hello, ask my name, or say bye."
    
    elif message == "python":
        return "Bot: Python is a popular language for AI."
    
    elif message == "thanks":
        return "Bot: You're welcome!"

    elif message in ["bye", "quit", "exit"]:
        return "Bot: Goodbye!"
        
    else:
        return "Bot: Sorry, I don't understand."


print("=== Rule Based AI Chatbot ===")
print("Type 'bye' to exit.")

print("Welcome to the chatbot!")

while True:
    user_message = input("You: ")

    response = chatbot(user_message)

    print("Bot: " + response)

    if user_message.lower() in ["bye", "quit", "exit"]:
        break