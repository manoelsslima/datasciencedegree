'''
Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e). Sabendo a resposta certa, o programa deve receber a opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.
'''

print('A soma de 2 e 5 é:')
print('a) 5')
print('b) 6')
print('c) 7')
print('d) 8')
print('e) 9')
resposta = input('Digite uma opção: ')
if(resposta == 'c'):
	print('Você escolheu a opção', resposta, 'e a resposta está certa')
else:
	print('Você escolheu a opção', resposta, 'e a resposta está errada')
