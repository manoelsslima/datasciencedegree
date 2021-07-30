from contato import Contato
from banco_dados import BancoDados

'''
Data Science Degree - Let's code
Classe da agenda
Autor: Manoel de Souza Silva Lima
Data: 25/07/2021
'''
class Agenda():
    '''Agenda'''
    limite = 75 # número máximo de contatos na agenda

    def __init__(self, arquivo_agenda):
        self.__bd = BancoDados(arquivo_agenda)
        self.__dados = self.__bd.abrir_arquivo()

    def __popular_contato(self, cpf=None, edicao=None):
        '''Solicita informações do usuário para preencher um objeto do tipo Contato
        Se o cpf for informado, significa que está editando o Contato e, portanto,
        o cpf não será solicitado'''
        telefones = list()
        emails = list()
        if (cpf == None):
            cpf = input('Informe o CPF: ')
        if (edicao == None):
            if (cpf in self.__dados):
                raise Exception("CPF já cadastrado!")
        nome = input('Informe um nome: ')
        if (nome == None or nome == ''):
            raise Exception('O campo \'nome\' é obrigatório!')
        sobrenome = input('Informe um sobrenome: ')
        while True:
            telefone = input('Informe um telefone (ou 0[zero] para parar): ')
            if (telefone == '0'):
                break
            else:
                if (telefone.isdigit()):
                    telefones.append(telefone)
                else:
                    print('Erro: O campo \'telefone\' deve conter apenas números!')
        while True:
            email = input('Informe um e-mail (ou 0[zero] para parar): ')
            if (email == '0'):
                break
            else:
                if (email.find('@') != -1 and email.find('.') != -1):
                    emails.append(email)
                else:
                    print('Erro: Informe um \'e-mail\' válido!')
        grupo = input('Informe o grupo do contato: ')
        contato = Contato(cpf, nome, sobrenome, telefones, emails, grupo)
        return contato

    def __converter_contato_json(self, contato):
        '''Converte um objeto do tipo Contato em uma string json'''
        string = "{'"+ contato.cpf +"':{'nome':'"+contato.nome+"','sobrenome':'"+ contato.sobrenome +"','telefones':["
        for telefone in contato.telefones:
            string += "'" + telefone + "',"
        string += "], 'emails':["
        for email in contato.emails:
            string += "'" + email + "',"
        string += "], "
        string += "'grupo':'" + contato.grupo + "'}}"
        return string

    def adicionar(self):
        '''Adiciona um contato à agenda'''
        tamanho = len(self.__dados)
        if (tamanho < Agenda.limite):
            contato = self.__popular_contato()
            contato_json = self.__converter_contato_json(contato)
            self.__dados.update(eval(contato_json))
            self.__bd.gravar_arquivo(self.__dados)
        else:
            raise Exception(f'Número máximo de {Agenda.limite} contatos excedidos!')

    def buscar(self):
        '''Busca um contato'''
        opcao = '0'
        while(opcao != '1' or opcao != '2'):
            print('=' * 78)
            print('Opções de busca')
            print('=' * 78)
            print('1) Por CPF')
            print('2) Por grupo')
            print('0) Sair da busca')
            opcao = input('Informe o tipo de busca: ')
            if (opcao == '1'):
                self.__buscar_por_cpf()
            elif (opcao == '2'):
                self.__buscar_por_grupo()
            elif (opcao == '0'):
                break
            else:
                print('Informe uma opção válida!')

    def __buscar_por_grupo(self):
        localizado = False
        contatos = dict()
        contato_localizado = dict()
        grupo = input('Informe o grupo que deseja buscar: ')
        for contato in self.__dados.items():
            valores = contato[1]
            if (grupo == valores['grupo']):
                localizado = True
                contato_localizado[contato[0]] = contato[1]
                contatos.update(contato_localizado)
        if (localizado == True):
            print('')
            print('=' * 78)
            print('Informações dos contatos do grupo:',grupo)
            print('=' * 78)
            for chave, valor in contatos.items():
                print(f'CPF :', chave)
                for chave, valor in valor.items():
                    if (isinstance(valor, list)):
                        print(chave.capitalize(), ": ", end="")
                        for i in range(len(valor)):
                            print(valor[i], end=" | ")
                        print('')
                    else:
                        print(chave.capitalize(),':', valor)
                print('-' * 39)
            print('')
        else:
            print('')
            print('-' * 78)
            print('Nenhum contato com do grupo', grupo, 'localizado!')
            print('-' * 78)
            print('')

    def __buscar_por_cpf(self, cpf=None):
        '''Busca um contato por CPF'''
        localizado = False
        if (cpf == None):
            cpf = input('Informe o CPF do contato que deseja buscar: ')
        for chave, valor in self.__dados.items():
            if (cpf == chave):
                localizado = True
                #print("CPF:", cpf, "localizado")
                print('')
                print('-' * 78)
                print('Informações do contato')
                print('-' * 78)
                for chave, valor in valor.items():
                    if (isinstance(valor, list)):
                        print(chave.capitalize(), ": ", end="")
                        for i in range(len(valor)):
                            print(valor[i], end=" | ")
                        print('')
                    else:
                        print(chave.capitalize(),':', valor)
                print('-' * 39)
                print('')
        if (localizado == False):
            print('')
            print('----------------------------------------')
            print('Contato não localizado! Tente outro CPF!')
            print('----------------------------------------')
            print('')

    def remover(self):
        '''Remove um contato por CPF'''
        localizado = False
        cpf = input('Informe o CPF do contato que deseja remover: ')
        for chave, valor in self.__dados.items():
            if (cpf == chave):
                localizado = True
                print('')
                print('----------------------------------------')
                print(f'Contato {cpf} removido')
                print('----------------------------------------')
                print('')
                del self.__dados[cpf]
                self.__bd.gravar_arquivo(self.__dados)
                break
        if (localizado == False):
            print('')
            print('----------------------------------------')
            print('Contato não localizado! Tente outro CPF!')
            print('----------------------------------------')
            print('')

    def editar(self):
        '''Edita um contato por CPF'''
        localizado = False
        cpf = input('Informe o CPF do contato que deseja alterar: ')
        for chave, valor in self.__dados.items():
            if (cpf == chave):
                self.__buscar_por_cpf(cpf)
                localizado = True
                print("Editando o contato CPF:", cpf)
                contato = self.__popular_contato(chave, edicao=True)
                string_contato = eval(self.__converter_contato_json(contato))
                dicionario = dict(string_contato)
                valores = str(list(dicionario.values()))
                self.__dados[cpf] = eval(valores.strip('[]'))
                self.__bd.gravar_arquivo(self.__dados)
                print('-' * 39)
                print('Contato atualizado com sucesso!')
                print('-' * 39)
                print('')
                break
        if (localizado == False):
            print('')
            print('----------------------------------------')
            print('Contato não localizado! Tente outro CPF!')
            print('----------------------------------------')
            print('')

    def listar(self):
        '''Lista o conteúdo do arquivo'''
        print('=' * 78)
        print('Contatos cadastrados')
        print('=' * 78)
        if (self.__dados):
            for chave, valor in self.__dados.items():
                print(f'CPF :', chave)
                for chave, valor in valor.items():
                    if (isinstance(valor, list)):
                        print(chave.capitalize(), ": ", end="")
                        for i in range(len(valor)):
                            print(valor[i], end=" | ")
                        print('')
                    else:
                        print(chave.capitalize(),':', valor)
                print('-' * 39)
            print('')
        else:
            print('')
            print('-' * 39)
            print('Arquivo vazio.')
            print('-' * 39)
            print('')