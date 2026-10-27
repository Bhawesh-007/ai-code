import re
from datetime import datetime

def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")
    while True:
        user = input("You: ").lower().strip()
        if re.search(r"\b(hi|hello|hey)\b", user):
            print("Bot: Hello! How can I help you today?")
        elif re.search(r"\bhow are you\b", user):
            print("Bot: I'm doing great! Thanks for asking.")
        elif re.search(r"\b(your name|who are you)\b", user):
            print("Bot: I am a simple rule-based chatbot.")
        elif re.search(r"\bhelp\b", user):
            print("Bot: I can answer simple questions like greetings, my name, date, and time.")
        elif re.search(r"\bdate\b", user):
            print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))
        elif re.search(r"\btime\b", user):
            print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))
        elif re.search(r"\b(thank you|thanks)\b", user):
            print("Bot: You're welcome!")
        elif re.search(r"\b(bye|exit|quit)\b", user):
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Please try another question.")

chatbot()