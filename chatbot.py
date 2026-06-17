def get_response(message):
    message = message.lower()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I am fine. Thank you for asking."

    elif message in ["what is your name", "who are you", "your name"]:
        return "My name is Decodebot."

    elif message == "help":
        return "You can say hello, ask my name, ask about python, or say bye."
    
    elif message == "python":
        return "Python is a popular language for AI."
    
    elif message == "thanks":
        return "You're welcome!"

    elif message in ["bye", "quit", "exit"]:
        return "Goodbye!"
        
    else:
        return "Sorry, I don't understand."


if __name__ == "__main__":
    print("=== Rule Based AI Chatbot ===")
    print("Type 'bye' to exit.")

    print("Welcome to the chatbot!")

    while True:
        user_message = input("You: ")

        response = get_response(user_message)

        print("Bot: " + response)

        if user_message.lower() in ["bye", "quit", "exit"]:
            break