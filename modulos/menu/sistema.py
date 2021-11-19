from lib.interface import Menu
from lib.arquivo import Arquivo
from time import sleep

sistema = Menu()
arquivo = Arquivo()

arquivo_nome = "cadastro.txt"

if not arquivo.existe(arquivo_nome):
    arquivo.criar(arquivo_nome)

try:
    while True:
        resposta = sistema.menu(["Listar Pessoas", "Cadastrar Pessoa", "Sair"])

        if resposta == 1:
            arquivo.ler(arquivo_nome)
        elif resposta == 2:
            sistema.cabecalho("Cadastrar Pessoa")

            nome = sistema.leiaString("\033[1;34mNome: \033[1;34m")
            idade = sistema.leiaInt(mensagem="\033[1;34mIdade: \033[1;34m")

            arquivo.cadastrar(arquivo_nome, nome, idade)
        elif resposta == 3:
            sistema.cabecalho("Saindo do sistema")
            break
        else:
            print("\033[31mErro, escolha uma opção válida!\033[31m")
        sleep(1)
except KeyboardInterrupt:
    sistema.cabecalho("\033[1;93mVolte sempre...\033[1;93m")
