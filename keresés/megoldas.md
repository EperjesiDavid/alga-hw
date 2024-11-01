
## Megoldás magyarázata


1. **Hash Halmaz a Gyors Kereséshez**: Az összes elem tárolásával egy hash halmazban gyorsan ellenőrizhető, hogy egy adott elemhez hozzáadott vagy abból kivont \( k \) érték létezik-e a tömbben.

2. **Egyetlen Bejárásos Ellenőrzés**: Minden \( x \) elemre a tömbben:
   - Ellenőrizzük, hogy \( x + k \) létezik-e a halmazban. Ha igen, akkor ez egy párt jelent.
   - Ellenőrizhetjük \( x - k \)-t is (ha egyedi párokat keresünk, és számít az irány).

3. **Időbeli Komplexitás**: A hash halmaz használatával minden ellenőrzés átlagosan \( O(1) \) időben elvégezhető, így a teljes megoldás időbeli komplexitása \( O(n) \).




Ez a megközelítés sokkal optimálisabb, mint egy beágyazott ciklus, amely \( O(n^2) \) komplexitású lenne.
