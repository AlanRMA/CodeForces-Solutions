

def somat(k,w):
    if w == 1:
        return k 
    else:
        return k * w + somat(k,w-1)

k, n, w = map(int, input().split())
leftover = somat(k,w) - n
if leftover >= 0:
    print(leftover)
else:
     print(0)