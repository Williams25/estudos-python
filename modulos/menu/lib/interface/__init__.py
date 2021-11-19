class Menu:
    def leiaInt(self, mensagem):
        while True:
            try:
                num = int(input(mensagem))
            except (ValueError, TypeError):
                print(f"\n\033[31mValor incorreto\033[m")
                continue
            except KeyboardInterrupt:
                print(f"\n\033[31mValor não informado\033[m")
                break
            else:
                return num

    def leiaString(self, mensagem):
        while True:
            try:
                value = str(input(mensagem))
            except (ValueError, TypeError):
                print(f"\n\033[31mValor incorreto\033[m")
                continue
            except KeyboardInterrupt:
                print(f"\n\033[31mValor não informado\033[m")
                break
            else:
                return value

    def linha(self, tamanho=48):
        return '\033[1;36m-\033[1;36m'*tamanho

    def cabecalho(self, texto):
        print(self.linha())
        print(f"\033[1;35m{texto.center(48)}\033[1;35m ")
        print(self.linha())

    def menu(self, lista=[]):
        self.cabecalho("Menu principal")
        for index, valor in enumerate(lista):
            print(f"    \033[33m{index+1}\033[33m", end=" - ")
            print(f"\033[34m{valor}\033[34m", end="\n")
        print(self.linha())

        opc = self.leiaInt("\033[32mSua opção: \033[32m")
        return opc
