# Dodaj plik tekstowy do korpusu New_York_Times z listą wyrazową (bez polskich znaków). Zmień nazwę korpusu na New_York_Times_02. Wydrukuj pierwszy wyraz ze swojego pliku z listą wyrazową.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, 'NYTimes04.txt')


# Wydrukowanie zdań
file04 = nltk.Text(my_corpus.words('NYTimes04.txt'))

print(file04[0])