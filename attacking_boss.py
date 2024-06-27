from sortedcontainers import SortedSet

# Recebe o número de casos de teste
t = int(input())

# Processa cada caso de teste
for _ in range(t):
    h, n = map(int, input().split())  # Recebe a vida do monstro e o número de ataques
    dmg_list = list(map(int, input().split()))  # Lista de danos dos ataques
    cd_list = list(map(int, input().split()))  # Lista de cooldown dos ataques

    next_turn = SortedSet()  # Conjunto ordenado para armazenar os próximos turnos disponíveis
    current_turn = 1
    total_damage = 0

    # Inicializa o conjunto com os ataques disponíveis no primeiro turno
    for i in range(n):
        next_turn.add((1, i))  # (próximo turno disponível, índice do ataque)

    # Processa até que a vida do monstro seja zero ou menor
    while h > 0:
        # Encontra o próximo turno em que ataques estão disponíveis
        while next_turn:
            next_available_turn, attack_index = next_turn.pop(0)  # Pega o primeiro elemento do conjunto
            if next_available_turn <= current_turn:
                total_damage += dmg_list[attack_index]
                next_turn.add((current_turn + cd_list[attack_index], attack_index))
            else:
                next_turn.add((next_available_turn, attack_index))
                break

        # Reduz a vida do monstro pelo dano total do turno atual
        h -= total_damage
        current_turn += 1

    # O loop termina quando h <= 0, mas o turno é incrementado uma vez a mais, então subtraímos 1
    print(current_turn - 1)
