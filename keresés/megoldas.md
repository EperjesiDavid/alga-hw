1. Pozíciók meghatározása: Tároljuk el a számok pozícióit egy tömbben.
2. Iteráció az indexeken: Iteráljunk az 1-től n-ig, és állapítsuk meg, hogy mikor kell új kört kezdeni.
3. Új kör felismerése: Ha az aktuális szám pozíciója kisebb, mint az előző számé, akkor új kör szükséges.

  - Időbeli bonyolultság:

    A pozíciók meghatározása O(n)
    
    A körök számlálása O(n)
    
    Összesen: O(n)

   - Memóriabonyolultság:

  Az positions tömb miatt O(n)
