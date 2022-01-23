# Napisz funkcję, w której zapytasz użytkownika o imię oraz ilość wykonanych zadań.
# Jeżeli liczba jest większa od 3, to wydrukuj informację 'imię, bardzo dobrze!.',
# a jeśli nie to wydrukuj 'imię, musisz więcej pracować w domu.' =>
# Za 'imię' należy podstawić to, co wpisał użytkownik, czyli np. 'Jola, bardzo dobrze!' lub 'Jola, musisz więcej pracować w domu.'


who = input("Jak masz na imię?")
how_many = int(input("Ile zadań wykonano?"))

if how_many > 3:
    print("%s, bardzo dobrze!" % who)
else:
    print("%s, musisz więcej pracować w domu." % who)