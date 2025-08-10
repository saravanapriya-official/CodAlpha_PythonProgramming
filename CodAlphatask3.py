def get_bot_reply(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks for asking! 😊"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I'm not sure how to respond to that. 🤔"

def run_chatbot():
    print("🤖 Welcome to the Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = get_bot_reply(user_input)
        print("Bot:", reply)

        if user_input.lower() in ["bye", "goodbye", "exit"]:
            break

# Run the chatbot
run_chatbot()
