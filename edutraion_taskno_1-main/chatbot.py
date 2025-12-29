# chatbot.py

import re

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"

    # Asking for name
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I'm a simple chatbot created to help you."

    # Asking about weather
    elif re.search(r'\b(weather|temperature|forecast)\b', user_input):
        return "I can't check real-time weather, but it's always a good idea to carry an umbrella!"

    # Time-related questions
    elif re.search(r'\b(time|clock|current time)\b', user_input):
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Date-related questions
    elif re.search(r'\b(date|day|today)\b', user_input):
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # Simple arithmetic
    elif re.search(r'\b(\d+)\s*[\+\-\*/]\s*(\d+)\b', user_input):
        try:
            result = eval(user_input)
            return f"The answer is {result}."
        except:
            return "Sorry, I couldn't calculate that."

    # Thanks
    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome!"

    # Goodbye
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"

    # Default response
    else:
        return "I'm not sure how to answer that yet. Can you ask something else?"

# Conversation loop
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("ChatBot:", response)
    if 'bye' in user_input.lower():
        break
input("\nChat ended.Press Enter to exit...")  # Prevents auto-closing