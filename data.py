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


def getCompData(infoRow):
    (infoName,
     infoIP,
     infoEconectVersion,
     infoClisitefVersion,
     infoJarReason) = infoRow
    return (infoName,
            infoIP,
            infoEconectVersion,
            infoClisitefVersion,
            infoJarReason)


def getEconectData(infoRow):
    (infoName,
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
     InfoBDCleanAnalist) = infoRow
    return (infoName,
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
            InfoBDCleanAnalist)


def getHardwareCompData(infoRow):
    (infoName,
     infoIP,
     infoProcessor,
     infoMemory,
     infoStorage,
     infoOperationalSystem,
     infoMaintenance,
     infoMaintenanceDate,
     infoMaintenanceResponsible,
     infoSerialNumber) = infoRow
    return (infoName,
            infoIP,
            infoProcessor,
            infoMemory,
            infoStorage,
            infoOperationalSystem,
            infoMaintenance,
            infoMaintenanceDate,
            infoMaintenanceResponsible,
            infoSerialNumber)
