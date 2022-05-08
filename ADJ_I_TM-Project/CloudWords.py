from PrzygotowanieDanych import tekstClear, cloud
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv(r'Pliki_CSV/dataset.csv',nrows=10000)

# Cloud world dla kolumn Text
tekst = ""
for i in range(len(df['text']))[:400]:
    tekst += df['text'].iloc[i]
    text_wordcloud = tekstClear(tekst)
    bow = cloud(text_wordcloud)

wc = WordCloud()
wc.generate_from_frequencies(bow)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title("text")
plt.show()
