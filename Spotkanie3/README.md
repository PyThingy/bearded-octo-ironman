# Pliki / algorytmy


## Zadania

### Fix indent

Wczytaj plik `file_to_read` wstawiając w każdej linii tyle spacji ile wynosi kolejny element listy
z ostatniej linijki pliku.

### 2 twarze Fibonacciego

Napisz funkcję obliczającą kolejny element ciągu Fibonacciego rekurencyjnie oraz za pomocą generatora.

### Sortowanie bąbelkowe :bath:

Posortuj listę używając sortowania bąbelkowego.


## Zadanie domowe :runner:

### Flat pickle jar

Napisz funkcję

    def flatten(li)

która przujmie strukturę danych złożoną z list i słowników, a następnie wylistuje wszystkie pojedyncze elementy
(bez kluczy), albo listę tych elementów. Struktura danych powinna zostać wczytana z pliku przy pomocy `pickle`.

**HINT:** :bulb: rekurencja

### List file

Napisz funkcję

    def list_files()

która dostaje ścieżkę do folderu pierwszego poziomu i listuje zawartość jego oraz jego podkatalogów.
Można nie wypisywać nazw katalogów albo wypisywać ale ze */*. Dodatkowy punkt za dodanie wcięcia
z każdym nowym poziomem, np:

```
folder/
    1.txt
    2.jpg
    folder2/
        a.wav
```