import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 
                      
                 # college quary chatbot 


nltk.download('punkt_tab')
# Load intents
with open('intents.json') as f:
    intents = json.load(f)

# Prepare training data
corpus = []
labels = []
classes = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])
    if intent['tag'] not in classes:
        classes.append(intent['tag'])

Vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize,token_pattern=None)
X = Vectorizer.fit_transform(corpus)    # transfrom the row text into matrix and fit 
y = np.array(labels)

# train model 
model = MultinomialNB()
model.fit(X,y) 

#predict intent

def predict_intent(text) :    # take a list as a input and return the tag name 
    text_vector = Vectorizer.transform([text])    # transform the text into matrix 
    return model.predict(text_vector)[0] 

# Generate response 
def get_response(intent_tag) :            
    for intent in intents['intents'] : 
        if intent['tag'] == intent_tag : 
            return random.choice(intent['responses'])

# chatbot_response 
def chatbot_response(text) : 
    intent = predict_intent(text) 
    response = get_response(intent)
    return response 