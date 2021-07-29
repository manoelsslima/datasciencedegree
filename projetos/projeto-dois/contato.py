'''
Data Science Degree - Let's code
Classe de contato
Autor: Manoel de Souza Silva Lima
Data: 25/07/2021
'''
class Contato():
    '''Classe que representa um contato'''
    def __init__(self, cpf, nome, sobrenome, telefones, emails, grupo):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefones = telefones
        self.emails = emails
        self.grupo = grupo

    def __str__(self):
        return str(self.cpf) + ' - ' + self.nome