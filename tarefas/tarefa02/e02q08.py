'''
Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça um programa que peça para o usuário digitar o valor do produto de acordo com o preço antigo e escreva uma das mensagens da Tabela 2, de acordo com o preço reajustado:

Tabela 1
Preço Antigo 	% de aumento
Até 50 reais 	5%
Entre 50 e 100 reais 	10%
De 100 a 150 reais 	13%
Acima de 150 reais 	15%

Tabela 2
Preço Novo 	Mensagem
Até 80 reais 	Barato
Entre 80 e 115 reais 	Razoável
Entre 115 e 150 reais 	Normal
Entre 150 e 170 reais 	Caro
Acima de 170 reais 	Muito Caro
'''

novo_preco = 0.0
preco_antigo = float(input('Informe o valor do produto: '))
if(preco_antigo > 0.0 and preco_antigo <= 50.0):
	novo_preco = preco_antigo + preco_antigo * 0.05 # 5%
elif(preco_antigo > 50 and preco_antigo <= 100.0):
	novo_preco = preco_antigo + preco_antigo * 0.1 # 10%
elif(preco_antigo > 100 and preco_antigo <= 150.0):
	novo_preco = preco_antigo + preco_antigo * 0.13 # 13%
elif(preco_antigo > 150):
	novo_preco = preco_antigo + preco_antigo * 0.15 # 15%
else:
	print('Informe um preço acima de 0.0')

if(novo_preco <= 80):
	print('Barato')
elif(novo_preco > 80 and novo_preco <= 115):
	print('Razoável')
elif(novo_preco > 115 and novo_preco <= 150):
	print('Normal')
elif(novo_preco > 150 and novo_preco <= 170):
	print('Caro')
else:
	print('Muito Caro')
