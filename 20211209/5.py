#Policz, ile jest zdań w pliku 2.
# https://stackoverflow.com/questions/5074562/how-do-the-count-the-number-of-sentences-words-and-characters-in-a-file

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, 'NYTimes02.txt')

# Wydrukowanie zdań
for sencence in my_corpus.sents():
    print(sencence)

#Wydrukowanie liczby zdań
print(len(my_corpus.sents()))
