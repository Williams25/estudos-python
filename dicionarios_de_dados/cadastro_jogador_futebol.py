jogadores = []
gols = []
dados = {}

while True:
    gols.clear()
    dados.clear()

    dados["nome"] = str(input("Nome: "))
    dados["partidas"] = int(
        input(f"Quantas partidas o jogador {dados['nome']} jogou? "))

    for i in range(0, dados["partidas"]):
        gols.append(int(input(f"Gols na partida {i+1}: ")))

    dados["gols"] = gols[:]
    dados["total_gols"] = sum(gols)

    jogadores.append(dados.copy())

    while True:
        resposta = str(input("quer continuar? [S/N] "))
        if resposta in "NnSs":
            break
        print("Erro digite apenas S ou N")
    if resposta in "Nn":
        break


print(jogadores)

print('-='*30)
print(f"{'Cod.':<4} {'Nome':<8} {'Gols':^8} {'total':>8}")
print('-='*30)

for index, value in enumerate(jogadores):
    print(
        f"{index:<4} {jogadores[index]['nome']:<8} {jogadores[index]['gols']} {jogadores[index]['total_gols']:>8}")
print('-='*30)

while True:
    index = int(
        input("Qual jogador que ver os detalhes? [999 para parar] "))

    if index == 999:
        break
    elif index != 999 and index > len(jogadores)-1:
        print("Erro digite um valor valido")
    else:
        for i, value in enumerate(jogadores[index]['gols']):
            print(
                f" No jogo {i+1} o jogador {jogadores[index]['nome']} fez {value} gols")
