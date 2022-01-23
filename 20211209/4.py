# Wydrukuj tylko te wyrazy z pliku 1, które są pisane wielkimi literami, np. BROOKS

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('NYTimes01.txt'))

# print(set(file01))

for word in set(file01):
    # https://www.nltk.org/book/ch01.html#tab-word-tests
    if word.isupper():
        print(word)