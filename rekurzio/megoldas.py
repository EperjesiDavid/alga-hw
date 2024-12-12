def minimalis_kulonbseg_rekurziv(index, jelenlegi_osszeg, osszes_suly, sulyok):
    # Alapeset: ha az összes almát feldolgoztuk
    if index == len(sulyok):
        # Visszatérünk a két csoport súlyainak különbségével
        return abs(osszes_suly - 2 * jelenlegi_osszeg)

    # 1. lehetőség: Az aktuális almát az első csoportba tesszük
    benne_van = minimalis_kulonbseg_rekurziv(
        index + 1, jelenlegi_osszeg + sulyok[index], osszes_suly, sulyok
    )

    # 2. lehetőség: Az aktuális almát NEM tesszük az első csoportba
    nincs_benne = minimalis_kulonbseg_rekurziv(
        index + 1, jelenlegi_osszeg, osszes_suly, sulyok
    )

    # Visszatérünk a két lehetőség közül a kisebb különbséggel
    return min(benne_van, nincs_benne)

def minimalis_kulonbseg(sulyok):
    # Összes alma összsúlya
    osszes_suly = sum(sulyok)
    # Kezdjük a rekurziót az első almával
    return minimalis_kulonbseg_rekurziv(0, 0, osszes_suly, sulyok)

# Bemenet beolvasása
n = int(input())
sulyok = list(map(int, input().split()))

# Eredmény kiírása
print(minimalis_kulonbseg(sulyok))
