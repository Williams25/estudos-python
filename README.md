# Conceitos basicos de python

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

### Estruturas de repetição

- `contagem_regressiva.py` Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

```py
from time import sleep

class ContagemRegressiva:
    def __init__(self, numero=10):
        self.numero = numero

    def regressiva(self):
        for c in range(self.numero, 0, -1):
            sleep(1)
            print("{}".format(c))
        print("Fim")
```

- `contagem_de_pares.py` Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

```py
class ContagemPares:
    def __init__(self, numero=50):
        self.numero = numero

    def contagem(self):
        for c in range(0, self.numero + 1):
            if c % 2 == 0:
                print("o numero {} é par".format(c))
```

- `soma_impares.py` Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

```py
class SomaImpares:
    def __init__(self, numero=500):
        self.numero = numero

    def soma(self):
        acumulador = 0
        contador = 0
        for c in range(1, self.numero + 1, 2):
            if c % 3 == 0:
                acumulador = acumulador + c
                contador += 1
                print("o numero {} é multiplo pro 3".format(c))

        print("a soma dos valores multiplos por 3 é {}".format(acumulador))
        print("foram encontrados {} numeros multiplos por 3".format(contador))
```

- `tabuada.py` Faça um programa que calcule a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

```py
def tabuada(targert: int, rangeNumber: int) -> str:
    for i in range(rangeNumber + 1):
        print("{0} * {1} = {2}".format(targert, i, targert * i))
```

- `soma_pares.py` Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

```py
class SomaPares:
    def __init__(self, numero):
        self.numero = numero

    def soma(self):
        acumulador = 0
        contador = 0
        for c in range(1, self.numero + 1):
            if c % 2 == 0:
                acumulador = acumulador + c
                contador += 1
                print("o numero {} é par".format(c))

        print("a soma dos valores pares é {}".format(acumulador))
        print("foram encontrados {} numeros pares".format(contador))
```

- `progressao_aritimetica.py` Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

```py
class ProgressaoAritimetica:
    def __init__(self, termo, razao):
        self.termo = termo
        self.razao = razao

    def contarPA(self):
        decimo = self.termo + (10 - 1) * self.razao
        contador = 0
        for c in range(termo, decimo + razao, razao):
            contador += 1
            print("{} ".format(c), end="-> ")
        print("acabou, a progresão tem {} numeros".format(contador)
```

- `numeros_primos.py` Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

```py
class NumerosPrimos:
    def __init__(self, numero=0):
        self.numero = numero

    def primos(self):
        total = 0
        for c in range(1, self.numero+1):
            numero_primo = self.numero % c
            if numero_primo == 0:
                total += 1
                print("\033[33m", end=' ')
            else:
                print("\033[31m", end=' ')
            print("{}".format(c), end=' ')

        if total == 2:
            print("\n\033[mo numero {} é primo ele foi dividido {}x".format(
                self.numero, total))
        else:
            print("\n\033[mo numero {} não é primo".format(self.numero))
```

- `palindromo.py` Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

```py
class Palindromo:
    def __init__(self, frase=""):
        self.frase = frase.strip().upper()
        self.palavras = self.frase.split()
        self.palavra = "".join(self.palavras)
        self.palavra_inversa = ""

    def palindromo(self):
        for letra in range(len(self.palavra) - 1, -1, -1):
            self.palavra_inversa += self.palavra[letra]
        if (self.palavra_inversa == self.palavra):
            print("A palavra {} é um palindrome, ela invertida fica {}".format(
                self.palavra, self.palavra_inversa))
        else:
            print("A palavra {} não é um palindrome, ela invertida fica {}".format(
                self.palavra, self.palavra_inversa))
```

- `maior_menor_sequencia.py` Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

```py
class MaiorMenorSequencia:
    def __init__(self, pesos):
        self.pesos = pesos
        self.menor_peso = 0
        self.maior_peso = 0

    def sequencia(self):
        index = 0
        for peso in self.pesos:
            if index == 0:
                self.menor_peso = peso
                self.maior_peso = peso
            else:
                if peso > self.maior_peso:
                    self.maior_peso = peso
                elif peso < self.menor_peso:
                    self.menor_peso = peso
            index += 1

        print("o maior peso lido foi de {}kg".format(self.maior_peso))
        print("o menor peso lido foi de {}kg".format(self.menor_peso))


pesos = [40.0, 5.20, 60.95, 90.95, 75.52]

maiorMenorSequencia = MaiorMenorSequencia(pesos)
maiorMenorSequencia.sequencia()
```

- `analise_completa.py` Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 25 anos.

