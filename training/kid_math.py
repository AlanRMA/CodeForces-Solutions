


str_math = input()

splited = str_math.split("+")
splited.sort()
result = ''
for num in splited:
    result += num
    result +="+"
        
print(result[:-1])