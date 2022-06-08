# Wydrukuj do pliku zewnętrzenego "output.txt" w folderze "2022-05-19" swoje imię z literami jedną pod drugą (w pętli "for"). Następnie zapytaj użytkownika o jakąś liczbę i również wydrukuj ją do tego samego pliku.
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
file = open(r"output.txt", "w")

for letter in "MarcinLawniczak":
    file.write(letter + "\n")

liczba = int(input("Podaj liczbę:\n"))
file.write(str(liczba))

file.close()
