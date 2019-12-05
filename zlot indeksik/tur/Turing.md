# Turing

## Stany:

1. Początkowy, szukam a lub b, idąc w lewo, jeśli znajdę to idę w prawo i przechodzę w 2
2. zaznaczam początek znakiem X i przechodzę w 3
3. szukam "b", idąc w lewo. Jeśli nie ma b to idę w lewo i szukam dalej; jeśli jest "b" to zmieniam je na "z" i przechodzę w 4. jeśli jest znak pusty to przechodzę w 5
4. szukam liczby (lub znaku pustego, idąc w prawo. Jak ją znajdę to dodaje jeden. jeśli liczba jest = 9 to zamieniam ją na zero i idę w prawo, w innym przypadku przechodzę w 3
5. szukam X, idąc w prawo.
6. szukam "a", idąc w lewo. Jeśli nie ma a to idę w lewo i szukam dalej; jeśli jest "a" to zmieniam je na "z" i przechodzę w 7. jeśli jest znak pusty to przechodzę w 8
7. szukam liczby, idąc w prawo. Jak ją znajde to odejmuje jeden. Jeśli liczba = 0 to zmieniam ją na 9 i idę w prawo. jeśli znajduje znak pusty to przechodzę w 9
8. szukam cyfy > 0, idąc w prawo; jeśli ją znajde to zmieniam stan na 10; jeśli znajde tylko stan pusty to przechodzę w 11
9. szukam X idąc w lewo, zmieniam go na A
10. szukam X idąc w lewo, zmieniam go na B
11. szukam X idąc w lewo, zmieniam go na N

### Testing

``` 
nnnnnczczczczcczzzzzzzzczczczccczzccczzzcB40nn
```


