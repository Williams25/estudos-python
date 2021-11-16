dados = {}
lista = []
mulheres = []
acima_media = []
media = 0

while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    dados["idade"] = int(input("Idade: "))

    while True:
        dados["sexo"] = str(input("Sexo [M/F]: "))
        if dados["sexo"] in "MmFf":
            break
        print("Erro digite apenas M ou F")

    lista.append(dados.copy())

    while True:
        resposta = str(input("quer continuar? [S/N] "))
        if resposta in "NnSs":
            break
        print("Erro digite apenas S ou N")

    if resposta in "Nn":
        break

for index, value in enumerate(lista):
    media += lista[index]['idade']

media = media / len(lista)

for index, value in enumerate(lista):
    if lista[index]['sexo'] in "Ff":
        mulheres.append(lista[index])
    if lista[index]['idade'] > media:
        acima_media.append(lista[index])

print(f" - foram cadastradas {len(lista)} pessoas")
print(f" - a media de idade é {media:0.0f} anos")

if len(mulheres) > 0:
    print(f"\n - lista de mulheres")
    for index, value in enumerate(mulheres):
        print(f"  - {mulheres[index]['nome'].upper()}")

if len(acima_media) > 0:
    print(f"\n - lista de pessoas com idade acima da media:")
    for index, value in enumerate(acima_media):
        print(
            f"  - {acima_media[index]['nome'].upper()} {acima_media[index]['idade']} anos sexo {acima_media[index]['sexo'].upper()}")
