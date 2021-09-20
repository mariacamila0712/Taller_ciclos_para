# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:34:57 2021

@author: Maria Camila
"""

# Un Zoólogo pretende determinar el porcentaje de animales que hay en las
# siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
# de 3 o mas años. El zoológico todavía no está seguro del animal que va
# estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
# si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
# 40.

edades_de_animales = []
numero_de_muestras = 0
porcentaje_de_0_a_1 = 0
porcentaje_de_1_menor_a_3 = 0
porcentaje_mayor_a_3 = 0
tipo_animal = input('Digite el tipo de animal(elefantes, chimpances o jirafas):')
if tipo_animal == "elefantes":
    numero_de_muestras = 20
elif tipo_animal == "jirafas":
    numero_de_muestras = 15
elif tipo_animal == "chimpances":
    numero_de_muestras = 40

for a in range(numero_de_muestras):
    edades_de_animales.append(int(input('Edad del animal: ')))

for edad in edades_de_animales:
    if edad == 0 or edad == 1:
        porcentaje_de_0_a_1 = porcentaje_de_0_a_1 + 1
    elif edad > 1 and edad < 3:
        porcentaje_de_1_menor_a_3 = porcentaje_de_1_menor_a_3 + 1
    elif edad >= 3:
        porcentaje_mayor_a_3 = porcentaje_mayor_a_3 + 1
porcentaje_de_0_a_1 = porcentaje_de_0_a_1 * 100 / numero_de_muestras
porcentaje_de_1_menor_a_3 = porcentaje_de_1_menor_a_3 * 100 / numero_de_muestras
porcentaje_mayor_a_3 = porcentaje_mayor_a_3 * 100 / numero_de_muestras

print(f'El porcentaje de edades de 0 a 1 es: {porcentaje_de_0_a_1}')
print(f'El porcentaje de edades de 1 menoar a 3 es: {porcentaje_de_1_menor_a_3}')
print(f'El porcentaje de edades mayor a 3 es: {porcentaje_mayor_a_3}')