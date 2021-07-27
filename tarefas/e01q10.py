'''
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:

a) o produto do dobro do primeiro com metade do segundo.

b) a soma do triplo do primeiro com o terceiro.

c) o terceiro elevado ao cubo.
'''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

a = (2 * num1) * (num2 / 2)
b = (3 * num1) + num3
c = num3 ** 3

print(a)
print(b)
print(c)
