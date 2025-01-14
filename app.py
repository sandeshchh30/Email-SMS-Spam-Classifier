import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import pickle
import streamlit as st

model = pickle.load(open('Model.pkl' , 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl' , 'rb'))
ps = PorterStemmer()

def text_preprocessor(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for word in text:
        if word.isalnum():
            y.append(word)

    text = y[:]
    y.clear()
    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(ps.stem(word))
    
    return ' '.join(y)

st.title("Email Spam Classifier")

text = st.text_area(label='Type your Email Message')

if st.button(label='Predict'):
    text = text_preprocessor(text)
    text = vectorizer.transform([text])
    prediction = model.predict(text)

    if prediction[0] == 0:
        st.header("NOT SPAM")
    else:
        st.header("SPAM")