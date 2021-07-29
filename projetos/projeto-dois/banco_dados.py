import json

'''
Data Science Degree - Let's code
Classe de banco de dados
Autor: Manoel de Souza Silva Lima
Data: 25/07/2021
'''
class BancoDados():
    '''Armazena as informações em um banco de dados
        Nesse caso, utiliza um arquivo json'''
    def __init__(self, nome_bd):
        self.__nome_banco_dados = nome_bd
        self.__dados = None

    def abrir_arquivo(self):
        try:
            with open(self.__nome_banco_dados, 'r+') as arquivo:
                conteudo = arquivo.read()
                if(conteudo):
                    self.__dados = json.loads(conteudo)
                else:
                    self.__dados = dict()
        except FileNotFoundError as fnfe:
            with open(self.__nome_banco_dados, 'w') as arquivo:
                arquivo.write('{}')
                arquivo.close()
                self.__dados = dict()
        return self.__dados

    def gravar_arquivo(self, conteudo):
        with open(self.__nome_banco_dados, 'w') as arquivo:
            json.dump(conteudo, arquivo)