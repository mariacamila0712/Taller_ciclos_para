# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:54:38 2021

@author: Maria Camila
"""
# La empresa Encuestas S.A desea crear una función que les permita
# conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
# el ganador o indicar si hubo empate y la cantidad de votos obtenidos
candidato1 = 0
candidato2 = 0
candidato3 = 0
ganador = 0

for i in range(0, 50000):
    voto = int(input('¿Por cuál candidato votó? Digite el 1,2 o 3?'))
    if voto == 1:
        candidato1 += 1
    if voto == 2:
        candidato2 += 1
    if voto == 3:
        candidato3 += 1

if candidato1 > candidato2 and candidato1 > candidato3:
    ganador = 1
if candidato2 > candidato1 and candidato2 > candidato3:
    ganador = 2
if candidato3 > candidato1 and candidato3 > candidato2:
    ganador = 3

print('El primer candidato recibio', candidato1, 'votos')
print('El segundo candidato recibio', candidato2, 'votos')
print('El tercer candidato recibio', candidato3, 'votos')
print("El ganador fue el candidato", ganador)