```py
class AnaliseCompleta:
    def __init__(self, pessoas=[]):
        self.pessoas = pessoas
        self.media = 0
        self.maior_idade = 0
        self.nome_maior_idade = 0
        self.quantidade_mulher = 0

    def analise(self):
        soma_idade = 0
        for p in pessoas:
            soma_idade += p.get("idade")

            if p.get("idade") > self.maior_idade:
                self.maior_idade = p.get("idade")
                self.nome_maior_idade = p.get("nome")

            if p.get("sexo") == "f" and p.get("idade") < 25:
                self.quantidade_mulher += 1

        self.media = soma_idade / len(self.pessoas)

        print("a media de idade é de {:.0f} anos".format(self.media))
        print("o nome da pessoa mais velha é {} e idade é de {:.0f} anos".format(
            self.nome_maior_idade, self.maior_idade))
        print("a quantidade de mulheres com menos de 25 anos é {:.0f}".format(
            self.quantidade_mulher))


pessoas = [
    {
        "nome": "william",
        "idade": 22,
        "sexo": "m"
    },
    {
        "nome": "taty",
        "idade": 21,
        "sexo": "f"
    },
    {
        "nome": "maria",
        "idade": 30,
        "sexo": "f"
    },
    {
        "nome": "claudio",
        "idade": 40,
        "sexo": "m"
    },
    {
        "nome": "ana",
        "idade": 50,
        "sexo": "f"
    },
]

analiseCompleta = AnaliseCompleta(pessoas)
analiseCompleta.analise()
```

- `maioridade.py` Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

```py
from datetime import datetime

class Maioridade:
    def __init__(self, ano_nascimento=[]):
        self.ano_nascimento = ano_nascimento

    def maioridade(self):
        maior = 0
        menor = 0

        for ano in self.ano_nascimento:
            ano_atual = datetime.now()
            idade = ano_atual.year - ano

            if idade >= 21:
                maior += 1
            elif idade < 18:
                menor += 1

        print("{} pessoas atigiram a maioridade".format(maior))
        print("{} pessoas não atigiram a maioridade".format(menor))


anos = [1975, 2000, 2002, 2003, 2004, 2005, 2006, 1999, 1990, 1998]
maioridade = Maioridade(anos)

maioridade.maioridade()
```

### Tuplas

- `times.py` Crie uma tupla preenchida com os da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

  - Os 5 primeiros times.
  - Os últimos 4 colocados.
  - Times em ordem alfabética.
  - Em que posição está o time da Corinthians.

```py
times = ("corinthians", "palmeiras", "santos", "gremio", "cruzeiro",
         "coritiba", "flamengo", "ponte preta", "atletico-go", "atletico-mg")

print(times)
print(times[:5])
print(times[6:])
print(sorted(times))
print(times.index("corinthians") + 1)
```

- `maior_menor.py` Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

```py
from random import randint

n = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))

maior = 0
menor = 0

for i in range(0, len(n)):
    if i == 0:
        maior = n[i]
        menor = n[i]
    else:
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]
print(n)
print("o maior numero sorteado foi {}".format(maior))
print("o menor numero sorteado foi {}".format(menor))
```

- `analise_de_dados.py` Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

  - Quantas vezes apareceu o valor 9.
  - Em que posição foi digitado o primeiro valor 3.
  - Quais foram os números pares.

```py
numeros = (int(input("Digite um numero: ")), int(input("Digite um numero: ")), int(
    input("Digite um numero: ")), int(input("Digite um numero: ")))

position3 = ""

print("os numeros pares são: ", end="")

for i in numeros:
    if i % 2 == 0:
        print("{} ".format(i), end="")

print("\no numero 9 apareceu {}x".format(numeros.count(9)))
if 3 in numeros:
    print("o numero 3 esta na {}° posição".format(numeros.index(3)+1))
else:
    print("o numero 3 não esta em nenhuma posição")
```

- `lista_de_preco` Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

```py
lista = ("lapis", 1.75, "borracha", 2.00, "estojo", 25.00, "caderno", 15.00)

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end="")
    else:
        print(f" R$ {lista[i]:>5.2f}")

print("-"*40)
```

- `vogais.py` Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

```py
palavras = (
    "aprender",
    "programar",
    "estudar",
    "linguagem",
    "python",
    "trabalhar",
    "mercado"
)

for p in palavras:
    print("\nna palavra {} temos as seguintes vogais ".format(p.upper()), end="")

    for letra in p:
        if letra.lower() in "aeiou":
            print("{}".format(letra), end=" ")
```

### Listas

- `numero_por_extenso.py` Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

```py
lista = []

maior = 0
menor = 0

for index in range(0, 5):
    lista.append(
        int(input(f"Digite um numero na posicao {index}: "))
    )
    if index == 0:
        maior = lista[index]
        menor = lista[index]
    else:
        if lista[index] > maior:
            maior = lista[index]
        if lista[index] < menor:
            menor = lista[index]

print("-"*40)
print(lista)
print("-"*40)
print(f"o maior valor encontrado foi {maior} na posicao ", end=" ")

for index, valor in enumerate(lista):
    if lista[index] == maior:
        print(f"{index}", end=" ")

print(f"\no menor valor encontrado foi {menor} na posicao ", end=" ")

for index, valor in enumerate(lista):
    if lista[index] == menor:
        print(f"{index}", end=" ")
```

- `valores_unicos.py` Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

```py
lista = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    if num not in lista:
        lista.append(num)
    else:
        print("valor duplicado")
    if resposta in "Nn":
        break

lista.sort()
print(lista)
```

