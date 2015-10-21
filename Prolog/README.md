# Prolog albo rozgrzewka


## Zadania

### Choinka :christmas_tree:
Napisz program do rysowania choinki z gwiazdek. Użytkownik podaje wysokość choinki, program rysuje trójkąt:

```
$ python choinka.py 3
  *
 ***
*****
```

```
$ python choinka.py 6
     *
    ***
   *****
  *******
 *********
***********
```

### Ramka

Napisz program do rysowania ramek wokół napisów. Użytkownik podaje tekst, program rysuje ramkę.
Pierwsza wersja dla jednej linii tekstu, bonus za wiele linii:

```
$ echo "foo" | python ramka.py
+-----+
| foo |
+-----+
```

```
$ echo "Zen\nof\nPython" | python ramka.py
+--------+
| Zen    |
| of     |
| Python |
+--------+
```

### FizzBuzz :honeybee:

Napisz program, który odlicza od 1 to N. Dla liczb podzielnych przez 3, wypisuje *Fizz*, dla podzielnych przez 5 wypisuje *Buzz*,
a dla podzielnych zarówno przez 3 jak i 5, wypisuje *FizzBuzz*:

```
$ python fizzbuzz.py 30
1
2
3 Fizz
4
5 Buzz
6 Fizz
7
8
9 Fizz
10 Buzz
11
12 Fizz
13
14
15 FizzBuzz
16
17
18 Fizz
19
20 Buzz
21 Fizz
22
23
24 Fizz
25 Buzz
26
27 Fizz
28
29
30 FizzBuzz
```

### Countdown :star: (zadanie z gwiazdką)

Napisz program, który przyjmuje datę i godzinę, a wyświetla ile pozostało do tej daty dni, godzin, minut i sekund:

```
$ python countdown.py "2015-03-18 18:40:23"
now: 2015-03-15 19:01-14
target: 2015-03-18 18:40:23
left: 2d 23h 39m 9s
```