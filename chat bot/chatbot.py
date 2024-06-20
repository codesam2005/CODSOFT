def chatbot_response(user_input):
    user_input = user_input.lower()


    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"

    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How can I help you?"

    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"

    elif 'your name' in user_input:
        return "I'm a simple chatbot created to assist you with basic queries."
    elif 'what can you do' in user_input:
        return "I can respond to simple greetings and questions. Try asking me something!"

    elif 'help' in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"

    elif 'time' in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')
        return f"The current time is {current_time}."

    elif 'joke' in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif 'weather' in user_input:
        return "I can't provide real-time weather updates, but you can check your favorite weather app!"

    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"


def main():
    print("Welcome to the chatbot! You can try the following commands:")
    print(" - Hello or Hi")
    print(" - How are you")
    print(" - What is your name")
    print(" - What can you do")
    print(" - Help")
    print(" - What time is it")
    print(" - Tell me a joke")
    print(" - What's the weather like")
    print(" - Goodbye or Bye")

    while True:
        user_input = input("\nYou: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
            break


if __name__ == "__main__":
    main()
