#load modules for natural language kit to import ngrams,word & sentence tokenizer
import nltk
from nltk.util import bigrams
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

#load input file / read the file
input_data=open('ip.txt',"r")
#read the data
data=input_data.read()
#get each word from sentence
words=word_tokenize(data)
#apply lemmitizer
lemm=WordNetLemmatizer()
list=[]
list1=[]
print("Applying lemmatization on all words ..... loading()... "+"\n")
#print lemma equivalent for each word
for each in words:
    print("Lemma for the word "+ "'"+each+"'"+" is "+lemm.lemmatize(each))

print("\n")
print("Applying Bigrams on the text corpus ..... loading()... "+"\n")
#print bigram to the text corpus
for eachbi in bigrams(words):
    print(eachbi)
    list.append(eachbi)

#append each word in bigram to a list to calc frequencies
for y in list:
    for z in y:
        list1.append(z)
#calc bigram word frequency and top 5 repeated words
count=Counter(list1)
count_most=count.most_common(5) #most_common function()
most=[i[0] for i in count_most]
#print bigram word frequency and top 5 repeated words
print("\nBigram word frequencies for each word\n")
print(count)
print("\nTop 5 bigrams repeated most\n")
print(count_most)
#calc Senteces with repeated bigrams
concat=""
repeated_sent=sent_tokenize(data)
print("\n Senteces with repeated bigrams:\n ")
for m in repeated_sent:
    if any(word in m for word in most):
        print(m)
        concat=concat+m
#print Senteces with repeated bigrams
print("\n Sentence after concatenation is: \n"+concat)