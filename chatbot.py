print("=== Rule Based AI Chatbot ===")
print("Type 'bye' to exit.")

print("Welcome to the chatbot!")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hi!")

    elif message == "how are you":
        print("Bot: I am fine.")

    elif message == "name":
        print("Bot: I am a Chatbot.")

    elif message == "help":
        print("Bot: Try saying hello or asking my name.")

    elif message == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")