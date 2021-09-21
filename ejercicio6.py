# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:22:49 2021

@author: Maria Camila
"""
# Cinco miembros de un club contra la obesidad desean saber cuanto han
# bajado o subido de peso desde la última vez que se reunieron. Para esto se
# debe realizar un ritual de pesaje en donde cada uno se pesa en diez
# básculas distintas para así tener el pormedio mas exacto de su peso. Si
# existe diferencia positiva entre este promedio de peso y el peso de la última
# vez que se reunieron, significa que subieron de peso. Pero si la diferencia
# es negativa, significa que bajaron. Lo que el problema requere es que por
# cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
# cantidad de kilos que subió o bajó de peso
peso = 0
for n in range(1, 6):
    peso_anterior = int((input(f'Digite el peso anterior del miembro número {n}:' ))
    for a in range(1, 11):
     peso += int((input(f'Digite el peso de la báscula número {a} del miembro {i}: '))     
if(peso_anterior-peso < 0):
    print("El miembro bajó: ", peso_anterior - (peso/10), " kilos.")
if(peso_anterior-peso > 0):
    print("El miembro subió: ", peso_anterior - (peso/10), " kilos.")
