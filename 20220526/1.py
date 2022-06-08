# 2 - Za pomocą funkcji re_show znajdź rożne pisownie wyrazu "chairman".
# 3 – Znajdź wszystkie liczby w pliku i wydrukuj.
# 4 – Policz, ile jest wszystkich wyrazów/tokenów w pliku.
# Przykładowe działanie programu:
#
# Poznan, 2018-05-24
# Task 1
#
# I am wondering about a word {chairman} at least 6 times. Can a woman be a {Chairman}?
# Maybe it is better to say a chairperson? {Chairrrrrmannnn}!!! Does it sound very masculine?
# Even if I say this 1000 times for me it is neutral. I would say {charman} may also be a woman.
# And what do you think about the word '{chaiman}'?
# ['2018', '05', '24', '1', '6', '1000']
# 74

# https://www.geeksforgeeks.org/reading-writing-text-files-python/
import nltk
from nltk.corpus import PlaintextCorpusReader

file = open("chairman.txt", "r")

text = ""
for line in file.readlines():
    text = text + line + " "
print(text)

nltk.re_show(r"[cC]hai*r*man*", text)

nltk.re_show(r"[0-9]+", text)

corpus_root = r'.\.'
my_corpus = PlaintextCorpusReader(corpus_root, '.*')


words = nltk.Text(my_corpus.words('chairman.txt'))

#ilość słów w tekście
print(len(words))

file.close()
