import math

x_ponto1 = float(input('Entre com a posição x do primeiro ponto: '))
y_ponto1 = float(input('Entre com a posição y do primeiro ponto: '))

x_ponto2 = float(input('Entre com a posição x do segundo ponto: '))
y_ponto2 = float(input('Entre com a posição y do segundo ponto: '))


DistEntrePontos = math.sqrt((x_ponto2-x_ponto1)**2 + (y_ponto2-y_ponto1)**2)

if DistEntrePontos >= 10:

    print('longe')

else:

    print('perto')
