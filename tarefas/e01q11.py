'''
Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).

Obs: IMC = Peso/Altura**2
'''

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
imc = peso / (altura ** 2)
print(imc)
