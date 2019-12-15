#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
zad. 1
Przejrzyj plik podstawy.py. Zawiera on kopię materiałów z części wykładowej.
"""

"""
zad. 2
Stwórz zmienną o nazwie `PI` i wartości 3.14. Wykorzystaj ją do obliczenia pola koła o promieniu 12.
Wynik wyświetl na ekran.
"""

"""
zad. 3
 * Stwórz dwie zmienne imie i nazwisko i przypisz do dowolne wartości (nie muszą
być prawdziwe).
 * wypisz obie zmienne na ekran.
 * Połącznie obie zmienne spacją i wynik zapisz do zmiennej dane.
"""

"""
zad. 4
Przekonwertuj wartość b na int, a następnie oblicz średnią z a, b i c.
"""
a = 314
b = "500"
c = 4.5

"""
zad. 5
Wczytaj z klawiatury 3 liczby, skonwertuj je na dowolny typ liczbowy, a
wynik zapisz do zmiennej suma. Wyświetl zawartość tej funkcji na ekran.
"""

"""
zad. 1
Stwórz 3 elementową listę, która zawiera nazwy 3 Twoich ulubionych owoców.
Wynik przypisz do zmiennej `owoce`.
"""

"""
zad. 2
Dodaj do powyższej listy jako nowy element "pomidor".
"""

"""
zad. 3
Usuń z powyższej listy drugi element.
"""


"""
zad. 4
Rozszerz listę o tablice ['Jabłko', "Gruszka"].
"""

"""
zad. 5
Wyświetl listę owoce, ale bez pierwszego i ostatniego elementu.
"""

"""
zad. 6
Wyświetl co trzeci element z listy owoce.
"""

"""
zad. 7
Stwórz pusty słownik i przypisz go do zmiennej magazyn.
"""

"""
zad. 8
Dodaj do słownika magazyn owoce z listy owoce, tak, aby owoce były kluczami,
zaś wartościami były równe 5.
"""

"""
zad. 9
 * Stwórz listę składającą się z parzystych elementów listy l (l. parzystych)
 * Stwórz listę z elementów l o nieparzystych indeksach
"""
l = [4, 5, 8, 9, 0, 3]

"""
zad. 10
Lista `zad10` zawiera 2 elementy - listy. Stwórz nową listę `zad10_flat`,
która będzie składać się z elementów każdej z tych listy.
"""

zad10 = [[9, 8, 12, 7], [12, 33, 8, 7]]

"""
zad. 11
Stwórz listę zad11out, która powstanie z <zad11> poprzez usunięcie 
powtarzających się wartości.
"""

zad11 = [3, 2, 2, 6, 9, 10, 1, 3]

"""
zad. 12
Wyświetl sumę liczb od 1 do 256.
"""

"""
zad. 13
Wyświetl sumę liczb parzystych od 1 do 256.
"""

"""
zad. 14
Poniżej znajdują się 2 słowniki z danymi o liczbie przejazdów rowerami miejskimi w Montrealu w 2018 z podziałem na miesiące.
Pierwszy słownik zawiera informacje o przejazdach wykonanych przez posiadaczy abonamentu, a drugi przez ludzi, który
nie mają wykupionego abonamentu. Dane pochodzą ze strony https://montreal.bixi.com/en/open-data. 

a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z miesięcy.
b) Wykorzystując listę `months` wyświetl ile w danym miesiącu odbyło się przejazdów. Załóż, że odbyło się 0 przejazdów 
w miesiącach, którycj brakuje w `all_rides`.
c) Oblicz jaki procent stanowią w ciągu roku przejazdy okazjonalne.
d) Czy obie grupy osiągają największą liczbę przejazdów w tym samym miesiącu? Spróbuj znaleźć odpowiedź bez patrzenia
na wartości w podanych słownikach.
"""

members = {'April': 211819, 'May': 682758, 'June': 737011, 'July': 779511, 'August': 673790,
           'September': 673790, 'October': 444177, 'November': 136791}

occasionals = {'April': 32058, 'May': 147898, 'June': 171494, 'July': 194316, 'August': 206809,
               'September': 140492, 'October': 53596, 'November': 10516}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

