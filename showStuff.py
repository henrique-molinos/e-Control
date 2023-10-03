from data import *
import os


def header(screen):
    word = 'e-Control'
    print('X' * (len(word) * 5 + 2))
    print('X' * (len(word) * 2) + ' ' + word + ' ' + 'X' * (len(word) * 2))
    print('X' * (len(word) * 5 + 2))
    print('\n' + screen)


def showCustomers():
    header('> SELEÇÃO DE CLIENTES <\n')
    print('CLIENTES\n'
          '1.Beltrame\n'
          '2.Bom Preço\n'
          '3.Lima\n'
          '4.Pazini\n'
          '5.Único\n'
          '-----------\n'
          '0.SAIR\n')


def showBranches(customer):
    header(f'> SELEÇÃO DE LOJA - {customer} <\n')
    if customer.lower() == 'beltrame':
        print('LOJAS DISPONÍVEIS\n'
              '1.Euclides da Cunha (Matriz)\n'
              '2.Parque Pinheiro\n'
              '3.Hélvio Basso\n'
              '4.Venâncio Aires\n'
              '5.Camobi\n'
              '----------------------------\n'
              '9.VOLTAR\n'
              '0.SAIR\n')

    elif customer.lower() == 'bom preço':
        print('LOJAS DISPONÍVEIS\n'
              '1.São Pedro do Sul\n'
              '------------------\n'
              '9.VOLTAR\n'
              '0.SAIR\n')

    elif customer.lower() == 'lima':
        print('LOJAS DISPONÍVEIS\n'
              '1.Cacequi (Matriz)\n'
              '2.São Vicente do Sul\n'
              '3.São Francisco de Assis\n'
              '------------------------\n'
              '9.VOLTAR\n'
              '0.SAIR\n')

    elif customer.lower() == 'pazini':
        print('LOJAS DISPONÍVEIS\n'
              '1.Borges (Matriz)\n'
              '2.Av. Farroupilha (Filial)\n'
              '--------------------------\n'
              '9.VOLTAR\n'
              '0.SAIR\n')

    elif customer.lower() == 'único':
        print('LOJAS DISPONÍVEIS\n'
              '1.Candelária\n'
              '2.Ernesto Alves\n'
              '3.Av. Brasil\n'
              '---------------\n'
              '9.VOLTAR\n'
              '0.SAIR\n')


def showBranch(option, values):
    for i, row in enumerate(values):
        if option == 9:
            break

        if 'Loja' in row[0]:
            branchName = row[0]
            values.pop(i)
            return values, branchName

    return values


def showCompOptions():
    print('-----------------------\n'
          '1.DETALHES\n'
          '9.VOLTAR\n'
          '0.INÍCIO\n')


def showCompTypes(branchName):
    header(f'> TIPO DE COMPUTADOR - {branchName} <\n')
    print('1.Concentrador\n'
          '2.Vasilhame\n'
          '3.Pdv\n'
          '-----------------------\n'
          '9.VOLTAR\n'
          '0.INÍCIO\n')


def showCompData(infoName,
                 infoIP,
                 infoEconectVersion,
                 infoClisitefVersion,
                 infoJarReason,
                 infoSerialNumber):
    print(infoName, '\n  '
                    'IP:', infoIP, '\n  '
                    'Versão Atual:', infoEconectVersion, '\n  '                                                      
                    'Versão CliSiTEF:', infoClisitefVersion, '\n  '                          
                    'Motivo Jar:', infoJarReason, '\n  '
                    'N/S:', infoSerialNumber)


