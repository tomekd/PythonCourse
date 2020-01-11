#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wczytaj_dane():
    pass

def most_common_room_number(dane):
    pass

def cheapest_flats(dane, n):
    pass

def find_borough(desc):
    dzielnice = ['Stare Miasto',
                 'Wilda',
                 'Jeżyce',
                 'Rataje',
                 'Piątkowo',
                 'Winogrady',
                 'Miłostowo',
                 'Dębiec']
    pass


def add_borough(dane):
    pass

def write_plot(dane, filename):
    pass

def mean_price(dane, room_number):
    pass

def find_13(dane):
    pass

def find_best_flats(dane):
    pass

def main():
    dane = wczytaj_dane()
    print(dane[:5])

    print("Najpopularniejsza liczba pokoi w mieszkaniu to: {}"
          .format(most_common_room_number(dane)))

    print("{} to najłądniejsza dzielnica w Poznaniu."
          .format(find_borough("Grunwald i Jeżyce"))))

    print("Średnia cena mieszkania 3-pokojowego, to: {}"
          .format(mean_price(dane, 3)))

if __name__ == "__main__":
    main()
