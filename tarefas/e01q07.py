'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.
'''

ganho_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Informe quantas horas você trabalhou no mês: '))
salario_mes = ganho_hora * horas_trabalhadas
print('Seu salário no mês é:', salario_mes)
