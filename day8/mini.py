import random
from datetime import datetime
from datetime import datetime

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
        # Respond to greetings
        greetings = ["hi", "hello", "hey"]
        if any(greet in user_input.lower() for greet in greetings):
            print("AI: Hello! How can I assist you today?")
            continue

        # Respond to asking for the time
        if "time" in user_input.lower():
            print("AI: The current time is", datetime.now().strftime("%H:%M:%S"))
            continue

        # Respond to asking for the date
        if "date" in user_input.lower():
            print("AI: Today's date is", datetime.now().strftime("%Y-%m-%d"))
            continue

        # Respond to asking for a joke
        if "joke" in user_input.lower():
            jokes = [
            "Why did the computer show up at work late? It had a hard drive!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the math book sad? Because it had too many problems."
            ]
            print("AI:", random.choice(jokes))
            continue

        print("AI:", basic_ai_response(user_input))