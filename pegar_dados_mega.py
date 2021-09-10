'''Programa para pegar dados dos ultimos sorteios da mega sena usando Web Scraping e também gerar
jogos aleatorios que não venceram a mega sena. Assim, esses dados
podem ser usado para um futuro projeto de Machine Learning'''

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random
def get_data(type : str):
    if type == 'mega sena':
        print ('Pegando jogos Mega sena...')
        url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/'
        loc_num_jogos = f'//*[@id="conteudoresultado"]/div[1]/div/h2/span'
        loc_dados_csv = 'dados_mega.csv'
        numero_numeros = 6
        max_num = 60
        loc_click_anterior = f'//ul[@class="clearfix"]/li[2]/a'
    elif type == 'loto facil':
        print ('Pegando jogos Loto Facil...')
        url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/'
        loc_num_jogos = f'//*[@id="resultados"]/div[1]/div/h2/span'
        loc_dados_csv = 'dados_lotoFacil.csv'
        numero_numeros = 15
        max_num = 25
        loc_click_anterior = f'//*[@id="resultados"]/div[1]/div/div[2]/ul/li[2]/a'

    option = Options()
    option.headless = False
    driver = webdriver.Firefox(executable_path=r'venv\Scripts\geckodriver.exe')
    driver.get(url)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 300)")
    
    
    num_jogos = driver.find_element_by_xpath(loc_num_jogos).text
    num_jogos = num_jogos.split()
    num_jogos = int(num_jogos[1])
    try:
        data2 = pd.read_csv(loc_dados_csv)
        data2.query('Resultado == "vence"', inplace=True)
        num_antes = len(data2)
        dados_antes = data2.values

        numeros_list = []
        numeros_list= dados_antes
        numeros_list= numeros_list.tolist()
    except:
        num_antes = 0
        numeros_list = []


    print (f'\nNumero de Jogos: {num_jogos - num_antes} \n')
    for jogos in range(num_jogos - num_antes):
        list_prev = []
        for numero in range(numero_numeros):
            while True:
                try:
                    if type == 'mega sena':
                        numero_achado = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/section/div[2]/div[2]/div/div[2]/div[2]/div/div/ul/li[{numero+1}]').text
                    elif type == 'loto facil':
                        numero_achado = driver.find_element_by_xpath(f'//*[@id="resultados"]/div[2]/div/div/div[1]/ul/li[{numero}+1]').text
                    list_prev.append(numero_achado)
                    break
                except:
                    time.sleep(2)
        if type == 'mega sena':
            numeros_list.append(['vence',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]])
            print(f'Jogo {jogos+1}: {list_prev[0]}, {list_prev[1]}, {list_prev[2]}, {list_prev[3]}, {list_prev[4]}, {list_prev[5]}')
        elif type == 'loto facil':
            numeros_list.append(['vence',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5], list_prev[6], list_prev[7], list_prev[8], list_prev[9], list_prev[10], list_prev[11], list_prev[12], list_prev[13], list_prev[14]])
            print(f'Jogo {jogos+1}: {list_prev[0]}, {list_prev[1]}, {list_prev[2]}, {list_prev[3]}, {list_prev[4]}, {list_prev[5]}, {list_prev[6]}, {list_prev[7]}, {list_prev[8]}, {list_prev[9]}, {list_prev[10]}, {list_prev[11]}, {list_prev[12]}, {list_prev[13]}, {list_prev[14]}')
        time.sleep(1)
        while True:
            try:
                jogo_antes = driver.find_element_by_xpath(loc_click_anterior)
                driver.execute_script("arguments[0].click();", jogo_antes)
                time.sleep(1)
                break
            except:
                time.sleep(2)

    driver.quit()
    
    if type == 'mega sena':
        numeros_list_pandas = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6'])
    elif type == 'loto facil':
        numeros_list_pandas = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15'])
    numeros_list_pandas.drop(columns=['Resultado'], inplace=True)
    valores = numeros_list_pandas.values

    for a in range(num_jogos*5): #gerar jogos aleatorios que não venceram
        while True:
            list_prev = []
            for b in range(numero_numeros):
                while True:
                    gerar = random.randint(1,max_num)
                    if gerar < 10:
                        gerar = f'0{gerar}'
                    else:
                        gerar = str(gerar)
                    if gerar not in list_prev:
                        list_prev.append(gerar)
                        break
            
            if list_prev not in valores:
                list_prev.sort()
                if type == 'mega sena':
                    numeros_list.append(['perde',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]])
                elif type == 'loto facil':
                    numeros_list.append(['perde',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5], list_prev[6], list_prev[7], list_prev[8], list_prev[9], list_prev[10], list_prev[11], list_prev[12], list_prev[13], list_prev[14]])
                break
        print (f'{a+1}/{num_jogos*5}')
    print ('Guardando jogos...')

    random.shuffle(numeros_list)
    if type == 'mega sena':
        data = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6'])
    elif type == 'loto facil':
        data = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15'])
    data.to_csv(loc_dados_csv, encoding='utf-8', index=False)
    print('Jogos atualizados, vamos agora treinar o nosso algoritimo')
    
