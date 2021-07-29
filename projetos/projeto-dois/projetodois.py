from agenda import Agenda

'''
Data Science Degree - Let's code
Classe principal da aplicação
Autor: Manoel de Souza Silva Lima
Data: 21/07/2021
'''
class Aplicacao():
    '''Aplicação principal'''
    def __init__(self):
        self.__agenda = Agenda('agenda.json')

    def __boas_vindas(self):
        '''Exibe uma mensagem de boas-vindas'''
        print('=====================================')
        print('====== Bem-vindo(a) ao sistema ======')
        print('=====================================')

    def __menu(self):
        opcao = None
        '''Exibe um menu de opções'''
        while(opcao != '6'):
            try:
                self.__boas_vindas()
                print('1) Listar')
                print('2) Buscar/Detalhar')
                print('3) Adicionar')
                print('4) Remover')
                print('5) Editar')
                print('6) Sair')

                opcao = input('Digite a opção: ')
                if (opcao == '1'):
                    self.__agenda.listar()
                elif (opcao == '2'):
                    self.__agenda.buscar()
                elif (opcao == '3'):
                    self.__agenda.adicionar()
                elif (opcao == '4'):
                    self.__agenda.remover()
                elif (opcao == '5'):
                    self.__agenda.editar()
                elif (opcao == '6'):
                    print('Saindo do sistema...')
                    break
                else:
                    print('')
                    print('-' * 39)
                    print('Informe uma opção válida!')
                    print('-' * 39)
                    print('')
            except Exception as erro:
                print('')
                print('-' * 78)
                print('Aviso:', str(erro))
                print('-' * 78)
                print('')

    def main(self):
        self.__menu()

if __name__ == '__main__':
    aplicacao = Aplicacao()
    aplicacao.main()