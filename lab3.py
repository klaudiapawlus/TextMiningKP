import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# reading CSV file
data = pd.read_csv("fake.csv", nrows=1000)

# converting column data to list
lista = data['text'].tolist()
tekst = ",".join(lista)

stop_words = set(stopwords.words('english'))


def oczyszczanie(str: tekst):
    emotikony = re.findall('[:|;]\-*[\)|<|\(]', tekst)
    tekst1 = re.sub('[:|;]\-*[\)|<|\(]', '', tekst)
    tekst1 = tekst1.lower()
    tekst2 = re.sub('[^a-z ]', '', tekst1)
    tekst3 = re.sub(' +', ' ', tekst2)
    # tekst4 = tekst3 + ''.join(emotikony)
    slowa = word_tokenize(tekst3)
    bezstopwords = [s for s in slowa if not s in stop_words]

    return bezstopwords


slowa1 = oczyszczanie(str)
# print(slowa1)

porter = PorterStemmer()
slowa2 = []


def lemporter(str: slowa1):
    for word in slowa1:
        slowa2.append(porter.stem(word))
    return slowa2


tekstdict = (lemporter(slowa1))

tf_diz = dict.fromkeys(tekstdict)


def bow(tf_diz, tekstdict):
    for word in tekstdict:
        tf_diz[word] = tekstdict.count(word)
    return tf_diz


bow = bow(tf_diz, tekstdict)

wc = WordCloud()
wc.generate_from_frequencies(bow)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# uniques = list(set(tokens))
#     bow = {unique: tokens.count(unique) for unique in uniques}
