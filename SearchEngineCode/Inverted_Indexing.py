from numpy import equal
import pandas
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import unidecode
# import contractions
import string
import csv

#--------------------------------------------------------------------------------
#loading lexicon into dictionary
path = 'D:\\DSAProject\\Project\\Code\\lexicon.csv'
df = pandas.read_csv(path, usecols = ["key", "value"], encoding='unicode_escape')
#loading back to dictionary
word_dict = {}
i=0
for word in df['value']:
    word_dict[i] = word
    i+=1
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
path = 'D:\\DSAProject\\Project\Dataset\\news_summary.csv'
df = pandas.read_csv(path, usecols=["text"], encoding='unicode_escape')
stop_words = stopwords.words('english')
snow_stemmer = SnowballStemmer(language='english')
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

i=0;
# clean_word = []
inverted_index = {}
inverted_words = []
doc_id = 0;
for text in df['text']:
    words = nltk.tokenize.word_tokenize(text)
    word_pos = 0
    for word in words:
        word = word.strip()
        word = word.lower()
        word = unidecode.unidecode(word)
        word = snow_stemmer.stem(word)
        table = str.maketrans('','',string.punctuation)
        word = word.translate(table)
        if word in word_dict.values() and word not in punc and word not in stop_words and word != '':
            key_list = list(word_dict.keys())
            val_list = list(word_dict.values())
            index = list(word_dict.keys())[list(word_dict.values()).index(word)]
            
            if word not in inverted_words:
                inverted_words.append(word)
                inverted_index[index] = {doc_id:str(word_pos)}
            else:
                if doc_id in inverted_index[index].keys():
                    inverted_index[index][doc_id] += '|' + str(word_pos)
                else:
                     inverted_index[index][doc_id] = str(word_pos)
        word_pos+=1
    
    doc_id+=1
    print(doc_id)
print(inverted_index)

with open('inverted_index.csv', 'w') as f:
    f.write("%s,%s,%s,%s\n"%("Word_ID", "DOC_ID", "Frequency" ,"Positions"))
    for i in inverted_index.keys():
        f.write("%s,%s,%s,%s\n"%(i, "", "", ""))
        for j in inverted_index[i].keys():
            f.write("%s,%s,%s,%s\n"%("", j, len(inverted_index[i][j].split('|')),inverted_index[i][j]))
        f.write("%s,%s,%s,%s\n"%(-1, "", "", ""))

print("Done")