#Zbuduj konkordans dla wyrazu 'sisters' w pliku 1.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file01 = nltk.Text(my_corpus.words('NYTimes01.txt'))
file01.concordance('sisters')