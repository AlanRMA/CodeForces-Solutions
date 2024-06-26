# Tenta fazer operacão de troca de cartas otimizada
# cada operação bem sucedida diminui em 1 o número de cartas na mão do jogador
# ao final das tentativas, retornar o número de cartas na mão do jogador

t = int(input())

for _ in range(t):
    # na primeira linha vem n e k, na segunda linha as cartas.
    n, k = map(int, input().split())
    hand = list(map(int, input().split()))
    if k > n:
        print(n)
    else:
        minimum = False
        for card in hand:
            if hand.count(card) >= k:
                minimum = True
        if minimum:
            print(k-1)
        else:
            print(n)
