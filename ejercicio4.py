# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:24:40 2021

@author: Maria Camila
"""

# Calcular el promedio de edades de hombres, mujeres y de todo un grupo
# de alumnos.

cantidad_alumnos = int(input('Digite la cantidad de alumnos: '))

total_mujeres = 0
contador_mujeres = 0
total_hombres = 0
contador_hombres = 0

for n in range(1, cantidad_alumnos + 1):
    genero = str(input('Digite la letra (h) para hombre y (m) para mujer: '))

    if(genero == 'h'):
        contador_hombres = contador_hombres + 1
        edad = int(input('Digite la edad: '))
        total_hombres += edad

    elif(genero == 'm'):
        contador_mujeres = contador_mujeres + 1
        edad = int(input('Digite la edad: '))
        total_mujeres += edad

promedio_hombres = total_hombres / contador_hombres
promedio_mujeres = total_mujeres / contador_mujeres
promedio_curso = (total_mujeres + total_hombres) / (contador_hombres + contador_mujeres )

print(f' El promedio de hombres es: {promedio_hombres}')
print(f' El promedio de mujeres es: {promedio_mujeres}')
print(f' El promedio total del grupo es: {promedio_curso}')
