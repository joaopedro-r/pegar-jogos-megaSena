import gerar_numeros
import pegar_dados_mega
import treino
import pickle
import pandas as pd
from sklearn.metrics import precision_score


def gerar_mega():
    rodada = 1
    total_jogos = 0
    loaded_model = pickle.load(open('modelo_mega.pkl', 'rb'))
    while True:
        gerar_numeros.generate_mega()
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
        acertos = acertos.loc[acertos['Prob ganhar'] > 90]
        total_jogos += len(numeros_gerados)
        print (f'Rodada: {rodada}')
        print (f'Jogos: {total_jogos}')
        if len(acertos)>0:
            print (acertos)
            break
        else:
            rodada+=1
            continue

def gerar_lotoFacil():
    rodada = 1
    total_jogos = 0
    loaded_model = pickle.load(open('modelo_lotoFacil.pkl', 'rb'))
    while True:
        gerar_numeros.generate_lotoFacil()
        numeros_gerados = pd.read_csv('numeros_previsao.csv')
        y_pred = loaded_model.predict(numeros_gerados)
        prob = loaded_model.predict_proba(numeros_gerados)
        #print(y_pred)
        prob = pd.DataFrame(prob)
        #print(prob)
        
        nomes =['numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15']
        numeros_gerados.columns = nomes

        data_veri = numeros_gerados
        data_veri['Previsão'] = y_pred
        data_veri['Prob perder'] = round(prob[0]*100,2)
        data_veri['Prob ganhar'] = round(prob[1]*100,2)
        #print (data_veri)
        acertos = data_veri.query('Previsão == "vence"')
        acertos = acertos.loc[acertos['Prob ganhar'] >= 60]
        total_jogos += len(numeros_gerados)
        print (f'Rodada: {rodada}')
        print (f'Jogos: {total_jogos}')
        pd.set_option('display.max_columns', None)
        if len(acertos)>0:
            print (acertos)
            break
        else:
            rodada+=1
            continue

def verificar_mega(numeros):
    loaded_model = pickle.load(open('modelo_mega.pkl', 'rb'))
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

def verificar_lotoFacil(numeros):
    loaded_model = pickle.load(open('modelo_lotoFacil.pkl', 'rb'))
    numeros = {'numero 1':[numeros[0]], 'numero 2': [numeros[1]], 'numero 3':[numeros[2]], 'numero 4':[numeros[3]], 'numero 5':[numeros[4]], 'numero 6':[numeros[5]], 'numero 7':[numeros[6]], 'numero 8':[numeros[7]], 'numero 9':[numeros[8]], 'numero 10':[numeros[9]], 'numero 11':[numeros[10]], 'numero 12':[numeros[11]], 'numero 13':[numeros[12]], 'numero 14':[numeros[13]], 'numero 15':[numeros[14]]}
    numeros = pd.DataFrame(numeros)

    y_pred = loaded_model.predict(numeros)
    prob = loaded_model.predict_proba(numeros)
    prob = pd.DataFrame(prob)
    
    nomes =['numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15']
    numeros.columns = nomes

    data_veri = numeros
    data_veri['Previsão'] = y_pred
    data_veri['Prob perder'] = round(prob[0]*100,2)
    data_veri['Prob ganhar'] = round(prob[1]*100,2)
    pd.set_option('display.max_columns', None)
    print (data_veri)

    


    

print ('Sistema Mega Sena')
while True:
    print ('=-'*30)
    print ('\nMenu')
    print ('1- Gerar jogos aleatorios e verificar')
    print ('2- Verificar meu jogo')
    print ('3- Atualizar a IA')
    print ('4- Encerrar programa')
    opcao = int(input('Opção: '))
    print ('\n\n')


    numeros = []
    if opcao == 1:
        print ('1- Mega sena')
        print ('2- Loto Fácil')
        new_opcao = int(input('Opção: '))
        if new_opcao == 1:        
            gerar_mega()
        else:
            gerar_lotoFacil()
    elif opcao == 2:
        print ('1- Mega sena')
        print ('2- Loto Fácil')
        new_opcao = int(input('Opção: '))
        if new_opcao == 1:
            for a in range (6):
                num = int(input(f'Insira o {a+1}º número: '))
                numeros.append(num)
            verificar_mega(numeros)
        else:
            for a in range (15):
                num = int(input(f'Insira o {a+1}º número: '))
                numeros.append(num)
            verificar_lotoFacil(numeros)
    elif opcao == 3:
        print ('1- Mega sena')
        print ('2- Loto Fácil')
        new_opcao = int(input('Opção: '))
        if new_opcao == 1:
            certeza = int(input('Tem Certeza? este processo pode levar algumas horas\n1- Sim\n2- Não\n'))
            if certeza == 1:
                pegar_dados_mega.get_data_mega()
                treino.train_mega()
        else:
            certeza = int(input('Tem Certeza? este processo pode levar algumas horas\n1- Sim\n2- Não\n'))
            if certeza == 1:
                pegar_dados_mega.get_data_lotofacil()
                treino.train_lotoFacil()
    elif opcao == 4:
        break
        

