from __future__ import print_function

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# System lib (Alpha)
import os

# Dealing with data (preAlpha) -- data.py; showStuff.py
# from data import *
from showStuff import *

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1zxWiR0S2ZGTkLAlipqbuODsazF6YHTkNs0b7YVnFXfo'
SAMPLE_RANGE_NAME = 'Beltrame!A5:K90'


def main(sample_range_name=SAMPLE_RANGE_NAME):
    global values
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file(
            #     'credentials.json', SCOPES)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        # Read information from the Sheet
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=sample_range_name).execute()

        # Collecting just the values from the dict received from get (r43).
        values = result['values']

        # Dealing with the case of not getting values from the spreadsheet.
        if not values:
            print('No data found.')
            return

    except HttpError as err:
        print(err)

    return values


if __name__ == '__main__':
    main()


# Customer selection screen
while True:
    customer = 0
    customers = [1, 2, 3, 4, 5]
    customerName = ''

    showCustomers()
    while customer not in customers:
        customer = int(input('Selecione um cliente: '))
        if customer not in customers:
            os.system('cls')
            showCustomers()
            print('Erro. Informe o código de um cliente válido!\n')
            continue

    # Branch selection screen
    while True:
        branches = []
        branch = 0

        os.system('cls')
        if customer == 1:
            branches = [1, 2, 3, 4, 9]
            customerName = 'Beltrame'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Beltrame!A5:K23'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Beltrame!A25:K41'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Beltrame!A43:K72'
                elif branch == 4:
                    SAMPLE_RANGE_NAME = 'Beltrame!A74:K90'

        elif customer == 2:
            branches = [1, 9]
            customerName = 'Bom Preço'
            SAMPLE_RANGE_NAME = 'BomPreco!A5:K17'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'BomPreco!A5:K17'

        elif customer == 3:
            branches = [1, 2, 3, 9]
            customerName = 'Lima'
            SAMPLE_RANGE_NAME = 'Lima!A5:J41'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Lima!A5:J16'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Lima!A18:J28'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Lima!A30:J41'

        elif customer == 4:
            branches = [1, 2, 9]
            customerName = 'Pazini'
            SAMPLE_RANGE_NAME = 'Pazini!A5:K23'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Pazini!A5:K14'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Pazini!A16:K25'

        elif customer == 5:
            branches = [1, 2, 3, 9]
            customerName = 'Único'
            SAMPLE_RANGE_NAME = 'Único!A5:J74'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Único!A5:J29'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Único!A31:J48'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Único!A50:J71'

        if branch == 9:
            break
        else:
            values = main(SAMPLE_RANGE_NAME)

        # Remove the rows that's not going to be used
        os.system('cls')
        for i, row in enumerate(values):
            if not row:  # [] -- empty rows
                values.pop(i)
            for register in row:
                if register == 'Descrição' or 'verificação' in register:  # removing the headers and BD verification row
                    values.pop(i)
                else:
                    continue

        # Printing which branch is being showed and popping it after
        for i, row in enumerate(values):
            if 'Loja' in row[0]:
                branchName = row[0]
                print(branchName.upper())
                values.pop(i)

            # Shows the info based on the new 'values' list
            displayCompInfo(values, customerName)

            exitChoice = input('\nFiltro encerrado. Selecione uma opção:\n9.VOLTAR\n0.SAIR\nOpção: ')

            while exitChoice != '9' and exitChoice != '0':
                if exitChoice not in ['9', '0']:
                    exitChoice = input('\nOpção inválida. Selecione uma opção:\n9.VOLTAR\n0.SAIR\nOpção: ')

            if exitChoice == '9':
                # os.system('cls')
                break
            elif exitChoice == '0':
                quit()
