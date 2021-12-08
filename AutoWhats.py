
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import urllib
from datetime import date, datetime
import random

contatos_df = pd.read_excel("TesteReal1.xlsx")
options = webdriver.ChromeOptions()
#options.add_argument(r"--user-data-dir=C:\Users\Usuário\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument(r"--user-data-dir=C:\Users\Usuário\AppData\Local\Google\Chrome\User Data\Default")
#while len(navegador.find_element_by_id("side")) < 1:
    #time.sleep(5)
navegador = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)
navegador.get("https://web.whatsapp.com/")
time.sleep(random.randint(35,40)) #tempo para escanear QR code

now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y")
print(date_time)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    dia = contatos_df.loc[i,"Data"]
    #if dia == date_time:
    pessoa = contatos_df.loc[i,"Nome"]
    numero = contatos_df.loc[i,"Numero"]
    #print(numero,"",pessoa,"",dia)
    textcod = urllib.parse.quote(mensagem) #transforma a mensagem em cod url, pode customisar com variaveis
    link = f"https://web.whatsapp.com/send?phone={numero}&text={textcod}"
    navegador.get(link)
    time.sleep(random.randint(20,25))
    #while len(navegador.find_element_by_id("side")) < 1:
    #time.sleep(1)
    try: #tenta apertar enter, se nao der avisa que deu errado
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER) # copiamos o XPATH da caixa de texto e vamos dar enter
    except:
        print(f"Numero errado de {pessoa}, ver se {numero} está correto")
    time.sleep(random.randint(6,10)) #tempo para envio da mensagem