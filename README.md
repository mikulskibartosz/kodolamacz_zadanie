# kodolamacz_zadanie

## Kod używany w czasie zajęć

### Regex (moduł `re`)

https://regex101.com/

* match - https://python.astrotech.io/stdlib/regex/re-match.html#re-match
* search - https://python.astrotech.io/stdlib/regex/re-search.html
* findall - https://python.astrotech.io/stdlib/regex/re-find.html#re-findall-finditer
* split - https://python.astrotech.io/stdlib/regex/re-split.html#re-split
* praca z grupami - https://python.astrotech.io/stdlib/regex/re-group.html

### Klasy i obiekty

* https://blog.finxter.com/object-oriented-programming-terminology-cheat-sheet/ (prawie) cały obiektowy Python na jednej kartce A4
* metody `__str__` oraz `__repr__` - https://python.astrotech.io/basics/oop/stringify.html#id1
* `@dataclass` - https://python.astrotech.io/stdlib/dataclass/about.html#dataclass-about

### Pliki

* ścieżki do plików - https://python.astrotech.io/basics/files/path.html#file-path
* zapis do plików - https://python.astrotech.io/basics/files/write.html#file-write
* odczyt z plików - https://python.astrotech.io/basics/files/read.html#file-read
* pickle - https://python.astrotech.io/stdlib/pickle/file.html#pickle-file

### Generatory

* funkcje `filter`, `map`, oraz (dodatkowo) `reduce` - https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
* `yield` - https://python.astrotech.io/advanced/generator/function.html#generator-function

### Daty

* parsowanie/formatowanie dat - https://dev.to/maikomiyazaki/python-date-time-conversion-cheatsheet-3m69
* parametry `strftime`/`strptime` - https://strftime.org/
* timedelta - https://python.astrotech.io/stdlib/datetime/timedelta.html#datetime-time-deltas
* strefy czasowe - https://python.astrotech.io/stdlib/datetime/timezones.html#datetime-timezone

## Praca w grupach

### Założenia

Celem zadań jest utrwalenie użycia pokazanych do tej pory elementów Pythona.

1. **Używamy tylko funkcji pokazanych do tej pory na zajęciach**. Wiekszość zadań można łatwo rozwiązać używając biblioteki Pandas. Proszę tego nie robić ;)
2. **Przed** napisaniem kodu, piszemy testy!
3. Używamy repozytorium na Githubie.
4. Praca w grupach 3-4 osobowych.
5. W pliku znajdują się wiersze zawierające znak ", proszę je pominąć. (np używająć funkcji `filter`)

### Zadania

1. Proszę wczytać plik i wyświetlić pierwsze 10 nazw produktów posortowane w kolejności alfabetycznej.
1. Dla każdego wiersza w pliku, proszę policzyć całkowitą cenę zakupu: `pieces_sold * price_per_item`. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć liczbę sprzedanych produktów w każdym ze sklepów i zwrócić ją jako listę krotek `(nazwa_sklepu, liczba_produktow)` posortowaną malejąco wg liczby produktów. Wiersze z pustą nazwą sklepu należy pominąć. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć sumę cen `pieces_sold * price_per_item` w każdym z kwartałów. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć liczbę produktów sprzedanych w weekendy (https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday).
1. Proszę policzyć liczbę dni między pierwszym i ostatnim zakupem w każdym ze sklepów. Wiersze z pustą nazwą sklepu należy pominąć.
1. Niektóre nazwy produktów składają się z dwóch części: `Kategoria - Nazwa/Opis` (np. `Tea - Apple Green Tea`, `Ham - Smoked, Bone - In`). Proszę policzyć liczbę **unikalnych** produktów w każdej z kategorii. Produkty bez kategorii proszę zignorować. W wyniku oczekujemy listy krotek: `(kategoria, liczba_produktow)` posortowanej malejąco wg liczby produktów. Uwaga: niektóre produkty zawierają więcej niż jeden myślnik!
