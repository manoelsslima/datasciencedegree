'''
Desafio 2 - Faça o mesmo programa do exercício anterior, porém com 4 números.
'''

primeiro = input('Informe o número 1: ')
segundo = input('Informe o número 2: ')
terceiro = input('Informe o número 3: ')
quarto = input('Informe o número 4: ')

if(primeiro > segundo and primeiro > terceiro and primeiro > quarto):
	maior = primeiro
if(segundo > primeiro and segundo > terceiro and segundo > quarto):
	maior = segundo
if(terceiro > primeiro and terceiro > segundo and terceiro > quarto):
	maior = terceiro
if(quarto > primeiro and quarto > segundo and quarto > terceiro):
	maior = quarto

print('O maior número é:', maior)
