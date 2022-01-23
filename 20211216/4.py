# Znormalizuj tekst z pliku Times_file_01.txt do małych liter i oblicz, ile jest typów wyrazów.

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('Times_file_01.txt'))

normalized = set(w.lower() for w in file01)

print(len(normalized))


