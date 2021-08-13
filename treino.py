import pandas as pd
from sklearn.model_selection import train_test_split #separar base para treino e teste
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score #definir a acuracia
import matplotlib.pyplot as plt
import pickle

def train_mega():
    data = pd.read_csv('dados_mega.csv')
    X = data.drop(columns=['Resultado'])
    y = data[['Resultado']]

    while True:
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.15)
        print ('\nQtd dados para treino: ', len(X_train))
        print ('Qtd dados para teste: ', len(X_test))
        print ('Total: ', len(X_train)+ len(X_test))

        obj = KNeighborsClassifier(n_neighbors=6,metric='euclidean')
        obj.fit(X_train, y_train)

        y_pred = obj.predict(X_test)
        precisao = accuracy_score(y_test,y_pred)
        print ('\nPrecisão de: ',precisao)

        repetir = int(input('Deseja repetir o treinamento da IA?\n1- Sim\n2- Não\n'))
        if repetir == 1:
            continue
        else:
            break


    with open('modelo_mega.pkl', 'wb') as fid:
        pickle.dump(obj, fid)

    print ('Treinamento reaalizado com sucesso!!')

def train_lotoFacil():
    data = pd.read_csv('dados_lotoFacil.csv')
    X = data.drop(columns=['Resultado'])
    y = data[['Resultado']]

    while True:
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.15)
        print ('\nQtd dados para treino: ', len(X_train))
        print ('Qtd dados para teste: ', len(X_test))
        print ('Total: ', len(X_train)+ len(X_test))

        obj = KNeighborsClassifier(n_neighbors=15,metric='euclidean')
        obj.fit(X_train, y_train)

        y_pred = obj.predict(X_test)
        precisao = accuracy_score(y_test,y_pred)
        print ('\nPrecisão de: ',precisao)

        repetir = int(input('Deseja repetir o treinamento da IA?\n1- Sim\n2- Não\n'))
        if repetir == 1:
            continue
        else:
            break


    with open('modelo_lotoFacil.pkl', 'wb') as fid:
        pickle.dump(obj, fid)

    print ('Treinamento reaalizado com sucesso!!')

