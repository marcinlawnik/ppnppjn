#Napisz funkcję, która zapyta użytkownika o liczby x i y, a następnie obliczy działanie:

from math import sqrt

x = int(input("Podaj x"))
y = int(input("Podaj y"))

# Wersja rozbudowana
p1 = sqrt(x)
p2 = (5 * y) / (3 * (x ** 2))

output = p1 + p2

print("Wynik: ", output)
