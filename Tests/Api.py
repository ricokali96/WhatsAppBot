from __future__ import print_function
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#cria o scopo - o que vai ser feito
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#caminho do json com credenciais
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1KG11x-xtsQLL2o4NHUGykfhedrCxSJ9y6UDohAVtkq4'
SAMPLE_RANGE_NAME = 'Clientes!A1:C'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
try:
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    #organiza os valores entre []                            
    values = result.get('values', [])

    if not values:
        print("No data found.")
    print(values)
    print(result)

    #print('Name, Major:')
    #for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
        #print('%s, %s' % (row[0], row[4]))
except HttpError as err:
    print(err)


if __name__ == '__main__':
    main()