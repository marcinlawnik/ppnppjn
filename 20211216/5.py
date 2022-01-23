#Stwórz listę frekwencyjną wyrazów z pliku Times_file_01.txt.
# Następnie wydrukuj tylko te wyrazy, które pojawiły się 4 lub więcej razy.
# Wyświetl wyraz i liczbę wystąpień tego wyrazu w formacie: wyraz <=> liczba.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


# file01 = nltk.Text(my_corpus.words('Times_file_01.txt'))

fdist = nltk.FreqDist(my_corpus.words('Times_file_01.txt'))

for word in sorted(fdist):
    if fdist[word] >= 4:
        print(word, '<=>', fdist[word], end='\r\n')