'''Gera jogos aleatorios da mega sena'''

import random
import pandas as pd

def generate():
    lista_numeros = []
    for a in range(500):
        list_prev = []
        for b in range(6):
            while True:
                gerar = random.randint(1,60)
                if gerar < 10:
                    gerar = f'0{gerar}'
                else:
                    gerar = str(gerar)
                if gerar not in list_prev:
                    list_prev.append(gerar)
                    break

        list_prev.sort()
        lista_numeros.append((list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]))

    data = pd.DataFrame(lista_numeros)
    data.to_csv('numeros_previsao.csv', encoding='utf-8', index=False)
    #print(data)