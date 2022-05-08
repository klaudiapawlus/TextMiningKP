import numpy as np
import sklearn.feature_extraction.text
from PrzygotowanieDanych import tekstClear
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

df = pd.read_csv(r"Pliki_CSV/dataset.csv",nrows=10000)

# 1. Top 10 najczęściej występujących tokenów dla kolumny Text?
vectorizer = sklearn.feature_extraction.text.CountVectorizer(tokenizer=tekstClear)
X_transform = vectorizer.fit_transform(df['text'])
sum_list = X_transform.toarray().sum(axis=0)
suma = -np.sort(-sum_list)[:10]
slowa = vectorizer.get_feature_names_out()[-np.argsort(-sum_list)[:10]]

# print(f"Suma: {suma}")
# print(f"Słowa: {slowa}")
plt.subplots(figsize=(10,5))
plt.bar(slowa, suma, width=0.4, color='green')
plt.title("Top 10 najczęściej występujących tokenów dla kolumny Text")
plt.show()
print()

#PrettyTable
columns = ["Słowa","Suma"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowa)
newTable.add_column(columns[1], suma)
print(newTable)


# 2. Top 10 najważniejszych tokenów dla kolumny Text?
vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(tokenizer=tekstClear)
X_transform = vectorizer.fit_transform(df['text'])
sum_list = X_transform.toarray().sum(axis=1)
sumaTFIDF = -np.sort(-sum_list).round(2)[:10]
slowaTFIDF = vectorizer.get_feature_names_out()[-np.argsort(-sum_list)[:10]]

plt.subplots(figsize=(11, 5))
plt.bar(slowaTFIDF, sumaTFIDF, width=0.5, color='red')
plt.title("Top 10 najważniejszych tokenów dla kolumny Text")
plt.show()
print()

# PrettyTable
columns = ["Słowa TFIDF", "Suma TFIDF"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowaTFIDF)
newTable.add_column(columns[1], sumaTFIDF)
print(newTable)


# 3. Top 10 dokumentów, które zawierają najwięcej tokenów
z4 = X_transform.toarray().sum(axis=1)
liczbaTop10 = (-z4).argsort()[:15]
slowaTop10 = vectorizer.get_feature_names_out()[(-z4).argsort()[:15]]

# print(f"Top 10 dokumentów: {(-z4).argsort()[:10]}")
# print(f"Top 10 dokumentów: {vectorizer.get_feature_names_out()[(-z4).argsort()[:10]]}")
plt.subplots(figsize=(16, 5))
plt.bar(slowaTop10, liczbaTop10, width=0.5)
plt.title("Top 10 dokumentów, które zawierają najwięcej tokenów")
plt.show()
print()

# PrettyTable
columns = ["Liczba Top 10", "Słowa Top 10"]
newTable = PrettyTable()
newTable.add_column(columns[0], slowaTop10)
newTable.add_column(columns[1], liczbaTop10)
print(newTable)
