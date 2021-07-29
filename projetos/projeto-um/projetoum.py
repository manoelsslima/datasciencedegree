import csv

'''
Data Science Degree - Let's code
Autor: Manoel de Souza Silva Lima
Data: 05/07/2021
'''

def abrir_arquivo(nome):
    '''Abre o arquivo informado e devolve uma lista com o arquivo organizado'''
    if (nome != None and nome != ''):
        try:
            arquivo = open(nome + '.csv', 'r')
            leitor_csv = csv.reader(arquivo, delimiter=';')
            for linha in leitor_csv:
                lista = list()
                # seleciona o nome
                for i in range(3):
                    if (linha[i].isalpha()):
                        lista.append(linha[i])
                # seleciona o telefone
                for j in range(3):
                    if (linha[j].isnumeric()):
                        lista.append(linha[j])
                # seleciona o e-mail
                for k in range(3):
                    if (linha[k].find('@') != -1):
                        lista.append(linha[k])
                # adiciona à lista
                lista_organizada.append(lista)
            return lista_organizada
        except:
            print('Houve um erro ao abrir o arquivo.')
        finally:
            arquivo.close()
    else:
        raise ValueError('Nome de arquivo inválido!')


def listar(lista):
    '''Lista o conteúdo do arquivo'''
    for i in range(len(lista)):
        print(f'Nome:', lista[i][0])
        print(f'Telefone:', lista[i][1])
        print(f'E-mail:', lista[i][2])
        print('------------------------------------')
        print('')

def buscar(lista_organizada):
    opcao = 1
    while (opcao != '1' and opcao != '2' and opcao != '3'):
        print('''Deseja buscar por:
1) Nome
2) Telefone
3) E-mail''')
        opcao = input('Digite a opção: ')

    if (opcao == '1'):
        nome = input('Informe o nome: ')
        buscar_por_nome(nome, lista_organizada)
    if (opcao == '2'):
        telefone = input('Informe o telefone: ')
        buscar_por_telefone(telefone, lista_organizada)
    if (opcao == '3'):
        email = input('Informe o e-mail: ')
        buscar_por_email(email, lista_organizada)

def buscar_por_nome(nome, lista_organizada):
    '''Busca um fornecedor por nome'''
    localizado = False
    for i in range(len(lista_organizada)):
        if (nome in lista_organizada[i]):
            localizado = True
            print('')
            print('-------------------------------')
            print('Dados do fornecedor')
            print('-------------------------------')
            print('Nome:', lista_organizada[i][0])
            print('Telefone:', lista_organizada[i][1])
            print('E-mail:', lista_organizada[i][2])
            print('-------------------------------')
            print('')
    if (localizado == False):
        print('')
        print('-------------------------------')
        print('Fornecedor não localizado!')
        print('-------------------------------')
        print('')

def buscar_por_telefone(telefone, lista_organizada):
    '''Busca um fornecedor por telefone'''
    localizado = False
    for i in range(len(lista_organizada)):
        if (telefone in lista_organizada[i]):
            localizado = True
            print('')
            print('-------------------------------')
            print('Dados do fornecedor')
            print('-------------------------------')
            print('Nome:', lista_organizada[i][0])
            print('Telefone:', lista_organizada[i][1])
            print('E-mail:', lista_organizada[i][2])
            print('-------------------------------')
            print('')
    if (localizado == False):
        print('')
        print('-------------------------------')
        print('Fornecedor não localizado!')
        print('-------------------------------')
        print('')

def buscar_por_email(email, lista_organizada):
    '''Busca um fornecedor por e-mail'''
    localizado = False
    for i in range(len(lista_organizada)):
        if (email in lista_organizada[i]):
            localizado = True
            print('')
            print('-------------------------------')
            print('Dados do fornecedor')
            print('-------------------------------')
            print('Nome:', lista_organizada[i][0])
            print('Telefone:', lista_organizada[i][1])
            print('E-mail:', lista_organizada[i][2])
            print('-------------------------------')
            print('')
    if (localizado == False):
        print('')
        print('-------------------------------')
        print('Fornecedor não localizado!')
        print('-------------------------------')
        print('')

'''
def gravar_arquivo(novo_nome):
    arquivo = open(novo_nome + '.csv', 'w')
    writer = csv.writer(arquivo)
    for i in range(len(lista_organizada)):
        writer.writerow(lista_organizada[i])
    arquivo.close()
    print('Arquivo gravado com sucesso!')
'''
def adicionar_fornecedor(lista):
    '''Adiciona um fornecedor'''
    print('=== Adicionando fornecedor ===')
    nome = input('Informe o nome do fornecedor: ')
    for i in range(len(lista)):
        if (nome == lista[i][0]):
            print('O fornecedor já está cadastardo!')
        else:
            telefone = input('Informe o telefone: ')
            email = input('Informe o e-mail: ')
            laux = list()
            laux.append(nome)
            laux.append(telefone)
            laux.append(email)
            lista.append(laux)
            arquivo = open(nome_arquivo + '.csv', 'w')
            writer = csv.writer(arquivo, delimiter=";")
            for i in range(len(lista_organizada)):
                writer.writerow(lista_organizada[i])
            arquivo.close()
            print('Arquivo gravado com sucesso!')
            break

def remover_fornecedor(lista):
    '''Remove um fornecedor'''
    print('=== Removendo fornecedor ===')
    nome = input('Informe o nome do fornecedor: ')
    for i in range(len(lista)):
        if (nome == lista[i][0]):
            print('O fornecedor foi localizado!')
            print('Removendo-o...')
            lista.remove(lista[i])
            print('Fornecedor removido com sucesso!')
            arquivo = open(nome_arquivo + '.csv', 'w')
            writer = csv.writer(arquivo, delimiter=";")
            for i in range(len(lista_organizada)):
                writer.writerow(lista_organizada[i])
            arquivo.close()
            print('Arquivo gravado com sucesso!')
            break


def boas_vindas():
    '''Exibe uma mensagem de boas-vindas'''
    print('=====================================')
    print('====== Bem-vindo(a) ao sistema ======')
    print('=====================================')


lista_organizada = list()
nome_arquivo = input('Informe o nome do arquivo .CSV que deseja manipular (sem extensão): ')
lista_organizada = abrir_arquivo(nome_arquivo)
opcao = '0'

while(opcao != '5'):
    boas_vindas()
    try:
        print('1) Listar')
        print('2) Adicionar')
        print('3) Remover')
        print('4) Buscar')
        print('5) Sair')

        opcao = input('Digite a opção: ')
        if (opcao == '1'):
            listar(lista_organizada)
        if (opcao == '2'):
            adicionar_fornecedor(lista_organizada)
        if (opcao == '3'):
            remover_fornecedor(lista_organizada)
        if (opcao == '4'):
            buscar(lista_organizada)
        if (opcao == '5'):
            print('Saindo do sistema...')
            break
    except:
        pass


