# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:39:21 2021

@author: Maria Camila
"""

"""Un teatro otorga descuentos según la edad del cliente, determinar la
cantidad del dinero que el teatro deja de percibir por cada ua de las
categorias. Tomar en cuenta que los niños menores de 5 años no pueden
entrar al teatro y que existe un precio único en los asientos. Los descuentos
se hacen tomando en cuenta el siguiente cuadro:
Edad % Descuento
5 – 14 35%
15-19 25%
20 – 45 10%
46 – 65 25%
66 en Adelante 35%"""
entrada = float(input('Digite el precio de la entrada única al teatro'))
clientes = int(input('Digite la cantidad de clientes: '))
edad = 0
suma_descuento = 0
for a in range(clientes):
	edad_actual = int(input('Digite la edad del cliente (debe ser mayor de 5años) número {a}: ')
    if edad_actual >= 5 and edad_actual <= 14:
		suma_descuento = suma_descuento + entrada * 0.35
	elif edad_actual >= 15 and edad_actual <= 19:
		suma_descuento = suma_descuento + entrada * 0.25
	elif edad_actual >= 20 and edad_actual <= 45:
		suma_descuento = suma_descuento + entrada * 0.10
	elif edad_actual >= 46 and edad_actual <= 65:
		suma_descuento = suma_descuento + entrada * 0.25
	elif edad_actual >= 66:
		suma_descuento = suma_descuento + suma_descuento * 0.35

print(f'El dinero en total que se descontó fue de ${:,sumaDescuento}')
