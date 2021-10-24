# kodolamacz_zadanie

## Założenia

Celem zadań jest utrwalenie użycia pokazanych do tej pory elementów Pythona.

1. **Używamy tylko funkcji pokazanych do tej pory na zajęciach**. Wiekszość zadań można łatwo rozwiązać używając biblioteki Pandas. Proszę tego nie robić ;)
2. **Przed** napisaniem kodu, piszemy testy!
3. Używamy repozytorium na Githubie.
4. Praca w grupach 3-4 osobowych.
5. W pliku znajdują się wiersze zawierające znak ", proszę je pominąć. (np używająć funkcji `filter`)

## Zadania

1. Proszę wczytać plik i wyświetlić pierwsze 10 nazw produktów posortowane w kolejności alfabetycznej.
1. Dla każdego wiersza w pliku, proszę policzyć całkowitą cenę zakupu: `pieces_sold * price_per_item`. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć liczbę sprzedanych produktów w każdym ze sklepów i zwrócić ją jako listę krotek `(nazwa_sklepu, liczba_produktow)` posortowaną malejąco wg liczby produktów. Wiersze z pustą nazwą sklepu należy pominąć. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć sumę cen `pieces_sold * price_per_item` w każdym z kwartałów. Brakująca wartość w kolumnie `pieces_sold` oznacza **jeden** produkt.
1. Proszę policzyć liczbę produktów sprzedanych w weekendy (https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday).
1. Proszę policzyć liczbę dni między pierwszym i ostatnim zakupem w każdym ze sklepów.
1. Niektóre nazwy produktów składają się z dwóch części: `Kategoria - Nazwa/Opis` (np. `Tea - Apple Green Tea`, `Ham - Smoked, Bone - In`). Proszę policzyć liczbę **unikalnych** produktów w każdej z kategorii. Produkty bez kategorii proszę zignorować. W wyniku oczekujemy listy krotek: `(kategoria, liczba_produktow)` posortowanej malejąco wg liczby produktów. Uwaga: niektóre produkty zawierają więcej niż jeden myślnik!
