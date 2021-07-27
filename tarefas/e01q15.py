'''
Desafio 2 - Faça um programa que informe a data e a hora para o usuário. Para isso use a função datetime.now() do módulo datetime.
'''

from datetime import datetime
data_hora_atual = datetime.now()
data = data_hora_atual.strftime('%d/%m/%Y')
hora = data_hora_atual.strftime('%H:%M:%S')
print(f"A data atual é: {data} e a hora atual é: {hora}")
