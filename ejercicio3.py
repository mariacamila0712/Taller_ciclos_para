# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:10:40 2021

@author: Maria Camila
"""
# Una empresa se requiere calcular el salario semanal de cada uno de los n 
# obreros que laboran en ella. El salario se obtiene de la siguiente forma:
# a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
# b. Si trabaja mas de 40 horas se le paga $20 por cada una de 
# las primeras 40 horas y $25 por cada hora extra.
cantidad_obreros = int(input('Digite la cantidad de obreros: '))
salarios = []

for a in range( 1, cantidad_obreros + 1):
  horas_trabajadas = int(input(f'Digite la cantidad de horas del obrero {a}: '))

  if(horas_trabajadas <= 40 ):
    pago = horas_trabajadas * 20

    salarios.append(pago)
  elif( horas_trabajadas > 40 ):
    pago = 40 * 20
    horas_extras = horas_trabajadas - 40
    pago_extra =int(horas_extras * 25 )

    salario_semanal = pago + pago_extra
    salarios.append(salario_semanal)

print(f'Los salarios de los obreros son: ${salarios}')