def showEconectData(infoName,
                    infoCurrentVersion,
                    infoOldVersion,
                    infoUpdateDate,
                    infoUpdateAnalist,
                    infoClisitefVersion,
                    infoJarReason,
                    infoJarTicket,
                    infoJarDate,
                    infoBDSize,
                    infoBDCleanDate,
                    infoBDCleanAnalist):
    print(infoName, '\n')
    print('> VERSIONAMENTO <\n'
          '  Versão Atual:', infoCurrentVersion, '\n  '
          'Versão Anterior:', infoOldVersion, '\n  '
          'Data Atualização:', infoUpdateDate, '\n  '
          'Atualizado por:', infoUpdateAnalist, '\n  ')

    print('> ARQUIVOS DE CORREÇÃO <\n'
          '  Motivo Jar:', infoJarReason, '\n  '
          'Ticket Jar:', infoJarTicket, '\n  '
          'Data Inst. Jar:', infoJarDate, '\n  ')

    print('> CLISITEF <\n'
          '  Versão CliSiTEF:', infoClisitefVersion, '\n  ')

    print('> BANCO DE DADOS <\n'
          '  Tamanho BD:', infoBDSize, '\n  '
          'Data Limpeza BD:', infoBDCleanDate, '\n  '
          'Analista Limp.:', infoBDCleanAnalist)


def showHardwareCompData(infoProcessor,
                         infoMemory,
                         infoStorage,
                         infoOperationalSystem,
                         infoMaintenanceDescription,
                         infoMaintenanceDate,
                         infoMaintenanceResponsible,
                         infoSerialNumber):
    print('\n > HARDWARE <')
    print('  Processador:', infoProcessor, '\n  '
          'Memória:', infoMemory, '\n  '
          'Armazenamento:', infoStorage, '\n  '
          'Sistema Operacional:', infoOperationalSystem, '\n  '
          'Manutenção:', infoMaintenanceDescription, '\n  '
          'Data Manutenção:', infoMaintenanceDate, '\n  '
          'Responsável Manutenção:', infoMaintenanceResponsible, '\n  '                                         
          'N/S:', infoSerialNumber)


def displayCompInfo(finalValues):
    for i, row in enumerate(finalValues):
        (name,
         ip,
         econectVersion,
         clisitefVersion,
         jarReason,
         serialNumber) = getCompData(row)

        print('---------------------------')
        showCompData(infoName=name,
                     infoIP=ip,
                     infoEconectVersion=econectVersion,
                     infoClisitefVersion=clisitefVersion,
                     infoJarReason=jarReason,
                     infoSerialNumber=serialNumber)


def showPdvs(pdValues, branchName):
    pdvList = []
    ipList = []
    header(f'> PDVs - {branchName} <\n')
    for pdvRow in pdValues:
        if 'pdv' in pdvRow[0].lower():
            pdvList.append(int((pdvRow[0])[4:6]))
            ipList.append(pdvRow[1])

    print(f'Os PDVs disponíveis são:\n')

    for i, pdv in enumerate(pdvList):
        if ipList[i] == '-':
            print(pdv, '-', 'N/A')
        else:
            print(pdv, '-', ipList[i])

    return pdvList


