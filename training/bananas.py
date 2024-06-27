

def somat(k,w):
    if w == 1:
        return k 
    else:
        return k * w + somat(k,w-1)

k, n, w = map(int, input().split())
if somat(k,w) - n >= 0:
    print((somat(k,w) - n ))
else:
     print(0)