- `lista_ordenada.py` Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

```py
lista = []

for i in range(0, 5):
    num = int(input("digite um numero "))

    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print("-"*30)
print(f"lista ordenada {lista}")
print("-"*30)
```

- `extraindo_dados.py` Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
  - Quantos números foram digitados.
  - A lista de valores, ordenada de forma decrescente.
  - Se o valor 5 foi digitado e está ou não na lista.

```py
lista = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    lista.append(num)

    if resposta in "Nn":
        break

lista.sort(reverse=True)

print("foram digitados {} numeros ".format(len(lista)))
print(lista)

if 5 not in lista:
    print("o numero 5 não foi encontrado")
else:
    print("o numero 5 foi encontrado")
```

- `multiplas_listas.py` Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

```py
lista = []
pares = []
impares = []

while True:
    num = int(input("digite um numero "))
    resposta = str(input("quer continuar? [S/N] "))

    lista.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if resposta in "Nn":
        break

print(f"Lista {lista}")
print(f"Numeros pares {pares}")
print(f"Numeros impares {impares}")
```

- `validando_expressoes.py` Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

```py
expr = str(input("digite uma espressao "))

pilha = []

for simbolo in expr:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("expressao correta")
else:
    print("expressao incorreta")
```

- `lista_composta.py` Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
  - Quantas pessoas foram cadastradas.
  - Uma listagem com as pessoas mais pesadas.
  - Uma listagem com as pessoas mais leves.

```py
temp = []
lista = []

maior = menor = 0

while True:
    temp.append(str(input("digite um nome ")))
    temp.append(float(input("digite um peso ")))

    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()

    resposta = str(input("quer continuar? [S/N] "))

    if resposta in "Nn":
        break

print("-"*40)
print(f"foram cadastrados {len(lista)} pessoas")
print(f"o maior peso foi de {maior}kg ", end="")
for p in lista:
    if p[1] == maior:
        print(f"{p[0]} ", end="")

print(f"\no menor peso foi de {menor}kg ", end="")
for p in lista:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
```

- `par_impar.py` Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

```py
numeros = [[], []]

for i in range(0, 7):
    num = int(input("digite um numero "))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f"os numeros pares foram {numeros[0]}")
print(f"os numeros impares foram {numeros[1]}")
```

- `matriz.py` Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. mostre:
  - A soma de todos os valores pares digitados.
  - A soma dos valores da terceira coluna.
  - O maior valor da segunda linha.

```py
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"digite um numero para [{l}, {c}]: "))

print("*"*30)

impares = pares = maior_valor_segunda_linha = soma_terceira_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        else:
            impares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[l][c]
    print()

print(f"a soma dos valores pares são {pares} e impares são {impares}")
print(f"a soma dos valores da terceira coluna é de {soma_terceira_coluna}")
print(f"o maior valor da segunda linha é de {maior_valor_segunda_linha}")
```

- `mega_sena.py` Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

```py
from random import randint
from time import sleep

lista = []
jogos = []
total = 1
quantidade = int(input("quantos jogos serão gerados? "))

while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("-="*3, f" SORTEANDO {quantidade} JOGOS ", "=-"*3)

for index, valor in enumerate(jogos):
    print(f"Jogo {index+1}: {jogos[index]}")
    sleep(1)

print("-="*5, f" BOA SORTE ", "=-"*5)
```

- `boletim.py` Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

```py
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
```

### Dicionários de dados

- `dicionario.py` Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

```py
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

print(f"O aluno {aluno['nome']} teve sua média {aluno['media']} e sua situação é {aluno['situacao']}")
```

- `jogo_dados.py` Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

```py
from random import randint
from time import sleep
from operator import itemgetter

ranking = []
dado = {}

dado["jogador1"] = randint(1, 6)
dado["jogador2"] = randint(1, 6)
dado["jogador3"] = randint(1, 6)
dado["jogador4"] = randint(1, 6)

print("Valores sorteados:")

for key, value in dado.items():
    print(f" {key} tirou {value} no dado.")
    sleep(1)

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

print("\nRanking:")

for index, value in enumerate(ranking):
    print(f" {index+1} lugar: {value[0]} com {value[1]}")
    sleep(1)
```

- `cadastro_trabalhador.py` Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

```py
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
```

- `cadastro_jogador_futebol.py` Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

```py
gols = []
dados = {}

dados["nome"] = str(input("Nome: "))
dados["partidas"] = int(input("Partidas: "))

for i in range(0, dados["partidas"]):
    gols.append(int(input(f"Gols na partida {i+1}: ")))

dados["gols"] = gols[:]
dados["total_gols"] = sum(gols)

print(dados)

print('-='*30)
for key, value in dados.items():
    print(f"O campo {key} tem o valor {value}")
print('-='*30)
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas.")

for index, value in enumerate(dados['gols']):
    print(f" Na {index + 1}° partida marcou {value} gol(s)")
```

- `dicionarios_e_listas.py` Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
  - Quantas pessoas foram cadastradas
  - A média de idade
  - Uma lista com as mulheres
  - Uma lista de pessoas com idade acima da média

```py
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
```
