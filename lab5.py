import sklearn.feature_extraction.text
import pandas as pd
import re
import sklearn
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np


def funkcja(tekst: str) -> str:
    text_new = tekst

    # Usun Emotikony
    text_new = re.sub('[:;][^\s]', '', text_new)

    # Tekst male znaki
    text_new = text_new.lower()

    # Usun Cyfry
    text_new = re.sub('\d', ' ', text_new)

    # Usun znaki HTML
    text_new = re.sub(r"<[^>]*>", '', text_new)

    # Usun Whitespace
    text_new = re.sub('\s', ' ', text_new)

    # Usun znaki interpunkcyjne
    text_new = re.sub(r"[^0-9a-zA-Z ]+", '', text_new)

    return text_new


def stop_words(tekst: str) -> list:
    en_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tekst)
    return [w for w in word_tokens if w not in en_words]


def stemming(list_words: list) -> list:
    ps = PorterStemmer()
    return [ps.stem(w) for w in list_words if len(w) > 3]


def tekst_tokenizer(tekst: str) -> list:
    return stemming(stop_words(funkcja(tekst)))


df = pd.read_csv("fake.csv", nrows=100)

vectorizer = sklearn.feature_extraction.text.CountVectorizer(tokenizer=tekst_tokenizer)
vectorizer2 = TfidfVectorizer(tokenizer=tekst_tokenizer)
X_transform = vectorizer.fit_transform(df['title'][:3])
X_transform2 = vectorizer2.fit_transform(df['title'][:3])
print(vectorizer.get_feature_names_out())
print(X_transform.toarray())
z = X_transform.toarray().sum(axis=0)
t = X_transform2.toarray().sum(axis=0)
# 2. Jak wyciągnąć top 10 najczęściej występujących tokenów?

print(z)
print((-z).argsort()[:10])
index = (-z).argsort()[:10]

print(vectorizer.get_feature_names_out()[index])
# 3.
print(t)
print((-t).argsort()[:10])
indext = (-t).argsort()[:10]

print(vectorizer2.get_feature_names_out()[indext])
# 4. Jak wyciągnąć top 10 dokumentów, które zawierają najwięcej tokenów?

z4 = X_transform.toarray().sum(axis=1)
print((-z4).argsort()[:10])
index4 = (-z4).argsort()[:10]

print(vectorizer2.get_feature_names_out()[index4])
