# Fa átmérője (Feladat leírás)

**Időkorlát:** 1.00 másodperc  
**Memóriakorlát:** 512 MB  

Adott egy fa, amely **n** csúcsból áll.  
A fa átmérője két csúcs közötti maximális távolság.  
A feladatod, hogy meghatározd a fa átmérőjét.

## Bemenet
- Az első sor tartalmaz egy egész számot, **n**-et: a csúcsok száma.
  A csúcsok számozása: 1, 2, ..., n.
- Ezután **n-1** sor következik, amelyek az éleket írják le.  
  Minden sor két egész számot tartalmaz, **a** és **b**, ami azt jelenti, hogy van egy él az **a** és **b** csúcs között.

## Kimenet
- Írj ki egy egész számot: a fa átmérőjét.

## Korlátok
- \(1 <= n <= 2 * 10^5\)  
- \(1 <= a, b <= n\)  

## Példa
### Bemenet:
```
5
1 2
1 3
3 4
3 5
```

### Kimenet:
```
3
```

### Magyarázat:
Az átmérő a következő útvonalnak felel meg:  
\(2 -> 1 -> 3 -> 5\).
