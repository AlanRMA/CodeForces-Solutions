



t = int(input())
resolutions = 0
for _ in range(t):
    lista = list(map(int, input().split()))
    if lista.count(1) >= 2:
        resolutions += 1

print(resolutions)