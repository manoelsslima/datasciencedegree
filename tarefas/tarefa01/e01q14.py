'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.
'''

velocidade_inicial_vo = float(input('Informe a velocidade inicial (Vo) (em m/s): '))
posicao_inicial_y0 = float(input('Informe a posição inicial (em metros): '))
instante_tempo_t = float(input('Informe um instante de tempo (em segundos): '))
gravidade_g = -10
posicao_final_yt = posicao_inicial_y0 + (velocidade_inicial_vo * instante_tempo_t) + (gravidade_g*(instante_tempo_t**2)/2)
print('A posição do projétil nesse instante de tempo é:', posicao_final_yt)
