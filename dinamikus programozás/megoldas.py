def max_pages(n, x, prices, pages):
    # DP tömb létrehozása, amely a költségkeret szerinti maximális oldalszámokat tárolja
    dp = [0] * (x + 1)

    # A könyveken való végighaladás
    for i in range(n):
        price = prices[i]
        page = pages[i]

        # Visszafelé iterálás az árrésen belül, hogy ne használjuk ugyanazt a könyvet többször
        for j in range(x, price - 1, -1):
            dp[j] = max(dp[j], dp[j - price] + page)

    # A maximális oldalszám visszaadása a költségkereten belül
    return dp[x]

# Bemenet beolvasása
import sys
input = sys.stdin.read
data = input().splitlines()

# Első sor beolvasása: n és x
n, x = map(int, data[0].split())

# Második sor beolvasása: könyvek árai
prices = list(map(int, data[1].split()))

# Harmadik sor beolvasása: könyvek oldalszámai
pages = list(map(int, data[2].split()))

# Eredmény kiírása
print(max_pages(n, x, prices, pages))
