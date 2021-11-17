class Ficha:

    def detalhes(self, jogador="<desconhecido>", gols=0):
        if len(jogador) == 0:
            jogador = "<desconhecido>"
        if len(gols) == 0:
            gols = 0
        print(f"O jogador {jogador} fez {gols} gol(s) no campeonato")


jogador = str(input("nome: "))
gols = str(input("gols: "))
Ficha().detalhes(jogador, gols)
