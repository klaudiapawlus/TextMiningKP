from PrzygotowanieDanych import tekstClear
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics

df = pd.read_csv("Pliki_CSV/dataset.csv",nrows=100000)

vectorizer = CountVectorizer(tokenizer=tekstClear)
df_vectorizer = vectorizer.fit_transform(df['text'])

X_train, X_test, Y_train, Y_test = train_test_split(df_vectorizer, df["humor"], test_size=0.4, random_state=40)

klasyfiaktory = [DecisionTreeClassifier(),
                 RandomForestClassifier(),
                 LinearSVC(),
                 AdaBoostClassifier(),
                 BaggingClassifier()]

for klasyfikator in klasyfiaktory:
    klasyfikator.fit(X_train, Y_train)
    Y_pred = klasyfikator.predict(X_test)
    print(f"{klasyfikator} - Accuracy: {round(metrics.accuracy_score(Y_test,Y_pred)*100,2)}%")
