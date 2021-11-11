lista = []
alunos = []

while True:
    lista.append(str(input("nome: ")))
    lista.append(float(input("nota 1: ")))
    lista.append(float(input("nota 2: ")))
    resposta = str(input("quer continuar? [S/N] "))

    alunos.append(lista[:])
    lista.clear()

    if resposta in "Nn":
        break

print('-'*26)
print(f"{'No.':<4}{'Nome':<10}{'Media':>8}")
print('-'*26)

for index, valor in enumerate(alunos):
    alunos[index].append((alunos[index][1] + alunos[index][2]) / 2)
    print(f"{index:<4}{valor[0]:<10}{valor[3]:>8.1f}")

print('-'*26)

while True:
    opcao = int(input("mostrar notas de qual aluno? (999 interromper)"))
    if opcao == 999:
        break
    if opcao <= len(alunos) - 1:
        print(f"Nota 1: {alunos[opcao][1]}, Nota 2: {alunos[opcao][2]}")
    else:
        print("opcao incorreta")
