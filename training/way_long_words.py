

t = int(input())

for _ in range(t):
    word = str(input())
    if len(word) <= 10:
        print(word)
    else:
        alt_word = word[0] + str(len(word) - 2) + word[-1]
        print(alt_word)