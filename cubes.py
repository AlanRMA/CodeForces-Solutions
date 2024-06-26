t = int(input())  # lê o número de casos de teste

for _ in range(t):
    n, m = map(int, input().split())  # lê n e m para cada caso de teste
    if m > n:
        print("No")
    elif m % 2 == 0 and n % 2 == 0:
        print("Yes")
    elif m % 2 == 1 and n % 2 == 1:
        print("Yes")
    else:
        print("No")
