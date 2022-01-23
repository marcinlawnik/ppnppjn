# Wydrukuj nazwy plików w tym korpusie.
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

# Wersja hard
#import os
# arr = os.listdir("New_York_Times")
# print(arr)


from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')
print(my_corpus.fileids())

