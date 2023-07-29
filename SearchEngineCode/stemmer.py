from numpy import equal
import pandas
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import unidecode
# import contractions
import string
import csv

path = 'D:\\DSAProject\\Project\Dataset\\news_summary.csv'
df = pandas.read_csv(path, usecols=["text"], encoding='unicode_escape')
stop_words = stopwords.words('english')
snow_stemmer = SnowballStemmer(language='english')
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

i=0;
wordDict = {}
# clean_word = []
for text in df['text']:
    words = nltk.tokenize.word_tokenize(text)
    for word in words:
        word = word.strip()
        word = word.lower()
        word = unidecode.unidecode(word)
        word = snow_stemmer.stem(word)
        table = str.maketrans('','',string.punctuation)
        word = word.translate(table)
        if word not in wordDict.values() and word not in punc and word not in stop_words and word != '':
            wordDict[i] = word
            i=i+1
            print(i)


with open('D:\\DSAProject\\Project\\Code\\lexicon.csv', 'w') as f:
    f.write("%s,%s\n"%("key", "value"))
    for key in wordDict.keys():
        f.write("%s,%s\n"%(key,wordDict[key]))

print('Completed')