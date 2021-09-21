# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:43:02 2021

@author: Maria Camila
"""

# Encontrar el menor valor de un conjunto de n números dados.
conjunto_numeros = int(input('Ingrese la cantidad de numeros: '))
total = []
for n in range(1, conjunto_numeros + 1):
    numero = int(input(f'Ingrese el valor número {n}: '))
    conjunto_numeros += 1
    total.append(numero)

menor = min(total)

print(f'El número menor es: {menor}')
