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
HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A5:G90'


def main(sample_range_name):
    global values
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
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


control = 0

# Customer selection screen
while True:
    customers = [1, 2, 3, 4, 5]
    customer = 404
    customerName = ''

    showCustomers()
    while customer not in customers:
        customer = int(input('Selecione um cliente: '))
        if customer == 0:
            quit()
        if customer not in customers:
            os.system('cls')
            showCustomers()
            print('Erro. Informe o código de um cliente válido!\n')
            continue

    # Branch selection screen
    while True:
        branches = []
        branch = 404

        if customer == 1:
            branches = [1, 2, 3, 4, 9]
            customerName = 'Beltrame'

            os.system('cls')
            showBranches(customerName)
            while branch not in branches:
                branch = int(input('Selecione uma loja: '))
                if branch == 9:
                    break
                elif branch == 0:
                    quit()

                if branch not in branches:
                    os.system('cls')
                    showBranches(customerName)
                    print('Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Beltrame!A5:K23'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A5:G23'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Beltrame!A25:K41'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A25:G41'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Beltrame!A43:K72'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A43:G72'
                elif branch == 4:
                    SAMPLE_RANGE_NAME = 'Beltrame!A74:K90'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A74:G90'

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
                elif branch == 0:
                    quit()

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
                elif branch == 0:
                    quit()

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
                elif branch == 0:
                    quit()

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
                elif branch == 0:
                    quit()

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
            os.system('cls')
            break
        elif branch == 0:
            quit()
        else:
            values = main(SAMPLE_RANGE_NAME)

        # Remove the rows that's not going to be used
        os.system('cls')
        values = cleaningData(values)

        # Printing which branch is being showed and popping it after
        option = 404
        branchName = ''
        values = showBranch(option, values)

        # Shows the info based on the new 'values' list
        while True:
            if control == 99:  # Verifying if the program already passed for VIEW MORE and resetting the data collection
                values = main(SAMPLE_RANGE_NAME)
                values = cleaningData(values)
                values = showBranch(option, values)

            displayCompInfo(values, customerName)

            # Menu -- view more details / back to showBranches() / exit
            options = [1]

            while option not in options:
                option = int(
                    input('\nFiltro encerrado. Selecione uma opção:\n1.DETALHES\n9.VOLTAR\n0.SAIR\nOpção: '))
                if option == 9:
                    break
                elif option == 0:
                    quit()

                if option not in options:
                    os.system('cls')
                    option = int(input('\nOpção inválida. Selecione uma '
                                       'opção:\n1.DETALHES\n9.VOLTAR\n0.SAIR\nOpção: '))
                    continue

            if option == 9:
                break
            elif option == 0:
                quit()

            # Option 1 - View more details
            if option == 1:
                compTypes = ['c', 'v', 'p', '9', '0']
                compType = ''
                concentratorOptions = [1]
                concentratorOption = 404

                os.system('cls')
                while compType not in compTypes:
                    showCompTypes(branchName)
                    compType = input('Selecione uma opção: ')
                    if compType not in compTypes:
                        os.system('cls')
                        showCompTypes(branchName)
                        print('Erro. Selecione uma opção válida!\n')
                        continue

                    # Selecting a computer type
                    if compType == 'c':
                        concRow = []
                        valuesS = main(SAMPLE_RANGE_NAME)
                        valuesH = main(HARDWARE_RANGE_NAME)

                        os.system('cls')
                        header(f'> CONCENTRADOR - {branchName} <\n')
                        for indexS, rowS in enumerate(valuesS):
                            if 'concentrador' in rowS[0].lower():
                                concRow = rowS
                                print(concRow)
                        showConcOptions()
                        while concentratorOption not in concentratorOptions:
                            concentratorOption = int(input('Selecione uma opção: '))
                            if concentratorOption == 9:
                                compType = ''
                                os.system('cls')
                                break
                            elif concentratorOption == 0:
                                quit()
                            if concentratorOption not in concentratorOptions:
                                os.system('cls')
                                showConcOptions()
                                print('Erro. Selecione uma opção válida!\n')
                                continue

                if compType == '9':
                    if concentratorOption == 9:
                        control = 99
                    option = 0
                    continue
                elif compType == '0':
                    quit()
