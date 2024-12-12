def count_rounds(n, arr):
    # Tároljuk az egyes számok pozícióit
    positions = [0] * n
    for i, num in enumerate(arr):
        positions[num - 1] = i

    # Számláljuk a köröket
    rounds = 1
    for i in range(1, n):
        if positions[i] < positions[i - 1]:
            rounds += 1
    print(positions)
    return rounds

# Példa input
n = int(input())
arr = list(map(int, input().split()))
print(count_rounds(n, arr))