#def get_data_mega():
#    print ('Pegando jogos Mega sena...')
#    url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/'
#    option = Options()
#    option.headless = False
#    driver = webdriver.Firefox(executable_path=r'venv\Scripts\geckodriver.exe')
#    driver.get(url)
#    time.sleep(2)
#    driver.execute_script("window.scrollBy(0, 300)")
#    
#
#    num_jogos = driver.find_element_by_xpath(f'//*[@id="conteudoresultado"]/div[1]/div/h2/span').text
#    num_jogos = num_jogos.split()
#    num_jogos = int(num_jogos[1])
#    data2 = pd.read_csv('dados_mega.csv')
#    data2.query('Resultado == "vence"', inplace=True)
#    num_antes = len(data2)
#    dados_antes = data2.values
#
#    numeros_list = []
#    numeros_list= dados_antes
#    numeros_list= numeros_list.tolist()
#
#    print (f'\nNumero de Jogos: {num_jogos - num_antes} \n')
#    for jogos in range(num_jogos - num_antes):
#        list_prev = []
#        for numero in range(6):
#            while True:
#                try:
#                    numero_achado = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/section/div[2]/div[2]/div/div[2]/div[2]/div/div/ul/li[{numero+1}]').text
#                    list_prev.append(numero_achado)
#                    break
#                except:
#                    time.sleep(2)
#        numeros_list.append(['vence',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]])
#        print(f'Jogo {jogos+1}: {list_prev[0]}, {list_prev[1]}, {list_prev[2]}, {list_prev[3]}, {list_prev[4]}, {list_prev[5]}')
#        time.sleep(1)
#        while True:
#            try:
#                jogo_antes = driver.find_element_by_xpath(f'//ul[@class="clearfix"]/li[2]/a')
#                driver.execute_script("arguments[0].click();", jogo_antes)
#                time.sleep(1)
#                break
#            except:
#                time.sleep(2)
#
#    driver.quit()
#
#    numeros_list_pandas = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6'])
#    numeros_list_pandas.drop(columns=['Resultado'], inplace=True)
#    valores = numeros_list_pandas.values
#
#    for a in range(num_jogos*5): #gerar jogos aleatorios que não venceram
#        while True:
#            list_prev = []
#            for b in range(6):
#                while True:
#                    gerar = random.randint(1,60)
#                    if gerar < 10:
#                        gerar = f'0{gerar}'
#                    else:
#                        gerar = str(gerar)
#                    if gerar not in list_prev:
#                        list_prev.append(gerar)
#                        break
#            
#            if list_prev not in valores:
#                list_prev.sort()
#                numeros_list.append(['perde',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]])
#                break
#    random.shuffle(numeros_list)
#    data = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6'])
#    data.to_csv('dados_mega.csv', encoding='utf-8', index=False)
#    print('Jogos atualizados, vamos agora treinar o nosso algoritimo')
#
#def get_data_lotofacil():
#    print ('Pegando jogos Loto Facil...')
#    url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/'
#    option = Options()
#    option.headless = False
#    driver = webdriver.Firefox(executable_path=r'venv\Scripts\geckodriver.exe')
#    driver.get(url)
#    time.sleep(2)
#    driver.execute_script("window.scrollBy(0, 300)")
#    
#
#    num_jogos = driver.find_element_by_xpath(f'//*[@id="resultados"]/div[1]/div/h2/span').text
#    num_jogos = num_jogos.split()
#    num_jogos = int(num_jogos[1])
#    try:
#        data2 = pd.read_csv('dados_lotoFacil.csv')
#        data2.query('Resultado == "vence"', inplace=True)
#        num_antes = len(data2)
#        dados_antes = data2.values
#
#        numeros_list = []
#        numeros_list= dados_antes
#        numeros_list= numeros_list.tolist()
#    except:
#        num_antes = 0
#        numeros_list = []
#
#    print (f'\nNumero de Jogos: {num_jogos - num_antes} \n')
#    for jogos in range(num_jogos - num_antes):
#        list_prev = []
#        for numero in range(15):
#            while True:
#                try:
#                    numero_achado = driver.find_element_by_xpath(f'//*[@id="resultados"]/div[2]/div/div/div[1]/ul/li[{numero}+1]').text
#                    list_prev.append(numero_achado)
#                    break
#                except:
#                    time.sleep(2)
#        numeros_list.append(['vence',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5], list_prev[6], list_prev[7], list_prev[8], list_prev[9], list_prev[10], list_prev[11], list_prev[12], list_prev[13], list_prev[14]])
#        print(f'Jogo {jogos+1}: {list_prev[0]}, {list_prev[1]}, {list_prev[2]}, {list_prev[3]}, {list_prev[4]}, {list_prev[5]}, {list_prev[6]}, {list_prev[7]}, {list_prev[8]}, {list_prev[9]}, {list_prev[10]}, {list_prev[11]}, {list_prev[12]}, {list_prev[13]}, {list_prev[14]}')
#        time.sleep(1)
#        while True:
#            try:
#                jogo_antes = driver.find_element_by_xpath(f'//*[@id="resultados"]/div[1]/div/div[2]/ul/li[2]/a')
#                driver.execute_script("arguments[0].click();", jogo_antes)
#                time.sleep(1)
#                break
#            except:
#                time.sleep(2)
#
#    driver.quit()
#
#    numeros_list_pandas = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15'])
#    numeros_list_pandas.drop(columns=['Resultado'], inplace=True)
#    valores = numeros_list_pandas.values
#    #print (valores)
#
#    for a in range(num_jogos*5): #gerar jogos aleatorios que não venceram
#        while True:
#            list_prev = []
#            #print (list_prev)
#            for b in range(15):
#                while True:
#                    gerar = random.randint(1,25)
#                    if gerar < 10:
#                        gerar = f'0{gerar}'
#                    else:
#                        gerar = str(gerar)
#                    if gerar not in list_prev:
#                        list_prev.append(gerar)
#                        break
#            
#            if list_prev not in valores:
#                list_prev.sort()
#                numeros_list.append(['perde',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5], list_prev[6], list_prev[7], list_prev[8], list_prev[9], list_prev[10], list_prev[11], list_prev[12], list_prev[13], list_prev[14]])
#                #print (numeros_list)
#                break
#        print (f'{a+1}/{num_jogos*5}')
#            
#                
#    random.shuffle(numeros_list)
#    data = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6','numero 7','numero 8','numero 9','numero 10','numero 11','numero 12','numero 13','numero 14','numero 15'])
#    data.to_csv('dados_lotoFacil.csv', encoding='utf-8', index=False)
#    print('Jogos atualizados, vamos agora treinar o nosso algoritimo')
#
#