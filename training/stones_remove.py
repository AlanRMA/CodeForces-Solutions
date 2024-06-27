



rock_number = int(input())
rock_seq = input()
to_remove = 0
for i in range(len(rock_seq)-1):
    if rock_seq[i] == rock_seq[i+1]:
        to_remove += 1

print(to_remove)