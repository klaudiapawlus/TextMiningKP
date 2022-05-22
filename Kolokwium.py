import re
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from wordcloud import WordCloud
# nltk.download

df = pd.read_csv("alexa_reviews.csv", sep=";", encoding='cp1252', names=['rating', 'verified_reviews'])
# print(data.head())
lista = df['verified_reviews'].tolist()
tekst = ",".join(lista)

def regex(tekst: str) -> str:
    text_new = tekst
    text_new = re.sub('[:;][^\s]', '', text_new)
    text_new = text_new.lower()
    text_new = re.sub('\d', ' ', text_new)
    text_new = re.sub('[\u00A0]', ' ', text_new)
    text_new = re.sub('\s', ' ', text_new)
    text_new = re.sub('[^\w]', ' ', text_new)
    text_new = re.sub(r"[^0-9a-zA-Z ]+", '', text_new)

    return text_new


def stop_words(tekst: str) -> list:
    en_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tekst)
    return [w for w in word_tokens if w not in en_words]


def stemming(list_words: list) -> list:
    ps = PorterStemmer()
    return [ps.stem(w) for w in list_words]


def tekstClear(tekst: str) -> list:
    return stemming(stop_words(regex(tekst)))


#
# print(tekstClear(tekst)
#
def bag(words: list) -> dict:
    bow = {}
    for w in words:
        if w not in bow.keys():
            bow[w] = 1
        else:
            bow[w] += 1
    return bow


print(bag(tekstClear(tekst)))

#WordCloud
for col in df['verified_reviews'].tolist():
    tekst = ""
    tekst += df[col].iloc[i][:100]
    text_wordcloud = tekstClear(tekst)
    bow = bag(text_wordcloud)
wc = WordCloud()
wc.generate_from_frequencies(bow)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
