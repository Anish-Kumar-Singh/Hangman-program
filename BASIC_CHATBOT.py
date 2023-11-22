#Create a text-based chatbot that can have conversations with users. You can use natural language processing libraries like NLTK or spaCy to make your chatbot more conversational.
import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
   (r'hi|hello|hey', ['Hello!', 'Hi there!']),
    (r'how are you', ['I am just a computer program, so I do not have feelings, but thanks for asking!']),
    (r'what is your name', ["I'm called ChatBot. How can I assist you today?"]),
    (r'who are you', ["I'm a chatbot created with NLTK."]),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!']),
    (r'my name is (.*)', ['Nice to meet you, {}!']),
    (r'motivate me', ["Embrace the power of small steps; progress, no matter how modest, is a victory."]),
]

# Create a chatbot using the patterns 
chatbot = Chat(patterns, reflections)

# Start the conversation loop
print("Hello! I'm ChatBot. Ask me anything or type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("ChatBot: Bye! Take care.")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)