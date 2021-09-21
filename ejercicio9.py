# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:50:26 2021

@author: Maria Camila
"""

"""Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la 
siguiente tabla:
Valor vendido Comisión
Menor o igual que 20 
Millones
10%
Mayor de 20 Millones y 
menor de 40 Millones
15%
Mayor o igual de 40 20%
Millones y menor de 80 
Millones
Mayor o igual de 80 
millones y menor de 
160 Millones
25%
De 160 Millones en 
adelante
30%
Realice un método que diga cuanto vendió y la comisión de los 100 
vendedores que tiene la empresa"""
def comision():
  for n in range( 1, 101):
    venta = float(input(f'Ventas realizadas empleado {n}: '))

    if venta <= 200000000:
      comision_venta = venta * 0.10
      print(f'La comision por ventas empleado {n}, {comision_venta}')

    if venta >= 200000000 and venta <= 400000000:
      comision = venta * 0.15
      print( f'La comision por ventas empleado {n}, {comision_venta}')

    if venta >= 400000000 and venta <= 800000000:
      comision = venta * 0.20
      print(f'La comision por ventas empleado {n}, {comision_venta}')

    if venta >= 800000000 and venta <= 1600000000:
      comision = venta * 0.25
      print( f'La comision por ventas empleado {n}, {comision_venta}')

    if venta > 1600000000:
      comision = venta * 0.30
      print( f'La comision por ventas empleado {n}, {comision_venta}')

comision()