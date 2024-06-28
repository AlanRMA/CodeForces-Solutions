




nickname = input()

split_nick = []
for i in nickname:
    if i not in split_nick:
        split_nick.append(i)

if len(split_nick) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM")