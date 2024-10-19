import numpy as np
import pandas as pd
import statistics as stat
import matplotlib.pyplot as pl
import math
0.284
#DATA_FILE: = "lista_boot_means.txt"

sync = np.array([41.60, 41.48, 42.34, 41.95, 41.86, 42.18, 41.72, 42.26, 41.81, 42.04 ])


'''
x = sync.mean()

erro = sync.std(ddof=1)/math.sqrt(len(sync))
print(f"Erro: ", erro)
print(f"Intervalo para a média populacional: ", x-3* erro, x+3*erro)


bootsample=np.random.choice(sync, size= 10, replace=True)


bootmean=np.mean(bootsample_means)

#range


'''
data_emp= np.array([24.1514, 27.4145, 20.4000, 22.5151, 28.5152, 28.5611, 21.2489, 20.9983, 24.9840, 22.6245])

y= data_emp.mean()

erro = data_emp.std(ddof=1)/math.sqrt(len(data_emp))
print(f"Intervalo para os pedidos de emprestimos: ", y-3* erro, y+3*erro)


lista_medias = []
for media in range(0, 201):
    bootstrap_data = np.random.choice(data_emp, size = 10, replace= True)
    soma  = 0

    for numero in data_emp:
        soma += numero
    lista_medias.append(soma/10)

print(lista_medias)

media_bootstrap = np.mean(lista_medias)
print(f"Media Intervalo para os pedidos de emprestimos: ", media_bootstrap-3* erro, media_bootstrap+3*erro)