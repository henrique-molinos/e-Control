from data import *


def header(screen=''):
    word = 'e-Control'
    print('X' * (len(word) * 3 + 2))
    print('X' * len(word) + ' ' + word + ' ' + 'X' * len(word))
    print('X' * (len(word) * 3 + 2))
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


def showCompTypes(branchName):
    header(f'> TIPO DE COMPUTADOR - {branchName} <\n')

    print('C.Concentrador\n'
          'V.Vasilhame (Se houver)\n'
          'P.Pdv\n'
          '-----------------------\n'
          '9.VOLTAR\n'
          '0.SAIR\n')


def showConcOptions(branchName):
    header(f'> CONCENTRADOR - {branchName} <\n')

    print('1.Editar\n'
          '-----------------------\n'
          '9.VOLTAR\n'
          '0.SAIR\n')


def showCompData(infoName,
                 infoIP,
                 infoCurrentVersion,
                 infoOldVersion,
                 infoUpdateDate,
                 infoClisitefVersion,
                 infoJarDate,
                 infoVPNDate,
                 infoRouteDate,
                 infoBDSize,
                 infoBDCleanDate,
                 infoMaintenanceDate):
    print(infoName, '\n  '
                    'IP:', infoIP, '\n  '
                    'Versão Atual:', infoCurrentVersion, '\n  '
                    'Versão Antiga:', infoOldVersion, '\n  '
                    'Data Atualização:', infoUpdateDate, '\n  '
                    'Versão CliSiTEF:', infoClisitefVersion, '\n  '
                    'Data Inst. jar:', infoJarDate, '\n  '
                    'Data Inst. VPN:', infoVPNDate, '\n  '
                    'Data Conf. Rota:', infoRouteDate, '\n  '
                    'Tamanho BD:', infoBDSize, '\n  '
                    'Data Limp. BD:', infoBDCleanDate, '\n  '
                    'Data Últ. Manutenção:', infoMaintenanceDate)


def displayCompInfo(finalValues, customerName):
    for i, row in enumerate(finalValues):
        if i < (len(finalValues)):
            (name,
             ip,
             currentVersion,
             oldVersion,
             updateDate,
             clisitefVersion,
             jarDate,
             vpnDate,
             routeDate,
             bdSize,
             bdCleanDate,
             maintenanceDate) = getCompData(row, customerName)

            print('---------------------------')
            showCompData(infoName=name,
                         infoIP=ip,
                         infoCurrentVersion=currentVersion,
                         infoOldVersion=oldVersion,
                         infoUpdateDate=updateDate,
                         infoClisitefVersion=clisitefVersion,
                         infoJarDate=jarDate,
                         infoVPNDate=vpnDate,
                         infoRouteDate=routeDate,
                         infoBDSize=bdSize,
                         infoBDCleanDate=bdCleanDate,
                         infoMaintenanceDate=maintenanceDate)
