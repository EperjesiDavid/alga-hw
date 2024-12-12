
#### **Probléma leírása**
Van \( n \) darab alma, amelyek súlyai adottak. A cél az, hogy ezeket az almákat két csoportra osszuk úgy, hogy a két csoport súlyának különbsége a lehető legkisebb legyen.

---

### **Algoritmus működése**
Az algoritmus egy rekurzív megközelítést alkalmaz, amely:
1. Minden egyes almát vizsgál, és eldönti, hogy az adott almát melyik csoportba helyezze.
2. Két lehetőséget próbál ki minden alma esetében:
   - Az alma az **első csoportba kerül** (így az első csoport súlya nő).
   - Az alma a **második csoportba kerül** (az első csoport súlya nem változik).
3. A végső megoldást úgy találja meg, hogy minden lehetséges elosztást kipróbál, és a két csoport közötti **minimális különbséget** választja.

---

### **Rekurzív logika**
Az algoritmus egy segédfüggvényt használ \(minimalis\_kulonbseg\_rekurziv \), amely a következő paramétereket kapja:
- **`index`**: Az aktuálisan vizsgált alma indexe a listában.
- **`jelenlegi_osszeg`**: Az első csoport súlyának eddigi összértéke.
- **`osszes_suly`**: Az almák teljes súlyának összege (változatlan minden rekurziós hívásnál).
- **`sulyok`**: Az almák súlyait tartalmazó lista.

#### **Alapeset**
- Ha az összes almát feldolgoztuk \( index == n \), akkor visszatérünk a két csoport súlyának különbségével:
  
 `abs(osszes_suly - 2 * jelenlegi_osszeg)`

 
  Ez a képlet az első csoport súlya \( jelenlegi\_osszeg \) és a második csoport súlya \( osszes\_suly - jelenlegi\_osszeg \) közötti különbséget adja meg.

#### **Rekurzív lépések**
1. Az aktuális almát az **első csoportba helyezzük**, így a \( jelenlegi\_osszeg \)-hez hozzáadjuk az alma súlyát.
2. Az aktuális almát nem helyezzük az első csoportba (ez esetben \( jelenlegi\_osszeg \) változatlan marad).
3. A két lehetőség közül kiválasztjuk azt, amelyik a minimális különbséget eredményezi:
   
 `min(benne_van, nincs_benne)`
 
   ahol:
   - **`benne_van`**: Az a minimális különbség, ha az alma az első csoportba kerül.
   - **`nincs_benne`**: Az a minimális különbség, ha az alma nem kerül az első csoportba.

---

### **Teljes algoritmus folyamata**
1. Az algoritmus a \( minimalis\_kulonbseg \) függvénnyel indul, amely:
   - Kiszámítja az összes alma súlyának összegét \( osszes\_suly = sum(sulyok) \).
   - Elindítja a rekurzív feldolgozást az első almával \( index = 0 \).
2. A rekurzív függvény minden egyes almánál meghívja önmagát mindkét lehetőségre (első vagy második csoportba helyezés).
3. Amikor elérjük az alapesetet, visszatér a két csoport közötti különbséggel.
4. A visszatérési értékekből minden rekurzív szinten a minimális különbség kerül továbbadásra.
5. Végül a gyökérszinten (amikor az első alma szintjére visszatérünk) az összes lehetséges elosztás közül a legkisebb különbséget kapjuk meg eredményként.

---

### **Idő- és térbeli komplexitás**
#### **Időbeli komplexitás**
A tisztán rekurzív megoldás **minden lehetséges csoportosítást** kipróbál. Ezért az időbeli komplexitása:
\[
O(2^n)
\]
Mivel \( n \) az almák száma, \( 2^n \) rekurzív hívás történik. 

#### **Térbeli komplexitás**
Az algoritmus maximális rekurziómélysége \( O(n) \), mivel legfeljebb \( n \) szint mélységig haladunk a rekurzív hívások során.

---

Habár ez az algoritmus működik \( n = 20 \)-ra, CSES tesztelésnél éppen lefut 1 mp-en belül, érdemes memoizációt vagy dinamikus programozást alkalmazni a hatékonyság javítása érdekében.

