# Stwórz listę frekwencyjną wyrazów z pliku paper1.txt.
# Następnie wydrukuj tylko te wyrazy i tokeny,
# które pojawiły więcej niż 3 razy w tekście.
# Wyświetl wyraz i liczbę wystąpień tego wyrazu/tokenu w formacie:
# wyraz *** >>> *** liczba.

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Corpus_test1_A'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')

fdist = nltk.FreqDist(my_corpus.words('paper1.txt'))

for word in sorted(fdist):
    if fdist[word] >= 3:
        print(word, ' *** >>> *** ', fdist[word], end='\r\n')