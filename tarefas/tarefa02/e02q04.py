'''
Faça um programa que leia a validade das informações:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.
'''

idade = int(input('Informe sua idade: '))
salario = float(input('Informe seu salário: '))
sexo = input('Informe seu sexo: ')

if(idade < 0 or idade > 150):
	print('Erro: idade inválida')

if(salario <= 0):
	print('Erro: Salário inválido')

if(sexo == 'F' or sexo == 'f'):
	print('Sexo feminino')
elif(sexo == 'M' or sexo == 'm'):
	print('Sexo masculino')
elif(sexo == 'Outro' or sexo == 'OUTRO' or sexo == 'outro'):
	print('Outro sexo')
else:
	print('Erro: Opção de sexo inválida')
