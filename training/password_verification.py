def verify(password):
    for i in range(len(password)-1):
        first = password[i]
        second = password[i+1]
        if (first.isdigit() or first.isalpha() or second.isdigit() or second.isalpha()) and (first < second):
            pass #Aprovado por enquanto
        if first.isalpha() and second.isdigit():
            return "NO"
        if (first.isdigit and second.isdigit()) and (first > second):
            return "NO"
        if (first.isalpha() and second.isalpha()) and (first > second):
            return "NO"
    return "YES"

t = int(input())

for _ in range(0,t):
    n= int(input())
    password = input()
    print(verify(password))




    