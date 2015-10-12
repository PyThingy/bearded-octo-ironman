# Struktury danych

Czyli oswajamy listy, słowniki i pętle.

## Zadania

### Dict Maker
Napisz funkcję przyjmującą na wejściu string (np. `'ala'`) zwracającą na wyjściu słownik
z liczbą powtórzeń danego znaku z wejścia (w tym przypadku `{‘a’: 2, ‘l’:1}`).


### Dict Maker Collective
Zmodyfikuj rozwiązanie zadania 1. (*Dict Maker*) tak, żeby wykorzystany był moduł *collections* z biblioteki standardowej.

**HINT**

[collections.Counter](https://docs.python.org/2/library/collections.html#collections.Counter)

### Phone book :phone:
Zaimplementuj prostą książkę telefoniczną. Potrzebne są nam takie funkcjonalności jak:
* dodawanie nowego numeru telefonicznego dla danego imienia i nazwiska, struktura powinna wyglądać następująco:
        `{‘surname’: {‘name’: [‘12-32-21’, ...], ...}, …}`
* czyszczenie ksiązki telefonicznej
* mając na wejściu nazwisko, chcemy wyświetlić przypisane do niego numery oraz na końcu liczbę tych numerów (użyj generatorów!). Przykładowy output:

        xxx-xxx-xxx
        yyy-yyy-yyy
        2

Program powinien przechowywać cały czas stan książki i umożliwiać interakcję z użytkownikiem.
Załużmy, że na początku książka jest pustym słownikiem.

### Phone book 2.0 :ledger:
Struktura podana w poprzednim zadaniu nie jest do końca poprawna dla takiego problemu.
Czy można zaproponować inne rozwiązanie? (kolejność alfabetyczna i numery nie powinny się powtarzać)


## Zadanie domowe :runner:

1. Przeczytać wstęp o *ciągu Fibonacciego* ([wiki](http://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego)).
2. Spróbować napisać funkcję rekurencyjną obliczającą n-tą liczbę ciągu Fibonacciego.
Można oswoić się z tematem rekurencji korzystając np. z [Rekurencja](http://brain.fuw.edu.pl/edu/TI:Algorytmy_i_struktury_danych/Rekurencja).
3. Napisać wersję programu obliczającego n-tą liczbę ciągu z wykorzystaniem słownika lub listy.
Kolejne wyrazy ciągu trzymamy w strukturze - dzięki temu możemy zmniejszyć liczbę wywołań funkcji
