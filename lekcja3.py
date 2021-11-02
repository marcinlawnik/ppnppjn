#zad 1
# Zapytaj o liczbę, a następnie wydrukuj kolejno liczby od 0 do przedostatniej liczby podanej przez ciebie

def zad1():
    n=int(input())
    for i in range(0, n):
        print(i)

zad1()


# Zapytaj użytkownika o to dokąd chce jechać i kiedy, a następnie wydrukuj informację
def zad2():
    print("Where do you want to go?")
    where = input()
    print("When do you want to go?")
    when = input()
    print("You want to go to %s on %s" % (where, when))

zad2()

# Wydrukuj kwadraty liczb od 0 do 9, użyj pętli for
def zad3():
    for i in range(0, 10):
        print(i ** 2, end=' ')
# end ustala string na końcu, dajemy spację zamiast domyślnej nowej linii

zad3()

# Wydrukuj lioczyn liczb z zakresu 10-15 pomnożonych przez 2, skorzystaj z for
def zad4():
    for i in range(10, 16):
        print(i * 2, end=' ')

zad4()