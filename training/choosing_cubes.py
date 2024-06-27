# Brainstorm
# n é o número de cubos, f é o enésimo cubo favorito na sequência 
# e k é o número de cubos que serão removidos após ordená-los

# Casos de teste
t = int(input())

# Processando os casos de teste
for _ in range(0,t):
    n, f, k = map(int, input().split())
    seq = list(map(int, input().split()))
    favorite = seq[f-1]
    seq.sort()
    seq.reverse()
    result = ""
    for i in range(k):
        if seq[i] == favorite:
            result = "Maybe"
    if result == "Maybe" and favorite in seq[k:]:
        result = "Maybe"
    elif result == "Maybe" and favorite not in seq[k:]:
        result = "Yes"
    else:
        result = "No"
    print(result)