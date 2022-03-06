import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))

tekst = 'Lorem  cats doors singing sized and ipsum then dolor :) sit amet, consecte12tur; adipiscing elit.14124-23 Sed eget mattis sem. ;) ' \
        'Mauris ;(  egestas 425256  erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; ' \
        'lobortis, tortor elit marius:-) nisl fac124ilisis leo, at ;< tristique augue 1223risus eu risus ;-).'


def oczyszczanie(str: tekst):
    emotikony = re.findall('[:|;]\-*[\)|<|\(]', tekst)
    tekst1 = re.sub('[:|;]\-*[\)|<|\(]', '', tekst)
    tekst1 = tekst1.lower()
    tekst2 = re.sub('[^a-z ]', '', tekst1)
    tekst3 = re.sub(' +', ' ', tekst2)
    tekst4 = tekst3 + ''.join(emotikony)
    slowa = word_tokenize(tekst4)
    bezstopwords = [s for s in slowa if not s in stop_words]

    return bezstopwords


porter = PorterStemmer()
slowa1 = oczyszczanie(tekst)
slowa2 = []


def lemporter(str: slowa1):cd
    for word in slowa1:
        slowa2.append(porter.stem(word))
    return slowa2


print(lemporter(slowa1))
