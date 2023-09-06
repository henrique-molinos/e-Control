def cleaningData(values):
    for i, row in enumerate(values):
        if not row:  # [] -- Pops empty rows
            values.pop(i)
        for register in row:
            if register == 'Descrição' or 'verificação' in register:  # Pops the headers and BD verification row
                values.pop(i)
                break
            else:
                continue

    return values


def getCompData(infoRow, customerName):
    if customerName.lower() == 'beltrame':
        (infoName,
         infoIP,
         infoCurrentVersion,
         infoOldVersion,
         infoUpdateDate,
         infoClisitefVersion,
         infoJarDate,
         infoVPNDate,
         infoBDSize,
         infoBDCleanDate,
         infoMaintenanceDate) = infoRow
        infoRouteDate = 'N/A'
        return (infoName,
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
                infoMaintenanceDate)

    elif customerName.lower() == 'bom preço':
        (infoName,
         infoIP,
         infoCurrentVersion,
         infoOldVersion,
         infoUpdateDate,
         infoClisitefVersion,
         infoJarDate,
         infoRouteDate,
         infoBDSize,
         infoBDCleanDate,
         infoMaintenanceDate) = infoRow
        infoVPNDate = 'N/A'
        return (infoName,
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
                infoMaintenanceDate)

    elif customerName.lower() == 'lima':
        (infoName,
         infoIP,
         infoCurrentVersion,
         infoOldVersion,
         infoUpdateDate,
         infoClisitefVersion,
         infoJarDate,
         infoBDSize,
         infoBDCleanDate,
         infoMaintenanceDate) = infoRow
        infoVPNDate = 'N/A'
        infoRouteDate = 'N/A'
        return (infoName,
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
                infoMaintenanceDate)

    elif customerName.lower() == 'pazini':
        (infoName,
         infoIP,
         infoCurrentVersion,
         infoOldVersion,
         infoUpdateDate,
         infoClisitefVersion,
         infoJarDate,
         infoRouteDate,
         infoBDSize,
         infoBDCleanDate,
         infoMaintenanceDate) = infoRow
        infoVPNDate = 'N/A'
        return (infoName,
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
                infoMaintenanceDate)

    elif customerName.lower() == 'único':
        (infoName,
         infoIP,
         infoCurrentVersion,
         infoOldVersion,
         infoUpdateDate,
         infoClisitefVersion,
         infoJarDate,
         infoBDSize,
         infoBDCleanDate,
         infoMaintenanceDate) = infoRow
        infoVPNDate = 'N/A'
        infoRouteDate = 'N/A'
        return (infoName,
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
                infoMaintenanceDate)

    else:
        print('getPCData(); Erro no recebimento dos dados do cliente.')


def getAddCompData(infoRow):
    (infoName,
     infoIP,
     infoProcessor,
     infoMemory,
     infoStorage,
     infoOperationalSystem) = infoRow
    return (infoName,
            infoIP,
            infoProcessor,
            infoMemory,
            infoStorage,
            infoOperationalSystem)
