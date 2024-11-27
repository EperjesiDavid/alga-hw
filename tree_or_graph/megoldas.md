# Fa Átmérőjének Számítása Pythonban

## **A probléma áttekintése**
A feladatban egy **fa** átmérőjét kell kiszámítanunk. A fa átmérője két csúcs közötti maximális távolságot jelenti, ahol a távolság az őket összekötő leghosszabb úton lévő élek száma.

---

## **A kód működése**

### **1. Bemenet feldolgozása**

```python
from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])  # Csúcsok száma
edges = [tuple(map(int, line.split())) for line in data[1:]]  # Az összes élt beolvassuk
```

- Az első sorban kapjuk meg a fa **csúcsainak számát** (\( n \)).
- A következő \( n-1 \) sorban az **élek** találhatók, amelyek azt írják le, mely csúcsok között van él.
- Ezeket a bemeneteket listába (`edges`) töltjük, hogy később szomszédsági listává alakítsuk.

---

### **2. Gráf reprezentáció (szomszédsági lista)**

```python
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

- A gráfot **szomszédsági listával** tároljuk, mivel hatékonyan reprezentálja a csúcsok közötti kapcsolatokat, különösen nagy gráfok esetén.
- `graph` egy `defaultdict`, ahol minden csúcs (kulcs) egy listát tartalmaz, amely a hozzá közvetlenül kapcsolódó csúcsokat (szomszédokat) tartalmazza.
- Az élek kétirányúak (fa esetében mindig így van), ezért mindkét irányban hozzáadjuk őket.

Például a következő élek:
```
1 2
1 3
3 4
3 5
```
ezt a szomszédsági listát eredményezik:
```python
graph = {
    1: [2, 3],
    2: [1],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}
```

---

### **3. Szélességi keresés (BFS)**

#### A BFS célja
- A BFS egy gráf bejárására szolgáló algoritmus, amely rétegenként halad a kezdőcsúcsból kiindulva.
- Ebben a feladatban a BFS-t arra használjuk, hogy megtaláljuk a legnagyobb távolságra lévő csúcsot egy adott kezdőcsúcstól.

```python
def bfs(start):
    visited = [-1] * (n + 1)  # -1: még nem látogatott csúcsok
    queue = deque([start])
    visited[start] = 0  # A kezdőcsúcs távolsága 0
    farthest_node = start
```

- **`visited` lista**: Nyilvántartjuk, hogy egy csúcsot meglátogattunk-e. Az érték a kezdőcsúcstól való távolságot tárolja.
- **`queue`**: Egy sor, amelyben az éppen feldolgozásra váró csúcsok vannak. Ez segíti a rétegenkénti feldolgozást.

---

#### BFS algoritmus lépései
```python
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # Ha még nem látogattuk meg
                visited[neighbor] = visited[current] + 1  # Távolság frissítése
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:  # Legtávolabbi csúcs frissítése
                    farthest_node = neighbor

    return farthest_node, visited[farthest_node]
```

1. **Amíg a sor nem üres**, folytatjuk a feldolgozást:
    - **Első csúcs kivétele**: Az aktuális csúcsot feldolgozzuk.
    - **Szomszédok bejárása**: Megnézzük az összes szomszédját (akikkel közvetlen éle van).
    - Ha egy szomszédot még nem látogattunk meg:
        - Frissítjük a szomszéd távolságát.
        - Hozzáadjuk a sorhoz feldolgozásra.
        - Frissítjük a legtávolabbi csúcsot, ha szükséges.

2. A **legtávolabbi csúcsot és annak távolságát** adjuk vissza.

---

### **4. Kétszeri BFS a fa átmérőjéhez**

#### Első BFS
```python
farthest_node1, _ = bfs(1)
```
- Az 1-es csúcsról elindítunk egy BFS-t.
- Ennek célja, hogy megtaláljuk a fától legtávolabbi csúcsot (\( u \)).

#### Második BFS
```python
_, diameter = bfs(farthest_node1)
```
- A legtávolabbi csúcsról (\( u \)) új BFS-t indítunk.
- Az ebben a BFS-ben talált legtávolabbi távolság lesz a **fa átmérője**.

---

### **5. Az eredmény kiírása**

```python
print(diameter)
```
- Az átmérőt kiírjuk.

---

## **Hogyan működik?**

### **Miért működik a kétszeri BFS?**
1. Egy fában az átmérő mindig két levélcsúcs (végpont) között helyezkedik el.
2. Az első BFS biztosítja, hogy megtaláljuk az átmérő egyik végpontját \( u \).
3. A második BFS pedig garantálja, hogy megtaláljuk az \( u \)-tól legtávolabbi csúcsot \( v \), amely az átmérő másik végpontja. A távolságuk az átmérő.

---

## **Hatékonyság**
- Az algoritmus **O(n)** időben fut, mivel a BFS minden csúcsot és élt egyszer látogat meg.
- Ez hatékony, és a megadott korlátok \( n <= 200,000 \) mellett jól működik.

---

## **Példa bemenet és futás**

### Bemenet:
```
5
1 2
1 3
3 4
3 5
```

### Első BFS (1-től):
- Látogatott csúcsok: [1, 2, 3, 4, 5].
- Legtávolabbi csúcs: 4.

### Második BFS (4-től):
- Látogatott csúcsok: [4, 3, 1, 5, 2].
- Legtávolabbi csúcs: 5.
- Átmérő: 3.

### Kimenet:
```
3
```
