# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:22:47 2021

@author: Maria Camila
"""

# En un supermercado una ama de casa pone en su carrito los artículos que
# va tomando de los estantes. La señora quiere asegurarse de que el cajero
# le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
# artóculo anota su precio junto con la cantidad de artículos iguales que ha
# tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
# que irá gastando en los demás artículos, hasta que decide que ya tomó
# todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
# compra.
def compra_total():
  articulos = []
  total_compra = 0


  for n in range( 1, 6):
    precio = float(input(f'Digite el precio del articulo {n} $: '))
    articulos.append(precio)

  for articulo in articulos:
    cantidad = int(input(f'Digite la cantidad del articulo {articulo}: '))
    total = articulo * cantidad
    total_compra += total 
  
  print(compra_total)

compra_total()