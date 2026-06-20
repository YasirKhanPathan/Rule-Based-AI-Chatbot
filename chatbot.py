def get_response(message):
    message = message.lower()

    responses = []

    if message in ["hello", "hi", "hey"]:
        return """Hi! How can I help you?
I can explain programming languages such as Python, C++, Java, HTML, CSS, JavaScript, and C#."""

    #elif message == "how are you":
    if any(phrase in message for phrase in [
        "how are you",
        "what about you"
    ]):
        responses.append((message.find("how are you"), "I am fine. Thank you for asking."))

    #elif message in ["what is your name", "who are you", "your name"]:
    if any(phrase in message for phrase in [
        "name",
        "who are you",
        "your name"
    ]):
        responses.append((message.find("your name"), "My name is Decodebot."))

    if any(phrase in message for phrase in [
        "what can you do",
        "what do you do",
        "how can you help me",
        "help"
    ]):
        return """I can:
        • Explain Python
        • Explain C++
        • Explain Java
        • Explain HTML
        • Explain CSS
        • Explain JavaScript
        • Explain C#
        • Respond to greetings"""

    programming_languages = {
        "python" : "Python is an interpreted, high-level programming language used globally for artificial intelligence (AI), data science, web development, and task automation. It is designed for high code readability, utilizing a dynamically typed system and automatic memory management to simplify software development.",
        "c++" : "C++ is a compiled, high-level, multi-paradigm programming language used globally for game engines, operating systems, embedded systems, and high-frequency trading applications. It is designed with a focus on system programming and performance, offering low-level memory manipulation alongside high-level abstractions.",
        "java" : "Java is a compiled, object-oriented programming language designed around the 'Write Once, Run Anywhere' (WORA) principle, used globally for enterprise software, Android app development, and large-scale backend systems. It runs inside a virtual machine (JVM), making it highly secure, stable, and platform-independent.",
        "javaScript": "JavaScript is an interpreted, high-level programming language used globally to add interactivity to websites, build full-stack web applications, and power mobile apps. It is the only programming language capable of running natively inside modern web browsers, making it the backbone of the interactive web.",
        "c#" : "C# is a modern, object-oriented, compiled programming language developed by Microsoft, used globally for indie game development, enterprise Windows applications, and cloud-based web services. It operates primarily on the .NET framework, combining the raw power of C++ with the ease of use of Java.",
        "html" : "HTML is the standard markup language used globally to create and structure the skeleton of webpages. It uses a system of tags to define elements like headings, paragraphs, links, images, and tables, ensuring web browsers know how to display content.",
        "css" : "CSS is a style sheet language used globally to design, style, and lay out the visual appearance of webpages. It works directly alongside HTML to control colors, fonts, spacing, animations, and responsive designs that adapt to mobile and desktop screens."
    }
    
    if message == "thanks":
        return "You're welcome!"

    if message in ["bye", "quit", "exit"]:
        return "Goodbye!"
    
    for language, definition in programming_languages.items():
        if language in message:
            return definition
        
    if responses:
        responses.sort()
        return " ".join(response for _, response in responses)
    
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