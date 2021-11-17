### Condições aninhadas

- `emprestimo.py` Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

```py
class Emprestimo:
    def __init__(self, casa, salario, anos):
        self.casa = casa
        self.salario = salario
        self.anos = anos
        self.prestacao = casa / (anos * 12)
        self.minimo = salario * 30 / 100

    def validar_emprestimo(self):
        if self.prestacao <= self.minimo:
            print("Emprestimo concedido")
        else:
            print("Emprestimo não aprovado")


casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual seu salario? R$"))
anos_a_pagar = int(input("Em quantos anos quer pagar? "))

prestacao = casa / (anos_a_pagar * 12)
minimo = salario * 30 / 100

emprestimo = Emprestimo(casa, salario, anos_a_pagar)
emprestimo.validar_emprestimo()

print("Para pagar a casa de R${:.2f} em {} anos".format(
    emprestimo.casa, emprestimo.anos))
print("o valor será de R${:.2f}".format(emprestimo.prestacao))
```

- `base_conversao.py` Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

```py
class Conversao:
    def __init__(self, num, opcao):
        self.num = num
        self.opcao = opcao

    def conversao(self):
        if opcao == 1:
            print("{} convertido para binário é igual a {}".format(
                self.num, bin(self.num)[2:]))
        elif opcao == 2:
            print("{} convertido para octal é igual a {}".format(
                  self.num, oct(self.num)[2:]))
        elif opcao == 3:
            print("{} convertido para hexadecimal é igual a {}".format(
                  self.num, hex(self.num)[2:]))
        else:
            print("opção {} inválida".format(
                  self.opcao))
```

- `comparando_numeros.py` Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

  - O primeiro valor é maior
  - O segundo valor é maior
  - Não existe valor maior, os dois são iguais.

```py
  class ComparandoNumeros:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def comparando(self):
        if self.num1 > self.num2:
            print("o primeiro numero {} é maior que o segundo numero {}". format(
                self.num1, self.num2))
        elif self.num1 < self.num2:
            print("o segundo numero {} é maior que o primeiro numero {}". format(
                self.num2, self.num1))
        elif self.num1 == self.num2:
            print("o primeiro numero {} é igual o segundo numero {}". format(
                self.num1, self.num2))
        else:
            print("aconteceu algo inesperado")
```

- `alistamento_militar.py` Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

```py
class AlistamentoMilitar:
    def __init__(self, ano):
        self.ano = ano
        self.ano_atual = datetime.now().year
        self.idade = datetime.now().year - ano

    def alistar(self):
        if self.idade > 18:
            print("já passou o tempo de se alistar, voce esta atrasado {} ano(s)".format(
                self.ano_atual-self.ano))
        elif self.idade < 18:
            print("ainda não esta no tempo de se alistar falta {} ano(s)".format(
                self.ano_atual-self.ano))
        elif self.idade == 18:
            print("já esta no limite do tempo de se alistar")
```

- `media.py` Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
  - Média abaixo de 5.0: REPROVADO
  - Média entre 5.0 e 6.9: RECUPERAÇÃO
  - Média 7.0 ou superior: APROVADO

```py
class Media:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0

    def calcular(self):
        self.media = (self.nota1 + self.nota2) / 2

        if self.media >= 7.0 and self.media <= 10.0:
            print("aprovado sua media é {}".format(self.media))
        elif self.media >= 5.0 and self.media <= 6.9:
            print("recuperação sua media é {}".format(self.media))
        elif self.media < 5.0:
            print("reprovado sua media é {}".format(self.media))
        else:
            print("ocorreu um erro ao calcular sua media")
```

- `massa_corporal.py` Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
  - IMC abaixo de 18,5: Abaixo do Peso
  - Entre 18,5 e 25: Peso Ideal
  - 25 até 30: Sobrepeso
  - 30 até 40: Obesidade
  - Acima de 40: Obesidade Mórbida

```py
class MassaCorporal:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.massa = 0

    def imc(self):
        self.massa = self.peso / (self.altura**2)

        if self.massa < 18.5:
            print("abaixo do peso, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 18.5 and self.massa <= 25:
            print("peso ideal, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 25 and self.massa <= 30:
            print(
                "esta em sobrepeso, sua massa é de {:.1f}". format(self.massa))
        elif self.massa >= 30 and self.massa <= 40:
            print(
                "esta em obesidade, sua massa é de {:.1f}". format(self.massa))
        else:
            print(
                "esta em obesidade morbida, sua massa é de {:.1f}". format(self.massa))
```

- `gerenciar_pagamento.py` Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
  - à vista dinheiro/cheque: 10% de desconto
  - à vista no cartão: 5% de desconto
  - em até 2x no cartão: preço formal
  - 3x ou mais no cartão: 20% de juros

```py
class GerenciarPagamento:
    def __init__(self, preco, opcao):
        self.preco = preco
        self.opcao = opcao
        self.total = 0
        self.parcela = 0

    def calcularValor(self):
        if self.opcao == 1:
            self.total = self.preco - (self.preco * 10 / 100)

            print("sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(
                self.preco, self.total))
        elif self.opcao == 2:
            self.total = self.preco - (self.preco * 5 / 100)

            print("sua compra de R$ {:.2f} vai custar R$ {:.2f}".format(
                  self.preco, self.total))
        elif self.opcao == 3:
            self.total = self.preco
            self.parcela = self.total / 2

            print("sua compra de R$ {:.2f} vai ser parcelada em 2x de R$ {:.2f}".format(
                self.total, self.parcela))
        elif self.opcao == 4:
            total_parcelas = int(input("quantas parcelas? "))
            self.total = self.preco + (self.preco * 20 / 100)
            self.parcela = self.total / total_parcelas

            print("sua compra de R$ {:.2f} vai ser parcelada em {}x de R$ {:.2f}".format(
                self.total, total_parcelas, self.parcela))
        else:
            print("ocorreu um erro tente novamente selecione as opções entre 1 a 4")

```

- `jokenpo.py` Crie um programa que faça o computador jogar Jokenpô com você.

```py
from random import randint
from time import sleep


class Jokenpo:
    def __init__(self, opcao=1):
        self.itens = ("Pedra", "Papel", "Tesoura")
        self.random = randint(0, 2)
        self.opcao = opcao - 1  # 1,2,3

    def jogar(self):
        if self.opcao >= 0 and self.opcao <= 2:
            self.start()
            print("-=" * 11)
            print("Computador jogou {}".format(self.itens[self.random]))
            print("Voce jogou {}".format(self.itens[self.opcao]))
            print("-=" * 11)

            if self.opcao == self.random:
                print("{} Empate {}".format('💢'*11, '💢'*11))
            elif self.opcao == 0 and self.random == 1:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            elif self.opcao == 0 and self.random == 2:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 1 and self.random == 0:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 1 and self.random == 2:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            elif self.opcao == 2 and self.random == 1:
                print("{} Vitoria {}".format('✨'*11, '✨'*11))
            elif self.opcao == 2 and self.random == 0:
                print("{} Derrota {}".format('❌'*11, '❌'*11))
            else:
                print("ocorreu um erro inesperado, tente novamente")
        else:
            print("Opção invalida jogue novamente e escolha entre 1 e 3")

    def start(self):
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO")
        sleep(1)


print('''
  [1] Pedra
  [2] Papel
  [3] Tesoura
''')

opcao = int(input("Qual a sua jogada? "))

jokenpo = Jokenpo(opcao)
jokenpo.jogar()
```
