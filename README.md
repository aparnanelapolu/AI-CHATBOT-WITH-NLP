# AI-CHATBOT-WITH-NLP
**COMPANY NAME** :CODTECH IT SOLUTIONS

**NAME** :N.Hima Bindu Aparna

**INTERN ID** :CT08LGO

**DOMINE** : PYTHON

**BATCH DURATION** :January 10th, 2025 to February 10th, 2025.

**MENTOR NAME** :Neela Santhosh Kumar 

**output : https://github.com/aparnanelapolu/AI-CHATBOT-WITH-NLP**

**discription : This code implements a simple chatbot using Natural Language Processing (NLP) techniques in Python. It utilizes the nltk, scikit-learn, and random libraries to achieve the following:

1. Data Preprocessing:

Import necessary libraries: Imports nltk, random, numpy, and components from sklearn for text processing, machine learning, and randomization.
Download NLTK resources: Downloads necessary resources like 'punkt_tab', 'wordnet', and 'stopwords' using nltk.download.
Lemmatization: Initializes a WordNetLemmatizer to reduce words to their base form.
Intents Definition: Defines a dictionary intents containing different categories (tags) of user inputs (patterns) and corresponding bot responses.
Data Preparation: The preprocess_data function tokenizes, lemmatizes, and prepares training data from the intents dictionary.
2. Model Training:

Feature Extraction: Uses TfidfVectorizer to convert text into numerical vectors based on word frequency and importance.
Model Creation: Creates a pipeline using make_pipeline that combines the vectorizer and a MultinomialNB classifier (Naive Bayes).
Model Training: Trains the model using the prepared training data (sentences and labels).
3. Chatbot Interaction:

Message Classification: The classify_message function predicts the intent (tag) of a user's message using the trained model.
Response Retrieval: The get_response function retrieves a random response from the intents dictionary based on the predicted tag.
Chatbot Loop: The chatbot function initiates a conversation loop, prompting the user for input, classifying the message, and providing a response. The loop continues until the user types "exit".
In essence, the code creates a chatbot that:

Understands user input: Uses NLP techniques to process and understand the user's message.
Classifies intent: Predicts the category or intention behind the user's message.
Provides relevant responses: Selects an appropriate response based on the identified intent.
Engages in conversation: Continues the interaction until the user chooses to exit.**
