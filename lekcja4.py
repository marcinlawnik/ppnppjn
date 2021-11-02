# Funkcja zapyta o podanie liczby oraz o tekst, a następnie wydrukuje tekst tyle razy, ile wynosi liczba
# podana przez użytkownika w jednym ciągu
# Jeżeli wydrukowany tekst będzie dłuższy lub równy 30 znakom, to wydrukuje "BRAWO!", a
# jeżli nie, to pojawi się komunikat "Spróbuj jeszcze raz!"


def dlugosc_tekstu():
    print("Podaj liczbę: ")
    liczba = int(input())
    print("Podaj tekst: ")
    tekst = input()
    wynik = tekst * liczba

    print(wynik)
    if len(wynik) >= 30:
        print("BRAWO!")
    else:
        print("Spróbuj jeszcze raz!")


dlugosc_tekstu()