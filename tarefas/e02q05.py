'''
Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.

Obs.: O aluno irá passar de ano se sua média for maior que 6.
'''

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
media = (nota1 + nota2 + nota3)/3
if(media > 6):
	print('O aluno passou de ano')
else:
	print('O aluno não passou de ano')
