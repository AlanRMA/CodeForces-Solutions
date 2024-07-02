
t = int(input())

for _ in range(0,t):
    x, y  = map(int, input().split())
    if y < -1:
        print("NO")
    elif x == 0 and y == 0:
        print("NO")
    else:
        print("YES")