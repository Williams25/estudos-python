### Funções

- `calcula_area.py` Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

```py
class CalculaArea:
    def __init__(self, largura=0, comprimento=0):
        self.largura = largura
        self.comprimento = comprimento

    def area(self):
        return self.largura * self.comprimento


largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

calculaArea = CalculaArea(largura, comprimento)
print(calculaArea.area())
```

- `print.py` Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
  - Ex:
    ```
      escreva('Olá, Mundo!')
      Saída:
      ~~~~~~~~~~~
      Olá, Mundo!
      ~~~~~~~~~~~
    ```

```py
class Print:
    def __init__(self, msg):
        self.msg = msg
        self.length = len(self.msg)+4

    def escreva(self):
        print(f"~"*self.length)
        print(f"  {self.msg}")
        print(f"~"*self.length)


Print("Olá, Mundo!").escreva()
```

- `contador.py` Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
  - de 1 até 10, de 1 em 1
  - de 10 até 0, de 2 em 2
  - uma contagem personalizada

```py
from time import sleep


class Contador:
    def __init__(self, inicio=10, fim=0, passo=1):
        self.inicio = inicio
        self.fim = fim
        self.passo = passo

    def contador(self):
        print("-="*30)
        print(f"Contagem de 1 até 10, de 1 em 1")
        for i in range(1, 11):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)

        print("-="*30)
        print(f"Contagem de 10 até 0, de 2 em 2")
        for i in range(10, 0, -2):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)

        print("-="*30)
        print(
            f"Contagem personalizada inicio {self.inicio} fim {self.fim} e pula de {self.passo} em {self.passo}")
        for i in range(self.inicio, self.fim, self.passo):
            print(f"{i}", end=" ", flush=True)
            sleep(1)
        print("Fim")
        print("-="*30)


inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

Contador(inicio, fim, passo).contador()
```

- `maior.py` Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

```py
class Maior:
    def __init__(self, * num):
        self.num = num
        self.maior_num = 0

    def maior(self):
        for i in self.num:
            print(i, end=" ")
            if i > self.maior_num:
                self.maior_num = i

        print(f"foram informados {len(self.num)} valores ao todo")
        print(f"o maior numero é {self.maior_num}")


Maior(10, 20, 2, 13).maior()
```

- `sortear_somar.py` Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

```py
from random import randint


class SortearSomar:
    def __init__(self):
        self.lista = []
        self.total_par = 0

    def sortear(self):
        print(f"os numeros sorteados foram:")
        for i in range(0, 5):
            self.lista.append(randint(1, 50))
        print(self.lista)

    def somaPar(self, lista=[]):
        print(f"os numeros pares sorteados foram:")
        for i in lista:
            if i % 2 == 0:
                print(f"{i}", end=" ")
                self.total_par += i

        print(f"\na soma dos numeros pares sorteados foram {self.total_par}")


sortear_somar = SortearSomar()
sortear_somar.sortear()
sortear_somar.somaPar(sortear_somar.lista)
```

- `votacao.py` Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

```py
from datetime import datetime


class Eleicao:
    def __init__(self):
        self.ano_atual = datetime.now().year

    def voto(self, ano=1910):
        idade = self.ano_atual - ano

        if idade >= 16 and idade < 18 or idade >= 65:
            return "OPCIONAL"
        elif idade < 16:
            return "NEGADO"
        elif idade > 18 and idade <= 64:
            return "OBRIGATÓRIO"


print(Eleicao().voto(1999))
```

- `fatorial.py` Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

```py
class Fatorial:
    def fatorial(self, calculo=1, show=False):
        """
        -> Calcule o fatorial de um numero.
        :param calculo: o sumero a ser calculado
        :param show: (opcional) mostrar ou não a conta
        :return: valor fatorial
        """
        f = 1
        for i in range(calculo, 0, -1):
            if show:
                print(i, end='')
                if i > 1:
                    print(" x ", end='')
                else:
                    print(" = ", end='')
            f *= i
        return f


n = Fatorial()
print(n.fatorial(5, True))
```

- `ficha_jogador.py` Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

````py
class Ficha:

    def detalhes(self, jogador="<desconhecido>", gols=0):
        if len(jogador) == 0:
            jogador = "<desconhecido>"
        if len(gols) == 0:
            gols = 0
        print(f"O jogador {jogador} fez {gols} gol(s) no campeonato")


jogador = str(input("nome: "))
gols = str(input("gols: "))
Ficha().detalhes(jogador, gols)```
````
