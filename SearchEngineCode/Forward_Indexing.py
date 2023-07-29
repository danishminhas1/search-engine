from numpy import equal
import pandas
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import unidecode
# import contractions
import string
import csv

path = 'D:\\DSAProject\\Project\\Code\\lexicon.csv'
df = pandas.read_csv(path, usecols = ["key", "value"], encoding='unicode_escape')
#loading back to dictionary
word_dict = {}
i=0
for word in df['value']:
    word_dict[i] = word
    i+=1
    #print(i)



path_data = 'D:\\DSAProject\\Project\Dataset\\news_summary.csv'
df = pandas.read_csv(path_data, usecols=["text"], encoding='unicode_escape')
stop_words = stopwords.words('english')
snow_stemmer = SnowballStemmer(language='english')
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

i=0;
doc_index = 0; 
# clean_word = []
forward_index_final = {}
for text in df['text']:
    forward_index = {}
    words_in_forward=[]
    print(f"Working for doc_id = {doc_index}")
    words = nltk.tokenize.word_tokenize(text)
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
            #print(word)
            if word not in words_in_forward:
                words_in_forward.append(word);
                #print("not already")
                forward_index[index] = 1
            else:
                #print("already")
                forward_index[index] += 1
    
    forward_index_final[doc_index] = forward_index
    doc_index+=1


with open('forward_index.csv', 'w') as f:
    f.write("%s,%s,%s\n"%("doc_id", "word_id", "number_of_hits"))
    for i in forward_index_final.keys():
        f.write("%s,%s,%s\n"%(i, "", ""))
        for j in forward_index_final[i].keys():
            f.write("%s,%s,%s\n"%("", j, forward_index_final[i][j]))
        