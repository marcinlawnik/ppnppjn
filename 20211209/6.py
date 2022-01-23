# Wydrukuj 60 pierwszych znaków z pliku 3.
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\New_York_Times'
my_corpus = PlaintextCorpusReader(corpus_root, 'NYTimes03.txt')


# Wydrukowanie zdań
file03 = nltk.Text(my_corpus.words('NYTimes03.txt'))

i = 0
for sentence in file03:
    for char in sentence:
        if i < 60:
            print(char, end='')
            i = i+1



# for i in range(0,10):
#     print(file01[i])

# i = 0
# for char in file01:
#     i=i+1
#     if i < 10:
#         print(char, end=' ')

# print(file01[:20])
# for char in my_corpus.chars():
#     print(char)