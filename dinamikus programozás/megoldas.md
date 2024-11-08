- DP Tömb: Az dp[j] tömb értéke a j költségkeret alatt elérhető maximális oldalszámot tárolja.
-  Iteráció Visszafelé: Minden könyv esetén visszafelé iterálunk a dp tömbben, hogy biztosítsuk, hogy minden könyvet legfeljebb egyszer használunk fel.
- DP Frissítés: Az aktuális könyv (price, page) hozzáadása után a maximális oldalszámot aktualizáljuk, ha nagyobb értéket kapunk.
- A megoldás a részproblémákat (kisebb költségkeretekre vonatkozó maximális oldalszámot) tárolja, hogy újra felhasználja őket.
  Minden részprobléma megoldása hozzájárul a végső megoldáshoz, így a probléma teljes megoldása a kisebb részproblémák eredményére épül.

- Futásidő: O(xn)

A dp[j] érték azt tárolja, hogy legfeljebb j összköltség mellett mennyi a maximálisan elérhető oldalszám, ha a könyvek egy részét választjuk ki.
Azaz dp[j] a költségkeret j értékénél elérhető legnagyobb oldalszámot jelenti.

dp[j - price] + page jelentése:

 - price és page egy adott könyv ára és oldalszáma.
 - dp[j - price] azt az értéket tárolja, amelyet akkor tudunk elérni, ha az aktuális költségkeret (j) előtt a könyv árát (price) már felhasználtuk.
 - dp[j - price] + page így azt jelenti, hogy ha megvesszük ezt a könyvet, akkor mennyi oldalszámunk lenne összesen.
 - Ezzel kiszámítjuk, hogy ha ezt a könyvet is megvesszük, mekkora lenne az elérhető oldalszám az aktuális j költségkeret mellett.

-max(dp[j], dp[j - price] + page) jelentése:

Ezzel a max függvénnyel eldöntjük, hogy érdemes-e az adott könyvet megvenni a maximális oldalszám elérése érdekében.
Ha dp[j - price] + page nagyobb, mint a dp[j] jelenlegi értéke, akkor érdemes megvenni a könyvet, mert több oldalt tudunk összegyűjteni.
Ha dp[j] nagyobb vagy egyenlő, akkor nem érdemes megvenni, mert már van egy jobb megoldásunk az adott költségkeretre.
