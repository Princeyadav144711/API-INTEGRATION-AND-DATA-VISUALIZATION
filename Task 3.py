import nltk
from nltk.chat.util import Chat, reflections

# Define pairs: list of (pattern, response) pairs
pairs = [
    [ r"hi|hello|hey", ["Hello! Welcome to the Python chatbot!", "Hi there! How can I help you with Python today?"] ],
    [ r"how are you", ["I'm doing well, thanks for asking! I'm here to help with any Python-related questions you may have."] ],
    [ r"what is ai", ["AI stands for Artificial Intelligence, which refers to the development of computer systems that can perform tasks that typically require human intelligence."] ],
    [ r"what is machine learning", ["Machine learning is a subset of AI that involves training algorithms to learn from data and make predictions or decisions."] ],
    [ r"what is deep learning", ["Deep learning is a type of machine learning that uses neural networks with multiple layers to analyze data."] ],
    [ r"who created you", ["I was created using NLTK and Python."] ],
    [ r"what can you do", ["I can answer questions about AI, machine learning, and deep learning."] ],
    [ r"quit", ["Goodbye!"] ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("Welcome to the AI chatbot! Type 'quit' to exit.")
chatbot.converse()