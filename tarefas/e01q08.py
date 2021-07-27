'''
Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).

°C = (5 * (F-32) / 9)

Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a transforme em graus Fahrenheit.
'''

temp_f = float(input('Informe a temperatura em °F: '))
temp_c = (5 * (temp_f-32) / 9)
print('A temperatura em Celsius é:', temp_c)
