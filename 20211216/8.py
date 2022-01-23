# Zsumuj cyfry z zadania 7.


import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'.\Zal_korpus_01'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


file03 = nltk.Text(my_corpus.words('Times_file_03.txt'))

sum = 0

for word in set(file03):
    # https://www.nltk.org/book/ch01.html#tab-word-tests
    if word.isdigit():
        # sum = sum + int(word)
        sum += int(word)

print(sum)