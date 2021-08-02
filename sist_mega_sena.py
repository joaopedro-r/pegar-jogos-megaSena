import gerar_numeros
import pegar_dados_mega
import treino
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
    #print(prob)
    
    nomes =['numero 1', 'numero 2', 'numero 3', 'numero 4', 'numero 5', 'numero 6']
    numeros_gerados.columns = nomes

    data_veri = numeros_gerados
    data_veri['Previsão'] = y_pred
    data_veri['Prob perder'] = round(prob[0]*100,2)
    data_veri['Prob ganhar'] = round(prob[1]*100,2)
    #print (data_veri)
    acertos = data_veri.query('Previsão == "vence"')
    print (acertos)

def verificar(numeros):
    numeros = {'numero 1':[numeros[0]], 'numero 2': [numeros[1]], 'numero 3':[numeros[2]], 'numero 4':[numeros[3]], 'numero 5':[numeros[4]], 'numero 6':[numeros[5]],}
    numeros = pd.DataFrame(numeros)

    y_pred = loaded_model.predict(numeros)
    prob = loaded_model.predict_proba(numeros)
    prob = pd.DataFrame(prob)
    
    nomes =['numero 1', 'numero 2', 'numero 3', 'numero 4', 'numero 5', 'numero 6']
    numeros.columns = nomes

    data_veri = numeros
    data_veri['Previsão'] = y_pred
    data_veri['Prob perder'] = round(prob[0]*100,2)
    data_veri['Prob ganhar'] = round(prob[1]*100,2)
    print (data_veri)
    


    
loaded_model = pickle.load(open('teste.pkl', 'rb'))
print ('Sistema Mega Sena')
while True:
    print ('=-'*30)
    print ('\nMenu')
    print ('1- Gerar jogos aleatorios e verificar')
    print ('2- Verificar meu jogo')
    print ('3- Atualizar a IA')
    opcao = int(input('Opção: '))
    print ('\n\n')


    numeros = []
    if opcao == 1:
        gerar(loaded_model)
    elif opcao == 2:
        for a in range (6):
            num = int(input(f'Insira o {a+1}º número: '))
            numeros.append(num)
        verificar(numeros)
    elif opcao == 3:
        certeza = int(input('Tem Certeza? este processo pode levar algumas horas\n1- Sim\n2- Não\n'))
        if certeza == 1:
            pegar_dados_mega.get_data()
            treino.train()
        

