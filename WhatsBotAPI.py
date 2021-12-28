from __future__ import print_function
from time import sleep, time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from numpy import string_
import pandas as pd
from IPython.display import display
import getpass, random, time, urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#cria o scopo - o que vai ser feito
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#caminho do json com credenciais
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '11tR34CLHoBnZLQQDMDunh0MJ3UsvyO_F4CMUxsmxI2Y'
SAMPLE_RANGE_NAME = 'Mensagens!A6:H'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
try:
    service = build('sheets', 'v4', credentials=creds)

    ## Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()                         
    values = result.get('values', []) #organiza os valores entre []
    colums_names = ['Data','Nome','Nome Completo','NumeroRaw','Numero','Marca','Modelo','Mensagem']#define nome das colunas de df1 e new_df
    contatos_df = pd.DataFrame(values, columns= colums_names) #cria dataframe com dados da api ja prontos para mandar
    
    ## Rotina para mandar mensagens pelo chromedriver 
    usern = getpass.getuser()
    profiledir = r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default".format(usern)
    options = webdriver.ChromeOptions()
    options.add_argument(profiledir)
    #while len(navegador.find_element_by_id("side")) < 1:
    #time.sleep(5)
    navegador = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)
    navegador.get("https://web.whatsapp.com/")
    time.sleep(random.randint(35,40)) #tempo para escanear QR code
    x = 0
    for i, mensagem in enumerate(contatos_df['Mensagem']):
        #dia = contatos_df.loc[i,"Data"]
        #if dia == date_time:
        pessoa = contatos_df.loc[i,"Nome"]
        numero = contatos_df.loc[i,"Numero"]
        #print(numero,"",pessoa,"",dia)
        if x == 0:
            textcod = urllib.parse.quote(mensagem) #transforma a mensagem em cod url, pode customisar com variaveis
            link = f"https://web.whatsapp.com/send?phone={numero}&text={textcod}"
            navegador.get(link)
            time.sleep(random.randint(20,25))
            #while len(navegador.find_element_by_id("side")) < 1:
            #time.sleep(1)
            x = 1
            try: #tenta apertar enter, se nao der avisa que deu errado
                navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER) # copiamos o XPATH da caixa de texto e vamos dar enter
            except:
                print(f"Numero errado de {pessoa}, ver se {numero} está correto")
            time.sleep(random.randint(6,10)) #tempo para envio da mensagem
        else:
            if contatos_df.loc[i,"Nome Completo"] != contatos_df.loc[i-1,"Nome Completo"]:
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


except HttpError as err:
    print(err)

if __name__ == '__main__':
    main()