class Notas:
    def __init__(self):
        self.media = {}

    def soma_media(self, *notas, situacao=False):
        media_total = media = maior = menor = 0

        for i, nota in enumerate(notas):
            if i == 0:
                maior = nota
                menor = nota
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
            media += nota

        media_total = media / len(notas)

        if situacao:
            self.media["situacao"] = self.situacao(media_total)

        self.media["total"] = len(notas)
        self.media["maior"] = maior
        self.media["menor"] = menor
        self.media["media"] = media_total
        return self.media

    def situacao(self, media=0):
        if media >= 6 and media <= 7:
            return "Bom"
        elif media < 6 and media >= 5:
            return "Regular"
        elif media > 7 and media <= 10:
            return "Otimo"
        elif media < 5:
            return "Ruim"


print(Notas().soma_media(10, 6, 6, situacao=True))
