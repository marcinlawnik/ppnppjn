# Napisz funkcję, która zapyta użytkownika o liczby x i y, a następnie obliczy działanie:
from math import sqrt

x = int(input("Podaj x"))
y = int(input("Podaj y"))

# Wersja rozbudowana
p1 = (2 * (x ** 4))
p2 = (sqrt(y) / x)

output = p1 + p2

print("Wynik: ", output)

# wersja jednolinjkowa
output = (2 * (x ** 4)) + (sqrt(y) / x)

print("Wynik: ", output)