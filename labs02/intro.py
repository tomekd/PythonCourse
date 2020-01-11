

"""
1. Napisz funckję, która zamieni stopnie Fahrenheita na Celcjusza zgodnie ze
wzorem:
    F = 32 + 9/5*C

Następnie dodaj kowałek kodu, który pozwoli na wczytanie temperatury z
klawiatury, a następnie wyświetli temperaturę w Fahrenheitach.

"""

"""
2. Poniższa słownik Letters zawiera informacje o literach w grze Scrubble,
dokładniej ile tabliczek z daną literą występuje w grze oraz wartość punktową
danej litery.

Napisz program, który wczyta z klawiatury słowo, a nastęnie zwróci ile dane
słowo jest warte punktów.

"""

Letters = {
        'a': { 'quantity' : 9, 'value': 1},
        'b': { 'quantity' : 2, 'value': 3},
        'c': { 'quantity' : 2, 'value': 3},
        'd': { 'quantity' : 4, 'value': 2},
        'e': { 'quantity' : 12, 'value': 1},
        'f': { 'quantity' : 2, 'value': 4},
        'g': { 'quantity' : 3, 'value': 2},
        'h': { 'quantity' : 2, 'value': 4},
        'i': { 'quantity' : 9, 'value': 1},
        'j': { 'quantity' : 1, 'value': 8},
        'k': { 'quantity' : 1, 'value': 5},
        'l': { 'quantity' : 4, 'value': 1},
        'm': { 'quantity' : 2, 'value': 3},
        'n': { 'quantity' : 6, 'value': 1},
        'o': { 'quantity' : 8, 'value': 1},
        'p': { 'quantity' : 2, 'value': 3},
        'q': { 'quantity' : 1, 'value': 10},
        'r': { 'quantity' : 6, 'value': 1},
        's': { 'quantity' : 4, 'value': 1},
        't': { 'quantity' : 6, 'value': 1},
        'u': { 'quantity' : 4, 'value': 1},
        'v': { 'quantity' : 2, 'value': 4},
        'w': { 'quantity' : 2, 'value': 4},
        'x': { 'quantity' : 1, 'value': 8},
        'y': { 'quantity' : 2, 'value': 4},
        'z': { 'quantity' : 1, 'value': 10},
        '*': { 'quantity' : 2, 'value': 0}
        }

"""
3. Oblicz ile wynosi suma wszystkich punktów na wszystkich kostkach w grze
Scrubble.
"""


"""
4. Korzystając z funkcji `permutations` z biblioteki `itertools` wypisz wszystkie
możliwe "słowa", które można ułożyć z liter z tablicy tiles.
"""

tiles = ['c','o','n','t','a','i','n']


"""
5. Napisz program, który wskaże, czy który gracz wygrał (Albo jest remis) w
poniższych grach "kołko i krzyżyk". Spacja oznacza wolne pole, które jeszcze
nie zostało zajęte.
"""

board_1 = [['x', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_2 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_3 = [[' ', 'o', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_4 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'x']]

board_5 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', ' ']]
