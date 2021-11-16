aluno = {}

aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Media do {aluno['nome']}: "))

if aluno["media"] >= 6.5 and aluno["media"] <= 10:
    aluno["situacao"] = "aprovado"
elif aluno["media"] >= 6 and aluno["media"] < 6.5:
    aluno["situacao"] = "recuperação"
elif aluno["media"] <= 6 and aluno["media"] >= 0:
    aluno["situacao"] = "reprovado"
else:
    aluno["situacao"] = "inválida"

print(
    f"O aluno {aluno['nome']} teve sua média {aluno['media']} e sua situação é {aluno['situacao']}")
