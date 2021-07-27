'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:

a. Sente dor no corpo?

b. Você tem febre?

c. Você tem tosse?

d. Está com congestão nasal?

e. Tem manchas pelo corpo?

Para o diagnóstico ele tem a seguinte tabela:
A 	B 	C 	D 	E 	Resultado
Sim 	Sim 	Não 	Não 	Sim 	Dengue
Sim 	Sim 	Sim 	Sim 	Não 	Gripe
Não 	Sim 	Sim 	Sim 	Não 	Gripe
Sim 	Não 	Não 	Não 	Não 	Sem doenças
Não 	Não 	Não 	Não 	Não 	Sem doenças
'''

a = input('Sente dor no corpo? (sim/não): ')
b = input('Você tem febre? (sim/não): ')
c = input('Você tem tosse? (sim/não): ')
d = input('Está com congestão nasal? (sim/não): ')
e = input('Tem manchas pelo corpo? (sim/não): ')

if(a == 'sim' and b == 'sim' and c != 'sim' and d != 'sim' and e == 'sim'):
	resultado = 'Dengue'
if(a == 'sim' and b == 'sim' and c == 'sim' and d == 'sim' and e != 'sim'):
	resultado = 'Gripe'
if(a != 'sim' and b == 'sim' and c == 'sim' and d == 'sim' and e != 'sim'):
	resultado = 'Gripe'
if(a == 'sim' and b != 'sim' and c != 'sim' and d != 'sim' and e != 'sim'):
	resultado = 'Sem doenças'
if(a != 'sim' and b != 'sim' and c != 'sim' and d != 'sim' and e != 'sim'):
	resultado = 'Sem doenças'

print('Resultado do diagnóstico é:', resultado)
