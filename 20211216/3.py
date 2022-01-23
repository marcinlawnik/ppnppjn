# Zbuduj konkordans dla wyrazu 'Brexit' w pliku Times_file_01.txt

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('Times_file_01.txt'))
file01.concordance('Brexit')