def displayCompInfoByType(compValues, econectValues, compHardwareValues, compType, *pdv):
    count = 0
    control = 0
    strCompType = ''

    if compType == 1:
        strCompType = 'CONCENTRADOR'
    elif compType == 2:
        strCompType = 'VASILHAME'
    elif compType == 3:
        strCompType = 'PDV'

    for i, row in enumerate(compValues):
        if compType == 1:  # Type = Concentrador
            if 'concentrador' in row[0].lower():
                count += 1

                econectRow = econectValues[i]
                (name_econect,
                 currentVersion,
                 oldVersion,
                 updateDate,
                 updateAnalist,
                 clisitefVersion_econect,
                 jarReason_econect,
                 jarTicket,
                 jarInstDate,
                 dbSize,
                 dbCleanDate,
                 dbCleanAnalist) = getEconectData(econectRow)

                compHardwareRow = compHardwareValues[i]
                (name_hardware,
                 ip_hardware,
                 processor,
                 memory,
                 storage,
                 operationalSystem,
                 maintenanceDescription,
                 maintenanceDate,
                 maintenanceResp,
                 serialNumber) = getHardwareCompData(compHardwareRow)

                print('---------------------------')

                showEconectData(name_econect,
                                currentVersion,
                                oldVersion,
                                updateDate,
                                updateAnalist,
                                clisitefVersion_econect,
                                jarReason_econect,
                                jarTicket,
                                jarInstDate,
                                dbSize,
                                dbCleanDate,
                                dbCleanAnalist)

                showHardwareCompData(infoProcessor=processor,
                                     infoMemory=memory,
                                     infoStorage=storage,
                                     infoOperationalSystem=operationalSystem,
                                     infoMaintenanceDescription=maintenanceDescription,
                                     infoMaintenanceDate=maintenanceDate,
                                     infoMaintenanceResponsible=maintenanceResp,
                                     infoSerialNumber=serialNumber)

        elif compType == 2:  # Type = Vasilhame:
            if 'vasilhame' in row[0].lower():
                count += 1
                econectRow = econectValues[i]
                (name_econect,
                 currentVersion,
                 oldVersion,
                 updateDate,
                 updateAnalist,
                 clisitefVersion_econect,
                 jarReason_econect,
                 jarTicket,
                 jarInstDate,
                 dbSize,
                 dbCleanDate,
                 dbCleanAnalist) = getEconectData(econectRow)

                compHardwareRow = compHardwareValues[i]
                (name_hardware,
                 ip_hardware,
                 processor,
                 memory,
                 storage,
                 operationalSystem,
                 maintenanceDescription,
                 maintenanceDate,
                 maintenanceResp,
                 serialNumber) = getHardwareCompData(compHardwareRow)

                print('---------------------------')
                showEconectData(name_econect,
                                currentVersion,
                                oldVersion,
                                updateDate,
                                updateAnalist,
                                clisitefVersion_econect,
                                jarReason_econect,
                                jarTicket,
                                jarInstDate,
                                dbSize,
                                dbCleanDate,
                                dbCleanAnalist)

                showHardwareCompData(infoProcessor=processor,
                                     infoMemory=memory,
                                     infoStorage=storage,
                                     infoOperationalSystem=operationalSystem,
                                     infoMaintenanceDescription=maintenanceDescription,
                                     infoMaintenanceDate=maintenanceDate,
                                     infoMaintenanceResponsible=maintenanceResp,
                                     infoSerialNumber=serialNumber)

        elif compType == 3:  # Type = PDV:
            ip_hardware = ''

            if control == 0:
                pdv = pdv[0]
            if control == 0 and len(pdv) == 1:
                pdv = '0'+pdv

            if f'pdv {pdv}' in row[0].lower():
                count += 1
                econectRow = econectValues[i]
                (name_econect,
                 currentVersion,
                 oldVersion,
                 updateDate,
                 updateAnalist,
                 clisitefVersion_econect,
                 jarReason_econect,
                 jarTicket,
                 jarInstDate,
                 dbSize,
                 dbCleanDate,
                 dbCleanAnalist) = getEconectData(econectRow)

                compHardwareRow = compHardwareValues[i]
                (name_hardware,
                 ip_hardware,
                 processor,
                 memory,
                 storage,
                 operationalSystem,
                 maintenanceDescription,
                 maintenanceDate,
                 maintenanceResp,
                 serialNumber) = getHardwareCompData(compHardwareRow)

                print('---------------------------')
                showEconectData(name_econect,
                                currentVersion,
                                oldVersion,
                                updateDate,
                                updateAnalist,
                                clisitefVersion_econect,
                                jarReason_econect,
                                jarTicket,
                                jarInstDate,
                                dbSize,
                                dbCleanDate,
                                dbCleanAnalist)

                showHardwareCompData(infoProcessor=processor,
                                     infoMemory=memory,
                                     infoStorage=storage,
                                     infoOperationalSystem=operationalSystem,
                                     infoMaintenanceDescription=maintenanceDescription,
                                     infoMaintenanceDate=maintenanceDate,
                                     infoMaintenanceResponsible=maintenanceResp,
                                     infoSerialNumber=serialNumber)
            control += 1
            if count != 0:
                return ip_hardware

        else:
            print('FALHA CATASTRÓFICA!\nO tipo de computador selecionado não existe.')

    if count == 0:
        print(f'ERRO:\nNão existe registro de {strCompType} para a loja selecionada.')

    return count


def showCompByTypeOptions(compType, *countTuple):
    if compType == 2:
        count = countTuple[0]
        if count == 0:
            print('\n-----------------------\n'
                  '9.VOLTAR\n'
                  '0.SELEÇÃO DE LOJA\n')
        else:
            print('\n-----------------------\n'
                  '9.VOLTAR\n'
                  '0.INÍCIO\n')
    else:
        print('\n-----------------------\n'
              '1.EXECUTAR SSH\n'
              '9.VOLTAR\n'
              '0.INÍCIO\n')


