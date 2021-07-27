'''
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

a. Mora perto da vítima?

b. Já trabalhou com a vítima?

c. Telefonou para a vítima?

d. Esteve no local do crime?

e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados.
'''

print('=== Questionário ===')
pontos = 0
mora_perto = input('Mora perto da vítima? (sim/não): ')
trabalhou_com = input('Já trabalhou com a vítima? (sim/não): ')
telefonou_para = input('Telefonou para a vítima? (sim/não): ')
esteve_local_crime = input('Esteve no local do crime? (sim/não): ')
devia_para = input('Devia para a vítima? (sim/não): ')

if(mora_perto == 'sim'):
	pontos += 1
if(trabalhou_com == 'sim'):
	pontos += 1
if(telefonou_para == 'sim'):
	pontos += 1
if(esteve_local_crime == 'sim'):
	pontos += 1
if(devia_para == 'sim'):
	pontos += 1

if(pontos == 5):
	print('A pessoa é o assassino!')
elif(pontos <= 5 and pontos >= 3):
	print('A pessoa é cúmplice')
elif(pontos == 2):
	print('A pessoa é um suspeito')
elif(pontos <= 2 and pontos >= 0):
	print('A pessoa está liberada')
else:
	print('Erro')
