# Lê o número de casos de teste
t = int(input())

# Para cada caso de teste
for _ in range(t):
    # Lê as strings a e b
    a, b = input().split()
    
    # Troca os primeiros caracteres de a e b
    swapped_a = b[0] + a[1:]
    swapped_b = a[0] + b[1:]
    
    # Imprime as strings após a troca
    print(swapped_a, swapped_b)
