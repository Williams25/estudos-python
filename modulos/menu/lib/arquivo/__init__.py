import os
from lib.interface import Menu


class Arquivo:
    def __init__(self):
        self.path = os.path.dirname(__file__) + "/"
        self.menu = Menu()

    def existe(self, arquivo):
        try:
            a = open(self.path + arquivo, "rt")
        except FileNotFoundError:
            return False
        else:
            return True

    def criar(self, arquivo):
        try:
            a = open(self.path + arquivo, "wt+")
            a.close()
        except:
            print("\033[1;31mHouve um erro na criação do arquivo\033[1;31m")
        else:
            print(f"\033[1;92mArquivo {arquivo} criado com sucesso\033[1;92m")

    def ler(self, arquivo):
        try:
            a = open(self.path + arquivo, "rt")
        except:
            print(
                f"\033[1;31mHouve um erro ao ler o arquivo {arquivo}\033[1;31m")
        else:
            self.menu.cabecalho("Pessoas Cadastradas")
            for linha in a:
                dado = linha.split(";")
                dado[1] = dado[1].replace("\n", "")
                print(f"\033[1;37m  {dado[0]:<30} {dado[1]:>3} anos\033[1;37m")
        finally:
            a.close()

    def cadastrar(self, arquivo, nome="<desconhecido>", idade=0):
        try:
            a = open(self.path + arquivo, "at")
        except:
            print(
                f"\033[1;31mHouve um erro ao ler o arquivo {arquivo}\033[1;31m")
        else:
            try:
                a.write(f"{nome};{idade}\n")
            except:
                print(
                    f"\033[1;31mHouve um ao cadastrar os dados no arquivo {arquivo}\033[1;31m")
            else:
                print(f"\033[1;92mNovo registo de {nome} adicionado\033[1;92m")
            finally:
                a.close()
