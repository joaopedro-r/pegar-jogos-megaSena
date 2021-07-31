import gerar_numeros
import pickle
import pandas as pd
from sklearn.metrics import precision_score

def gerar(loaded_model):
    gerar_numeros.generate()
    numeros_gerados = pd.read_csv('numeros_previsao.csv')
    y_pred = loaded_model.predict(numeros_gerados)
    prob = loaded_model.predict_proba(numeros_gerados)
    #print(y_pred)
    prob = pd.DataFrame(prob)
    print(prob)
    
    nomes =['numero 1', 'numero 2', 'numero 3', 'numero 4', 'numero 5', 'numero 6']
    numeros_gerados.columns = nomes

    data_veri = numeros_gerados
    data_veri['Previsão'] = y_pred
    data_veri['Prob perder'] = prob[0]
    data_veri['Prob ganhar'] = prob[1]
    #print (data_veri)
    acertos = data_veri.query('Previsão == "vence"')
    print (acertos)


loaded_model = pickle.load(open('teste.pkl', 'rb'))
print ('Sistema Mega Sena')

print ('\nMenu')
print ('1- Gerar jogos aleatorios e verificar')
print ('2- Verificar meu jogo')
opção = int(input('Opção: '))

if opção == 1:
    gerar(loaded_model)
