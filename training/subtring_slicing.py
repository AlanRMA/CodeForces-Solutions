def encontrar_maiores_substrings(s):
    substrings = []
    n = len(s)
    i = 0
    
    while i < n:
        # Encontrar o começo da substring (deve ser 'A')
        if s[i] == 'A':
            j = i
            # Contar quantos 'A' seguidos existem
            while j < n and s[j] == 'A':
                j += 1
            # Encontrar o final da substring (deve ser 'B')
            k = j
            while k < n and s[k] == 'B':
                k += 1
            # Verificar se a substring é válida (tem pelo menos um 'A' e um 'B')
            if j > i and k > j:
                substrings.append(s[i:k])
                i = k  # Continuar a busca após o final desta substring
            else:
                i = j  # Continuar a busca após os 'A' encontrados
        else:
            i += 1
    
    return substrings

# Exemplo de uso
string1 = "ABABAB"
result1 = encontrar_maiores_substrings(string1)
print(result1)
