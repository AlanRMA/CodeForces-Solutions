





t = int(input())

for i in range(t):
    ram_upload, window = list(map(int, input().split()))
    if window == 1:
        print(window * ram_upload)
    if window > 1:
        print(((ram_upload - 1) * window) + 1)