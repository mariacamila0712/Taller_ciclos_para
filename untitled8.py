# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:22:47 2021

@author: Maria Camila
"""

peso = 0
for i in range(1, 6):
    peso_anterior = int((input("Digite el peso anterior del miembro n°" + str(i)+": ")))
    for j in range(1, 11):
     peso += int((input("Digite el peso de la báscula n°"+ str(j)+ " del miembro " + str(i)+": ")))     
    if(peso_anterior-peso < 0):
     print("El miembro bajó: ", peso_anterior - (peso/10), " kilos.")
    if(peso_anterior-peso > 0):
     print("El miembro subió: ", peso_anterior - (peso/10), " kilos.")