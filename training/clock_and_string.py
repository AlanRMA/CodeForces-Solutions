def isBetween(target,a,b):
    if (target > a and target < b) or (target > b and target < a):
        return True
    else:
        return False

t = int(input())


for _ in range(t):
    a, b, c, d = map(int, input().split())
    # Cruzam
    if (isBetween(c,a,b) and not isBetween(d,a,b)) or (isBetween(d,a,b) and not isBetween(c,a,b)):
        print("YES")
    else:
        print("NO")

