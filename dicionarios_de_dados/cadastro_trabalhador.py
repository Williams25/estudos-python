from datetime import datetime

cadastro = {}

cadastro["nome"] = str(input("Nome: "))
cadastro["ano_nascimento"] = int(input("Ano de nascimento: "))
cadastro["idade"] = datetime.now().year - cadastro["ano_nascimento"]
cadastro["ctps"] = int(input("Carteira de trabalho (0 não tem): "))

if cadastro["ctps"] != 0:
    cadastro["ano_contratacao"] = int(input("Ano de contratação: "))
    cadastro["salario"] = float(input("Salario R$: "))
    cadastro["aposentadoria"] = cadastro["idade"] + \
        ((cadastro["ano_contratacao"] + 35) - datetime.now().year)

    print(
        f"O trabalhador {cadastro['nome']} tem {cadastro['idade']}", end=" ")
    print(f"anos sua carteira de trabalho é {cadastro['ctps']}", end=" ")
    print(
        f"e seu salario é de {cadastro['salario']} e vai se aposentar com {cadastro['aposentadoria']} anos")
