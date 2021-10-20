#drugie zajęcia:
#–	listy vs zbiory (set)
#–	funkcja len
#–	funkcja sorted
#–	funkcja print ze wstawianiem zmiennej (%s, %d, %f)

#Lista jest w lekcji 1, a zbiory poznamy teraz
#To też jest grupa elementów, tyle że:
# jest nieuszeregowana (nie ma kolejności)
# każdy element jest unikatowy (dwa takie same elementy są łączone w jeden)
# nie można zmieniać jego elementów (ale można usuwać i dodawać elementy do zbioru)
zbior = {1, 1, 2, 2, 3}
print(zbior)

#zauważ że wynik to {1,2,3}. a nie {1,1,2,2,3}

# Nowy pusty zbior tworzymy funkcją set()
zbior = set()
print(type(zbior))

#uwaga: zrobienie pustych nawiasów klamrowych tworzy słownik (dictionary), nie zbiór
zbior = {}
print(type(zbior))

#przydatne operacje na zbiorach
zbior = {5,2,9,3,1}
print(zbior)

#długość zbioru (ilość elementów)
print(len(zbior))

#dodanie elementu do zbioru
zbior.add(4)
print(zbior)
print(len(zbior))

#usunięcie elementu
zbior.remove(1)
print(zbior)
print(len(zbior))

#Można też dokleić elementy z listy do zbioru
zbior.update([11,12,13])
print(zbior)
print(len(zbior))

#zbiór albo listę albo inne typy można posortować funkcją sorted()
#funkcja sorted zawsze zwraca LISTE (nie ten typ który sortujemy)
# pierwszy argument to to co sortujemy, pozostale opcjonalne to kolejnosc i klucz po ktorym sortujemy
# wiec reverse da nam sortowanie malejace
print(sorted(zbior, reverse=True))

#więcej przydatnych rzeczy:
#https://www.programiz.com/python-programming/set
