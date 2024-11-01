
## Feladat

Egy egész számokat tartalmazó tömb és egy célérték adott. Határozd meg, hogy hány olyan elem-pár van a tömbben, amelyek különbsége egyenlő a célértékkel.

### Példa

```
k = 1
arr = [1, 2, 3, 4]
```

Három olyan érték van, amelyek különbsége \( k = 1 \): 2 - 1 = 1, 3 - 2 = 1, és 4 - 3 = 1. Az eredmény 3.

### Funkcióleírás

Készítsd el a `pairs` függvényt.

A `pairs` függvény a következő paraméterekkel rendelkezik:

- `int k`: egy egész szám, a célkülönbség
- `int arr[n]`: egy egész számokat tartalmazó tömb

#### Visszatérési érték

- `int`: azon párok száma, amelyek megfelelnek a feltételnek.

### Bemenet Formátum

Az első sor két szóközzel elválasztott egész számot tartalmaz, \( n \) és \( k \)-t, amelyek a tömb méretét és a célértéket jelentik.

A második sor \( n \) szóközzel elválasztott egész számot tartalmaz, amelyek az `arr` tömb elemei.

### Megkötések

- \( 2 \leq n \leq 10^5 \)
- \( 0 < k < 10^9 \)
- \( 0 < arr[i] < 2^{31} - 1 \)
- minden `arr[i]` elem egyedi lesz