def displaySshOptions(computerName, branchName):
    commandControl = 0

    while True:
        if commandControl == 999:
            os.system('cls')

        header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
        print('TIPOS DE COMANDOS:\n')

        commandTypes = [1, 2, 9]
        commandType = 404

        while commandType not in commandTypes:
            print('1.COMANDOS DE CONSULTA\n'
                  '2.COMANDOS DE EXECUÇÃO\n'
                  '------------------------------------------------\n'
                  '9.VOLTAR\n')
            commandType = int(input('Selecione uma opção: '))

            if commandType not in commandTypes:
                os.system('cls')
                print('> Erro. Informe um código de tipo de comando válido!\n')
                continue

        queryCommandOptions = [1, 2, 3, 4, 9]
        executionCommandOptions = [1, 2, 9]
        commandOption = 404
        commandControl = 404

        # If commandType is QUERY
        os.system('cls')
        if commandType == 1:
            while commandOption not in queryCommandOptions:
                # Tests if user entered an invalid option (line 68 condition)
                if commandControl == 99:
                    os.system('cls')
                    header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
                    print('COMANDOS DE CONSULTA:\n'
                          '1.Verificar memória livre -> free -h\n'
                          '2.Verificar dispositivos USB conectados -> lsusb\n'
                          '3.Verificar hardware -- SO / Procesador / Memória / Armazenamento\n'
                          '4.Verificar conteúdo estrutura.sh e parametros.sh\n'
                          '------------------------------------------------------\n'
                          '9.VOLTAR\n')
                    print('> Erro. Informe um código de comando válido!\n')
                    commandOption = int(input('Selecione uma opção: '))
                    if commandOption == 9:
                        commandControl = 999
                        break
                else:
                    os.system('cls')
                    header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
                    print('COMANDOS DE CONSULTA:\n'
                          '1.Verificar memória livre -> free -h\n'
                          '2.Verificar dispositivos USB conectados -> lsusb\n'
                          '3.Verificar hardware -- SO / Procesador / Memória / Armazenamento\n'
                          '4.Verificar conteúdo estrutura.sh e parametros.sh\n'
                          '-----------------------------------------------\n'
                          '9.VOLTAR\n')
                    commandOption = int(input('Selecione uma opção: '))
                    if commandOption == 9:
                        commandControl = 999
                        break
                    if commandOption not in queryCommandOptions:
                        commandControl = 99
                        continue

        # If commandType is EXECUTION
        elif commandType == 2:
            while commandOption not in executionCommandOptions:
                # Tests if user entered an invalid option (line 68 condition)
                if commandControl == 99:
                    os.system('cls')
                    header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
                    print('COMANDOS DE EXECUÇÃO:\n'
                          '1.Desconectar sessões ativas via VNC\n'
                          '2.Corrigir arquivos de monitor (estrutura.sh & parametros.sh)\n'
                          '------------------------------------------------------\n'
                          '9.VOLTAR\n')
                    print('> Erro. Informe um código de comando válido!\n')
                    commandOption = int(input('Selecione uma opção: '))
                    if commandOption == 9:
                        commandControl = 999
                        break
                else:
                    os.system('cls')
                    header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
                    print('COMANDOS DE EXECUÇÃO:\n'
                          '1.Desconectar sessões ativas via VNC\n'
                          '2.Corrigir arquivos de monitor (estrutura.sh & parametros.sh)\n'
                          '------------------------------------------------------\n'
                          '9.VOLTAR\n')
                    commandOption = int(input('Selecione uma opção: '))
                    if commandOption == 9:
                        commandControl = 999
                        break
                    if commandOption not in executionCommandOptions:
                        commandControl = 99
                        continue
        elif commandType == 99:
            return commandType, commandOption

        if commandControl == 999:
            continue

        return commandType, commandOption


def showAfterSshOptions():
    print('OPÇÕES:')
    print('1.EXECUTAR OUTRO COMANDO\n'
          '9.VOLTAR\n'
          '0.SAIR\n')
