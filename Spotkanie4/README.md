# Mid season challange

Czyli szukamy wyjścia z labiryntu.


## Zadanie domowe
1. Napisać funkcję, która rekurencyjnie odwróci listę

        my_list = [1, 2, 3, 4]
        rev(my_list)  => [4,3,2,1]

czyli standard, ale niech rekurencja się w  bebechach pojawi ;)


2. Napisać funkcję, która jako argument przyjmuje string składający się z samych nawiasów (np `‘(){}[]’`)
i sprawdzi, czy nawiasy są poprawnie sparowane:

    valid_brackets(‘(([[{}]]))’) => zwróci True
    valid_brackets(‘{[}]()’) => zwróci False
    valid_brackets(‘{(){}[]}’) => zwróci True
