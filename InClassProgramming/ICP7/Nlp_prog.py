import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.util import ngrams


f= open("input.txt","w+", encoding="utf-8")
# First, we will grab a web page content then we will analyze the text to see what the page
# is about
# Assigning link to a variable
myLink = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# We will use the urllib module to crawl the web page:
# Opens the URL
getLink=urllib.request.urlopen(myLink)

# from the printed output, the result contains a lot of HTML tags that need to be cleaned

# We can use BeautifulSoup to clean the grabbed text like this:
# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
text = soup.get_text()
f.write(soup.get_text())

# we have a clean text from the crawled web page.
# convert that text into tokens by splitting the text like this
# Tokenization the text in the URL given
stokens = nltk.sent_tokenize(text)
wtokens = nltk.word_tokenize(text)

# Tokenization is the process of breaking a stream of text up into words, phrases, symbols, or
# other meaningful elements called tokens.
# Printing Tokenized Sentences
print(" ---------------- sentences ---------------- ")
for s in stokens:

    print(s)
# Printing Tokenized Words
print(" ----------------------- words ------------------------- ")
for w in wtokens:
    print(w)

# Stemming the text in the URL given
ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer('english')
# stemming is process of reducing the words to it stem base root word
print("----------------------------- Stemming Output ---------------- ")
for words in wtokens:
 # print("Porter stemming Output")
    #print(ps.stem(words))
   # print("Lancaster stemming Output")
    #print(ls.stem(words))
   # print("Snowball stemming Output")
    print(ss.stem(words))

# lemma is a canonical form of the word
# Lemmatization (will apply pos to get a proper word)
lemmatizer = WordNetLemmatizer()
print("---------------------------- Lemmatized Output --------------------- ")
print(lemmatizer.lemmatize(text))


print("--------------------------- stemming vs lemmetization ---------------  ")
print("lemm:",lemmatizer.lemmatize('finally'))
print("stem:",ss.stem('finally'))

# Parts of speech
# The process of classifying the words in a text(corpus) into their parts of speech
print("------------------------------------ POS output ------------------------")
# for w in wtokens:
possentence="hello i am a software engineer"
wtokenspos = nltk.word_tokenize(possentence)
print(nltk.pos_tag(wtokenspos))

   #print(nltk.pos_tag(w))
#print(nltk.pos_tag_sents(possentence))

# Named Entity Recognition
print("----------------- NER output ------------------")
sentence = "The Spring Web MVC framework provides Model View Controller architecture and ready components that can be used to develop flexible and loosely coupled web applications"
print(ne_chunk(pos_tag(word_tokenize(sentence))))

# Trigram
print("------------------------- Trigram output -----------------------------")
mySentence = "Hello i am a software engineer by birth"
token=nltk.word_tokenize(mySentence)
trigram = ngrams(token,3)
for t in trigram:
    print(t)


# ----------------------- since the webpage data is showing a huge amount of output,
# I have cut down for few techniques using a sample input sentences
# All the above techniques can handle any amount of data