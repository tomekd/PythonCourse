# Zadania


### Zad. 1
Sklonuj repozytorium https://github.com/tomekd/PythonCourseProject.git, o ile jeszcze tego nie zrobiłeś.

### Zad. 2
Zainstaluj bibliotekę ``(File > Settings > Project:PythonCourseProject > Project Interpreter)
 
 ### Zad. 3
Uruchom grę i zobacz jak ona działa, spróbuj ułożyć kilka słów. Nie przejmuj się, jeżeli komputer gra znacznie lepiej
od Ciebie.

### Zad. 4
Cały projekt składa się z 5 plików w katalogu `game`. Zaczynając od końca pliku `game_manager.py`,
spróbuj zrozumieć jak działa cały projekt: jakie są zależności między klasami, co wykonywało się
po kolei jak grałeś. Pamiętaj, że nie musisz wszystkiego rozumieć, żeby mieć ogólną wizję projektu.

### Zad. 5
Zamień plik `scrabble_players.py` na paczkę:
 1. Stwórz nową paczkę (`package`) w katalogu `game` i nazwij ją `players`.
 2. Dla każdej klasy w `scrabble_players.py`:
    * utwórz nowy plik w powyżej stworzonej paczce.
    * Nowy plik nazwij w taki sam sposób jak nazywa się klasa.
    * Przenieś definicje klasy do nowego pliku.
    * Dodaj brakujące importy. 
  3. Usuń plik `scrabble_players.py`.
  4. Popraw importy w pozostałych plikach projektu. Jeżeli wszystko zostało wykonane poprawnie,
  gra będzie zachowywać się tak samo jak wcześniej.
  
  ### Zad. 6 (pylint)
  1. Zainstaluj bibliotekę `pylint`, o ile jeszcze jej nie masz.
  2. Zainstaluj plugin do Pycharma o nazwie `pylint`. (File > Settings > Plugins) a następnie wyszukaj i 
  zainstaluj plugin. Po instalacji, zrestartuj Pycharma.
  3. Wejdź jeszcze raz do Ustawień i wyszukaj słowa `pylint`. W znalezionej zakładce, kliknij w test, żeby sprawdzić,
  czy plugin został poprawnie zainstalowany.
  4. Otwórz plik `game_manager.py` i uruchom na nim `pylint`.
  5. Usuń wszystkie błędy, jakie znalazł `pylint`.
  
  ### Zad. 7 (testy)
  1. Napisz test jednostkowy do klasy `HumanPlayer`, który sprawdzi, czy obiekt tej klasy tworzy się
  bez błędów.
  
  ### Zad. 8 (Doc-stringi)
1. Przeczytaj doc-stringi w w pliku `scrabble_box.py`. Czy są one pomocne w rozumieniu co robi dana
metody?
2. Dopusz brakujący dokc-string do metody `word_is_valid` w klasie `Rulebook`.

### Zad. 9 (lokalizacja gry)
W pliku `scrabble_box.py` w linii 112 jest zdefiniowana metoda `generate_dictionary_tree`.
1. Przeanalizuj co robi ta metoda.
2. Zobacz jak wygląda słownik, który ona wczytuje.
3. Napisz skrypt, który wczyta słownik, z którego korzystaliśmy na drugich zajęciach i przerobi
go do następującej postaci:
   * zamieni znaki `ę` na `e`, `ż` na `z`, itd. 
   * zamieni Wszystkie litery na wielkie.
   * zapisze wynik do nowego pliku.
4. Zmodyfikuj metodę `generate_dictionary_tree` w taki sposób, żeby wczytywała nowy słownik.