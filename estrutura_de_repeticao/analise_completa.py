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
