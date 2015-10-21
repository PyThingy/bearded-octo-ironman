# Mid season challenge

## Zadanie

Mając labirynt dany w pliku `l1.txt`, znajdź drogę wyjścia z labiryntu. Dla ułatwienia, część
odpowiedzialna za wczytanie labiryntu została już dla Ciebie napisana w pliku `labirynth.py`.


## Zadanie domowe :runner:
1. Napisz funkcję, która rekurencyjnie odwróci listę:

        my_list = [1, 2, 3, 4]
        rev(my_list)  => [4,3,2,1]



2. Napisz funkcję, która jako argument przyjmuje *string* składający się z samych nawiasów (np `‘(){}[]’`)
i sprawdza, czy nawiasy są poprawnie sparowane:

        valid_brackets(‘(([[{}]]))’) => zwróci True
        valid_brackets(‘{[}]()’) => zwróci False
        valid_brackets(‘{(){}[]}’) => zwróci True
