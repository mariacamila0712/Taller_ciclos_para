# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:19:39 2021

@author: Maria Camila
"""

# El departamento de Seguridad de Transito de Barranquilla, desea saber de
# los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
# color. Conociendo el último digito de la placa de cada automóvil se puede
# determinar el color de la calcomanía utilizando la siguiente relación:
# DIGITO COLOR
# 1 o 2 Amarilla
# 3 o 4 Rosa
# 5 o 6 Roja
# 7 u 8 Verde
# 9 o 0 Azul
cantidad_autos = int(input('Digite la cantidad de autos a ingresar: '))
autos = []
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
for carro_numero in range(0, cantidad_autos):
   autos.append(int(input(f'Escriba el ultimo digito de la placa del auto numero {carro_numero}: '))) 

for color in autos:
    if color == 1 or color == 2:
        amarillo = amarillo + 1
    elif(color == 3 or color == 4):
        rosa = rosa + 1
    elif(color == 5 or color == 6):
        roja = roja + 1
    elif(color == 7 or color == 8):
        verde = verde + 1
    else:
        azul = azul + 1
print(f'Cantidad de autos con calcomanias amarillas es: {amarillo}')
print(f'Cantidad de autos con calcomanias rosas es: {rosa}')
print(f'Cantidad de autos con calcomanias rojas es: {roja}')
print(f'Cantidad de autos con calcomanias verde es: {verde}')
print(f'Cantidad de autos con calcomanias azul es: {azul}')
