# Wydrukuj tylko te wyrazy z pliku paper1.txt, które mają 10 liter.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Corpus_test1_A'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('paper1.txt'))

#wersja krotka
[print(w) for w in file01 if len(w) == 10]

#wersja dluga
for w in file01:
    if len(w) == 10:
        print(w)

#przykład z while
slowo = 0
while slowo < len(file01):
    if len(file01[slowo]) == 10:
        print(file01[slowo])
    slowo = slowo + 1