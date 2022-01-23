# Wydrukuj tylko te wyrazy z pliku paper1.txt, które mają ciąg liter „ff”.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Corpus_test1_A'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('paper1.txt'))

#wersja krotka
[print(w) for w in file01 if "ff" in w]

#wersja dluga
for w in file01:
    if "ff" in w:
        print(w)
