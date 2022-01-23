# Wydrukuj najkrótsze zdanie (lub zdania) z pliku Times_file_02.txt.

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file02 = nltk.Text(my_corpus.sents('Times_file_02.txt'))

#najdłuższe zdanie
max_length = 0
for sentence in file02:
    if len(sentence) > max_length:
        max_length = len(sentence)

print(max_length)

for sentence in file02:
    if len(sentence) == max_length:
        print(sentence)

#Najkrótsze zdanie
min_length = 1000
for sentence in file02:
    if len(sentence) < min_length:
        min_length = len(sentence)

print(min_length)

for sentence in file02:
    if len(sentence) == min_length:
        print(sentence)