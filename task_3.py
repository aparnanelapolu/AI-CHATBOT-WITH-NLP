# -*- coding: utf-8 -*-
"""Task 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sptw76E6w7QPXTCuiMDUgpHJQQYa0ytk
"""

import nltk
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from nltk.stem import WordNetLemmatizer


nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')


lemmatizer = WordNetLemmatizer()


intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hello", "How are you?", "Hey", "Howdy"],
            "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "Goodbye", "See you", "Later"],
            "responses": ["Goodbye!", "See you later!", "Bye!", "Take care!"]
        },
        {
            "tag": "thanks",
            "patterns": ["Thanks", "Thank you", "Thank you so much"],
            "responses": ["You're welcome!", "Anytime!", "Glad to help!"]
        },
        {
            "tag": "about",
            "patterns": ["What is your name?", "Who are you?", "Tell me about yourself"],
            "responses": ["I am a chatbot created to help you!", "I am an AI assistant created to chat with you."]
        }
    ]
}


def preprocess_data(intents):
    training_sentences = []
    training_labels = []
    labels = []

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            training_sentences.append(" ".join([lemmatizer.lemmatize(w.lower()) for w in word_list]))
            training_labels.append(intent['tag'])
        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    return training_sentences, training_labels, labels


training_sentences, training_labels, labels = preprocess_data(intents)


vectorizer = TfidfVectorizer()
model = make_pipeline(vectorizer, MultinomialNB())
model.fit(training_sentences, training_labels)


def classify_message(message):
    return model.predict([message])[0]
def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])


def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        message = input("You: ")

        if message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break


        tag = classify_message(message.lower())


        response = get_response(tag)
        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot()