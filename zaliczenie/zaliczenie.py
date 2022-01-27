import nltk
from nltk.corpus import PlaintextCorpusReader
corpus = PlaintextCorpusReader(r'.\zal1_korpusA', '.*')

# Wydrukuj nazwy plików w tym korpusie
print("Zadanie 2")
print(corpus.fileids())

# Zbuduj konkordans dla wyrazu „Swiss” w pliku text01.txt
print("Zadanie 3")
nltk.Text(corpus.words('text01.txt')).concordance('Swiss')

# Wydrukuj tylko te wyrazy z pliku text01.txt, które kończą się literą „s”
print("Zadanie 4")
for word in nltk.Text(corpus.words('text01.txt')):
    if word[-1] == "s":
        print(word)

# Policz, ile razy pojawił się wyraz „Davos” w pliku text01.txt
print("Zadanie 5")

i = 0
for word in nltk.Text(corpus.words('text01.txt')):
    if word == "Davos":
        i = i+1

print("Wyraz dawos pojawia się %i razy w tekście" % i)


#  Wydrukuj najdłuższy wyraz z pliku text01.txt
print("Zadanie 6")
max_length = 0
for word in nltk.Text(corpus.words('text01.txt')):
    if len(word) > max_length:
        max_length = len(word)

for word in nltk.Text(corpus.words('text01.txt')):
    if len(word) == max_length:
        longest_word = word

print("Najdłuższym złowem w tekście jest: %s" % longest_word)

# Stwórz listę frekwencyjną wyrazów z pliku text01.txt.
# Następnie wydrukuj tylko te wyrazy, które pojawiły się dokładnie 3 razy w tekście.
# Wyświetl wyraz i liczbę wystąpień tego wyrazu w formacie: word appeared number times

print("Zadanie 7")
freqDist = nltk.FreqDist(corpus.words('text01.txt'))
for word in freqDist:
    if freqDist[word] == 3:
        print(word, " appeared ", freqDist[word], " times")

# Policz, ile jest zdań w pliku text02.txt
print("Zadanie 8")
sentences = corpus.sents('text02.txt')
print("W pliku text02.txt jest %i zdań" % len(sentences))

# Wydrukuj tylko te zdania z pliku text02.txt, które zawierają nazwisko „Trump”
print("Zadanie 9")
for sentence in sentences:
    should_print = False
    for word in sentence:
        if word == "Trump":
            should_print = True
    if should_print:
        print(sentence)

# Wydrukuj 4 ostatnie wyrazy/tokeny z przedostatniego zdania w pliku text02.txt
print("Zadanie 10")
words = corpus.words('text02.txt')
print(words[-4:])

#Wydrukuj tylko duże litery z pliku text03.txt
print("Zadanie 11")
words = corpus.words('text03.txt')
for word in words:
    for char in word:
        if char.isupper():
            print(char, end='')

# Policz, ile jest różnych typów dużych liter w pliku text03.txt
print("Zadanie 12")
words = corpus.words('text03.txt')
chars = []
i = 0
for word in words:
    for char in word:
        if char.isupper():
            i = i + 1
            chars.append(char)

print("text03.txt zawiera ", len(set(chars)),  " różnych wielkich liter: ",  set(chars))

# Napisz funkcję, która zapyta użytkownika o liczby x i y, a następnie obliczy działanie:
print("Zadanie 13")
from math import sqrt
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

calculation = (6*sqrt(x)) - ((2 * (y ** 4))/(y  - (x ** 2)))

print("Wynik działania to ", calculation)

# Napisz funkcję, która zapyta użytkownika o imię, a następnie zapyta, czy użytkownik bierze udział w loteriach.
# Jeśli użytkownik odpowie „tak”, to zostanie wydrukowana informacja:
# „IMIĘ, masz szansęna wygraną.” Jeśli zostanie wprowadzona inna odpowiedź,
# to program wydrukuje „IMIĘ, nigdy nie wygrasz!” Za IMIĘ podstaw tekst, który wpisałeś/-aś,
# korzystając z operatora %s. Postaraj się, aby program akceptował różne pisownie wyrazu „tak”
print("Zadanie 14")
imie = str(input("Podaj imię: "))
loteria = str(input("Czy bierzesz udział w loteriach?"))
# Normalizacja do małych liter i usuwanie spacji
# Tutaj możnaby jeszcze usuwać cyfry, niepoprawne znaki unicode i inne bajery.
loteria = loteria.lower().strip()

if loteria == "tak":
    print("%s, masz szansę na wygraną." % imie)
else:
    print("%s, nigdy nie wygrasz!" % imie)


