# Pliki / algorytmy


## Zadania

### Fix indent

Wczytaj plik `file_to_read` wstawiając w każdej linii tyle spacji ile wynosi kolejny element listy
z ostatniej linijki pliku.

### 2 twarze Fibonacciego

Napisz funkcję obliczającą kolejny element ciągu Fibonacciego rekurencyjnie oraz za pomocą generatora.

### Sortowanie bąbelkowe :bath:

Posortuj listę używając sortowania bąbelkowego.


## Zadanie domowe

### Flat pickle jar

Napisz funkcję

    def flatten(li)

która wylistuje wszystkie pojedyncze elementy (bez kluczy), albo listę tych elementów.

**HINT:** rekurencja

### List file

Napisz funkcję

    def list_files()

która dostaje ścieżkę do folderu pierwszego, ma tam zajrzeć i wylistować jego zawartość.
Dla podfoderów ma również zajrzeć do środka i wylistować zawartość, i tak do skutku.
Nie trzeba wypisywać katalogów (lub wypisywać ale ze /). Dodatkowy punk za dodanie wciącia
z każdym nowym poziomem, np:

```
folder/
    1.txt
    2.jpg
    folder2/
        a.wav
```