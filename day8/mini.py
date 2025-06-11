import random

def basic_ai_response(user_input):
    responses = [
        "Hello! How can I help you?",
        "I'm an AI. Ask me anything!",
        "That's interesting. Tell me more.",
        "Sorry, I don't understand. Can you rephrase?",
        "Let's talk about something else."
    ]
    return random.choice(responses)

if __name__ == "__main__":
    print("Basic AI Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("AI:", basic_ai_response(user_input))