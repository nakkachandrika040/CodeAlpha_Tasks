def get_response(user_input):
    """
    Returns a response based on user input.
    """

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple Python chatbot."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that."


def chatbot():
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_message = input("You: ")

        response = get_response(user_message)

        print("Bot:", response)

        if user_message.lower().strip() == "bye":
            break


# Start the chatbot
chatbot()