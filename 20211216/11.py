# Napisz funkcję, która zapyta użytkownika w pętli 'for' trzy razy o podanie liczby,
# a następnie wydrukuje sześciany tych liczb.
for i in range(0, 3):
    liczba = int(input("Podaj liczbę: "))
    print("Sześcian liczby %i wynosi %i." % (liczba, liczba ** 3))


# przykład poboczny do range
zdanie = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(0, len(zdanie), 2):
    print(zdanie[i])