# Operacje matematyczne
# Dodawanie
print(2 + 2)
# Odejmowanie
print(5 - 3)
# mnożenie
print(6 * 4)
# Dzielenie
print(8 / 2)
# Potęgowanie
print(5 ** 3)
# Modulo (reszta z dzielenia)
print(5 % 2)

# Zmienna to takie "pudełko/miejsce" w ktorym można zapisać dane
# dane te można zmieniać w trakcie działania programu
# Jest wiele różnych typów, ale te podstawowe poniżej
# funkcja type() pozwala poznać typ danej zmiennej
# Ciąg znaków, string
ciag = "Testowy ciąg"
print(type(ciag))  #str
# liczba całkowita, integer
ciag = 4
print(type(ciag))  #int
# liczba zmiennoprzecinkowa (float)
ciag = 5.2
print(type(ciag))  #float
#wartość logiczna, typ boolean, prawda/fałsz
ciag = True
print(type(ciag))

# Zmienna może też zawierać listę
#lista jest mutowalna, czyli można ją zmieniać w trakcie wykonywania programu
# elementy listy (ang. list) zapisujemy w kwadratowych nawiasach
# elementy listy mogą być różnych typów
ciag = ['test', 5, 7.3, ['inna lista', 2]]
print(ciag)

#Więcej materiałów o liście:
# https://www.programiz.com/python-programming/list

#Możemy się też odwoływać do poszczegołnych elementów listy (są indeksowane/liczone od zera)
print(ciag[0])
#z minusem liczy się od końca
print(ciag[-2])
#Albo nawet zagłębić się dalej niż 1 poziom
print(ciag[3][0])

# Wypisywanie zmiennych
string = "tekst"
integer = 3
float = 8.23456789

# do wypisywania służy funkcja print
# można podać samą zmienną
print(float)
#jakiś tekst
print("tekst")
#albo kombinację zmiennych i tekstów, jak poniżej,
# gdzie te znaczki %d, %f itd. są podmieniane
# %s to string
# %d to liczba całkowita
# %f to float

# precyzję (ilość miejsc po przecinku) podajemy jako .X przed modyfikatorem, czyli %.5d to 5 miejsc po przecinku
print(
    'Tekst: %s, liczba całkowita %d oraz stworzyłem liczbę rzeczywistą %.4f, dla której wyświetlam 4 miejsca po przecinku.'
    % (string, integer, float))
