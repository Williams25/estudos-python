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
