# Wydrukuj nazwy plików w tym korpusie.

from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')
print(my_corpus.fileids())