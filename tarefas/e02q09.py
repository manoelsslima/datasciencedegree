'''
Desafio 1 - Faça um programa que leia 3 números e informe o maior deles.
'''

primeiro = input('Informe o número 1: ')
segundo = input('Informe o número 2: ')
terceiro = input('Informe o número 3: ')

if(primeiro > segundo and primeiro > terceiro):
	maior = primeiro
if(segundo > primeiro and segundo > terceiro):
	maior = segundo
if(terceiro > primeiro and terceiro > segundo):
	maior = terceiro

print('O maior número é:', maior)
