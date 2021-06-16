'''Programa para pegar dados dos ultimos sorteios da mega sena usando Web Scraping e também gerar
jogos aleatorios que não venceram a mega sena. Assim, esses dados
podem ser usado para um futuro projeto de Machine Learning'''

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random
print ('Pegando jogos...')
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/'
option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'venv\Scripts\geckodriver.exe')
driver.get(url)
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300)")

numeros_list = []
for jogos in range(2359):
    list_prev = []
    for numero in range(6):
        while True:
            try:
                numero_achado = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/section/div[2]/div[2]/div/div[2]/div[2]/div/div/ul/li[{numero+1}]').text
                list_prev.append(numero_achado)
                break
            except:
                time.sleep(2)
    numeros_list.append(('vence',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]))
    print(f'Jogo {jogos+1}: {list_prev[0]}, {list_prev[1]}, {list_prev[2]}, {list_prev[3]}, {list_prev[4]}, {list_prev[5]}')
    time.sleep(1)
    while True:
        try:
            jogo_antes = driver.find_element_by_xpath(f'//ul[@class="clearfix"]/li[2]/a')
            driver.execute_script("arguments[0].click();", jogo_antes)
            time.sleep(1)
            break
        except:
            time.sleep(2)

driver.quit()

for a in range(11795): #gerar 11795 jogos aleatorios que não venceram
    while True:
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
        if list_prev not in numeros_list:
            list_prev.sort()
            numeros_list.append(('perde',list_prev[0], list_prev[1], list_prev[2], list_prev[3], list_prev[4], list_prev[5]))
            break
random.shuffle(numeros_list)
data = pd.DataFrame(numeros_list, columns=['Resultado','numero 1','numero 2','numero 3','numero 4','numero 5','numero 6'])
data.to_csv('dados_mega.csv', encoding='utf-8', index=False)
print(data)
para = input()
