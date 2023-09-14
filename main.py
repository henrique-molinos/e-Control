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
SAMPLE_SPREADSHEET_ID = '1Jj74J-d-AYBZjFhk5F0eppoDiKJB3uBx7AugB_lpG3w'
SAMPLE_RANGE_NAME = 'Beltrame!A5:K117'
HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A5:F117'


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

    if control == 0:
        os.system('cls')
        showCustomers()
    else:
        showCustomers()

    while customer not in customers:
        customer = int(input('Selecione um cliente: '))
        if customer == 0:
            quit()
        if customer not in customers:
            os.system('cls')
            showCustomers()
            print('> Erro. Informe o código de um cliente válido!\n')
            continue

    # Branch selection screen
    while True:

        if control == 9:
            control = 0
            break

        branches = []
        branch = 404

        if customer == 1:
            branches = [1, 2, 3, 4, 5, 9]
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
                    print('> Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Beltrame!A5:K23'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A5:F23'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Beltrame!A25:K41'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A25:F41'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Beltrame!A43:K72'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A43:F72'
                elif branch == 4:
                    SAMPLE_RANGE_NAME = 'Beltrame!A74:K90'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A74:F90'
                elif branch == 5:
                    SAMPLE_RANGE_NAME = 'Beltrame!A92:K117'
                    HARDWARE_RANGE_NAME = 'Beltrame_Hardware!A92:F117'

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
                    print('> Erro. Informe o código de uma loja válida!\n')
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
                    print('> Erro. Informe o código de uma loja válida!\n')
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
                    print('> Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Pazini!A5:K14'
                    HARDWARE_RANGE_NAME = 'Pazini_Hardware!A5:F14'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Pazini!A16:K25'
                    HARDWARE_RANGE_NAME = 'Pazini_Hardware!A16:F25'

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
                    print('> Erro. Informe o código de uma loja válida!\n')
                    continue

                # Defining ranges on the table
                if branch == 1:
                    SAMPLE_RANGE_NAME = 'Único!A5:J29'
                    HARDWARE_RANGE_NAME = 'Único_Hardware!A5:F29'
                elif branch == 2:
                    SAMPLE_RANGE_NAME = 'Único!A31:J48'
                    HARDWARE_RANGE_NAME = 'Único_Hardware!A31:F48'
                elif branch == 3:
                    SAMPLE_RANGE_NAME = 'Único!A50:J71'
                    HARDWARE_RANGE_NAME = 'Único_Hardware!A50:F71'

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
        values, branchName = showBranch(option, values)

        # Shows the info based on the new 'values' list
        while True:
            # Verifying if the program already passed for VIEW MORE and resetting the data collection
            if control == 999:
                values = main(SAMPLE_RANGE_NAME)
                values = cleaningData(values)
                values, branchName = showBranch(option, values)  # END of verification and reset

            displayCompInfo(values, customerName)

            # Menu -- view details / back to showBranches() / exit
            options = [1]

            while option not in options:
                print('\n> Filtro encerrado.')
                showCompOptions()
                option = int(input('Selecione uma opção: '))
                if option == 9:
                    break
                elif option == 0:
                    control = 9
                    break
                if option not in options:
                    os.system('cls')
                    header(f'> SELEÇÃO DE OPÇÕES - {branchName} <\n')
                    print('> Erro. Selecione uma opção válida!')
                    continue

            if option == 9:
                break
            elif option == 0:
                control = 9
                break

            # Option 1 - View details based on computer type
            if option == 1:
                compTypes = [1, 2, 3, 9, 0]  # 1.Concentrador/2.Vasilhame/3.Pdv
                compType = 404
                computerOptions = [1]
                computerOption = 404

                os.system('cls')
                showCompTypes(branchName)
                while compType not in compTypes:
                    # Verifying if the program already passed for VIEW MORE and resetting the data collection
                    if control in [99, 999]:
                        os.system('cls')
                        showCompTypes(branchName)
                        compType = int(input('Selecione uma opção: '))  # END of verification
                        if compType not in compTypes:
                            os.system('cls')
                            showCompTypes(branchName)
                            print('> Erro. Selecione uma opção válida!\n')
                            continue
                    else:
                        compType = int(input('Selecione uma opção: '))
                        if compType not in compTypes:
                            os.system('cls')
                            showCompTypes(branchName)
                            print('> Erro. Selecione uma opção válida!\n')
                            continue

                    # Selecting a computer type
                    # Concentrador
                    if compType == 1:
                        compValues = main(SAMPLE_RANGE_NAME)
                        compValues = cleaningData(compValues)
                        compValues, branchName = showBranch(option, compValues)

                        addValues = main(HARDWARE_RANGE_NAME)
                        addValues = cleaningData(addValues)
                        addValues, addBranchName = showBranch(option, addValues)

                        os.system('cls')
                        header(f'> CONCENTRADOR - {branchName} <\n')
                        displayCompInfoByType(compValues, addValues, customerName, compType)

                        # Menu after showing details
                        showCompByTypeOptions(compType)
                        while computerOption not in computerOptions:
                            computerOption = int(input('Selecione uma opção: '))
                            # Option 9 - back
                            if computerOption == 9:
                                compType = 99
                                control = 999
                                os.system('cls')
                                break
                            # Option 0 - quit
                            elif computerOption == 0:
                                compType = 0
                                control = 9
                                break
                            if computerOption not in computerOptions:
                                os.system('cls')
                                showCompByTypeOptions(compType)
                                print('> Erro. Selecione uma opção válida!\n')
                                continue

                    # Vasilhame
                    elif compType == 2:
                        compValues = main(SAMPLE_RANGE_NAME)
                        compValues = cleaningData(compValues)
                        compValues, addBranchName = showBranch(option, compValues)

                        addValues = main(HARDWARE_RANGE_NAME)
                        addValues = cleaningData(addValues)
                        addValues, branchName = showBranch(option, addValues)

                        os.system('cls')
                        header(f'> VASILHAME - {branchName} <\n')
                        count = displayCompInfoByType(compValues, addValues, customerName, compType)

                        # Menu after showing details
                        showCompByTypeOptions(compType, count)
                        while computerOption not in computerOptions:
                            computerOption = int(input('Selecione uma opção: '))
                            # Option 9 - back
                            if computerOption == 9:
                                compType = 99
                                control = 999
                                os.system('cls')
                                break
                            # Option 0 - branch or home -- depends on the count return
                            elif computerOption == 0:
                                compType = 0
                                if count == 0:
                                    control = 0
                                else:
                                    control = 9
                                break
                            if computerOption not in computerOptions:
                                os.system('cls')
                                showCompByTypeOptions(compType, count)
                                print('> Erro. Selecione uma opção válida!\n')
                                continue

                    # PDV
                    elif compType == 3:
                        while True:

                            if control == 9:
                                break

                            pdv = 404
                            pdvOptions = [9, 0]
                            pdvOption = 404

                            compValues = main(SAMPLE_RANGE_NAME)
                            compValues = cleaningData(compValues)
                            compValues, addBranchName = showBranch(option, compValues)

                            addValues = main(HARDWARE_RANGE_NAME)
                            addValues = cleaningData(addValues)
                            addValues, branchName = showBranch(option, addValues)

                            os.system('cls')
                            pdvs = showPdvs(compValues, branchName)
                            while pdv not in pdvs:
                                print('\n---------------------------\n'
                                      '99.VOLTAR\n'
                                      '0.INÍCIO\n')
                                pdv = int(input('\nSelecione um PDV: '))
                                if pdv == 99:
                                    compType = 99
                                    control = 99
                                    os.system('cls')
                                    break
                                elif pdv == 0:
                                    control = 9
                                    compType = 0
                                    break
                                if pdv not in pdvs:
                                    os.system('cls')
                                    pdvs = showPdvs(compValues, branchName)
                                    print('\n> Erro. Selecione um PDV válido!')

                            if control in [9, 99]:
                                os.system('cls')
                                break

                            pdv = str(pdv)
                            os.system('cls')
                            header(f'> PONTO DE VENDA - {branchName} <\n')
                            displayCompInfoByType(compValues, addValues, customerName, compType, pdv)

                            # Menu after showing details
                            showCompByTypeOptions(compType)
                            while pdvOption not in pdvOptions:
                                pdvOption = int(input('Selecione uma opção: '))
                                # Option 9 - back
                                if pdvOption == 9:
                                    control = 999
                                    os.system('cls')
                                    break
                                # Option 0 - home
                                elif pdvOption == 0:
                                    control = 9
                                    compType = 0
                                    break
                                if pdvOption not in pdvOptions:
                                    os.system('cls')
                                    header(f'> PONTO DE VENDA - {branchName} <\n')
                                    displayCompInfoByType(compValues, addValues, customerName, compType, pdv)
                                    showCompByTypeOptions(compType)
                                    print('> Erro. Selecione uma opção válida!\n')
                                    continue

                if compType == 9:
                    if computerOption == 9:
                        control = 999
                    if control == 99:
                        control = 999
                    option = 0
                    continue
                elif compType == 0:
                    control = 9
                    break
