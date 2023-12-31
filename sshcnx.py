import json
from paramiko import SSHClient, AutoAddPolicy
import time
import os
from showStuff import header


def getComputerCredentials(customer, branch, ip, credentialsFile):
    with open(credentialsFile) as cf:
        credentialsFile = json.load(cf)
    for cred in credentialsFile:
        if (customer.lower() in cred['customer']) and (branch == cred['branch']) and (ip == cred['host']):
            return cred['host'], cred['user'], cred['passwd'], cred['name'], cred


def SSH_Connection(SSH_HOST, SSH_PORT, SSH_USER, SSH_PASSWD,
                   commandType, commandOption,
                   branch, computerName, branchName):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(SSH_HOST,
                       SSH_PORT,
                       SSH_USER,
                       SSH_PASSWD)
        client.invoke_shell()
        os.system('cls')
        header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
        print('Conexão realizada com sucesso!\n')

        commands = []
        titles = []

        if commandType == 1:
            if commandOption == 1:
                commands = [
                    'free -h'
                ]
                titles = [
                    '>> MEMÓRIA LIVRE <<'
                ]
            elif commandOption == 2:
                commands = [
                    'lsusb'
                ]
                titles = [
                    '>> DISPOSITIVOS CONECTADOS <<'
                ]
            elif commandOption == 3:
                commands = [
                    'cat /etc/os-release',
                    'cat /proc/cpuinfo',
                    'dmidecode -t memory',
                    'parted -l',
                ]
                titles = [
                    '>> SISTEMA OPERACIONAL <<',
                    '>> INFORMAÇÕES DO PROCESSADOR <<',
                    '>> INFORMAÇÕES DA MEMÓRIA RAM <<',
                    '>> INFORMAÇÕES DO ARMAZENAMENTO <<'
                ]
            elif commandOption == 4:
                commands = [
                    'cat /etc/conf.d/estrutura.sh',
                    'cat /etc/conf.d/parametros.sh'
                ]
                titles = [
                    '>> ESTRUTURA.SH <<',
                    '>> PARAMETROS.SH <<'
                ]
            elif commandOption == 5:
                commands = [
                    'echo -n | telnet 127.0.0.1 4096'
                ]
                titles = [
                    '>> VERIFICAÇÃO DE COMUNICAÇÃO VPN GSURF <<'
                ]
            elif commandOption == 6:
                schema = ''
                if 'concentrador' in str(computerName).lower():
                    schema = 'concentrador'
                elif 'pdv' in str(computerName).lower():
                    schema = 'pdv'
                commands = [
                    f'echo \'SELECT table_schema "{schema}", ROUND(SUM(data_length + index_length)'
                    f' / 1024 / 1024, 1) "Size (MB)" '
                    f'FROM information_schema.tables '
                    f'WHERE table_schema = "{schema}"\' | mysql -ueconect -p123456 {schema} -t'
                ]
                titles = [
                    '>> VERIFICAÇÃO DO TAMANHO DO BD <<'
                ]
            else:
                print('Opção inválida')

        elif commandType == 2:
            if commandOption == 1:
                commands = [
                    'x11vnc -R disconnect:all'
                ]
                titles = [
                    '>> DESCONEXÃO DE DISPOSITIVOS ATIVOS VIA VNC <<'
                ]
            elif commandOption == 2:
                commands = [
                    'killall java'
                ]
                titles = [
                    '>> FINALIZAR PROCESSOS DO JAVA <<'
                ]
            elif commandOption == 3:
                commands = [
                    'cp -f -v /usr/socin/econect/ftp/suporte/display/etc-conf.d/* /etc/conf.d/',
                    'cp -f -v /usr/socin/econect/ftp/suporte/display/usr-bin/* /usr/bin'
                ]
                titles = [
                    '>> ATUALIZAÇÃO DE ARQUIVOS DE DISPLAY /ETC/CONF.D/ <<',
                    '>> ATUALIZAÇÃO DO ARQUIVO /USR/BIN/MONITOR <<'
                ]
            elif commandOption == 4:
                commands = [
                    '/sbin/reboot -f > /dev/null 2>&1 &'
                ]
                titles = [
                    '>> REINÍCIO DO COMPUTADOR <<'
                ]
            else:
                print('Opção inválida!')

        logOptions = ['s', 'n']
        logOption = ''

        while logOption not in logOptions:
            logOption = input('Deseja gerar arquivo de log? (S/N): ').lower()
            if logOption not in logOptions:
                os.system('cls')
                header(f'> CONEXÃO SSH - {computerName} - {branchName} <\n')
                print('Conexão realizada com sucesso!\n')
                continue

        if logOption == 's':
            with open(f'log\\log-L{branch}-{computerName.replace(" ", "")}\
-{time.strftime("%d%m%Y_%H-%M-%S", time.localtime())}.txt', 'w') as outFile:
                # For every command in commands[] execute command, get output, get errors (if exists)
                for i, command in enumerate(commands):
                    stdin, stdout, stderr = client.exec_command(command)
                    output = stdout.readlines()
                    executionErrors = stderr.readlines()
                    # In the case there's no error stored in stderr (normal situation)
                    if not executionErrors:
                        # Check if there's titles
                        if titles[i]:
                            print('\n' + titles[i])
                            outFile.write(titles[i] + '\n')
                        else:
                            pass

                        for line in output:
                            print(line.strip())
                            outFile.write(line)
                        if not output:
                            continue
                        else:
                            print('\n')
                            outFile.write('\n')
                    # In the case there's any error stored in stderr (command return)
                    else:
                        if titles[i]:
                            print(titles[i])
                            outFile.write(titles[i] + '\n')
                        else:
                            pass

                        for line in output:
                            print(line.strip())
                            outFile.write(line)
                        if not output:
                            continue
                        else:
                            print('\n')
                            outFile.write('\n')

                        print('[!] ERRO')
                        outFile.write('[!] ERRO\n')
                        for errorLine in executionErrors:
                            print(errorLine)
                            outFile.write(f'{time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())} - ')
                            outFile.write(errorLine)

        elif logOption == 'n':
            for i, command in enumerate(commands):
                stdin, stdout, stderr = client.exec_command(command)
                output = stdout.readlines()
                executionErrors = stderr.readlines()
                if not executionErrors:
                    if titles[i]:
                        print('\n' + titles[i])
                    else:
                        pass

                    for line in output:
                        print(line.strip())
                    if not output:
                        continue
                    else:
                        print('\n')

                else:
                    if titles[i]:
                        print(titles[i])
                    else:
                        pass

                    for line in output:
                        print(line.strip())
                    if not output:
                        continue
                    else:
                        print('\n')

                    print('[!] ERRO')
                    for errorLine in executionErrors:
                        print(errorLine)

        client.close()
        print('> E-CONTROL: Conexão fechada após executar os comandos!\n')

    except Exception as excep:
        print(f'Falha ao estabelecer conexão! Erro: {str(excep)}\n')

    finally:
        client.close()


def multipleSSHConnection(commandOption):
    commands = []
    titles = []

    with open('computers.json') as fh:
        credentials = json.load(fh)

    for cred in credentials:
        try:
            if commandOption == 1:
                commands = [
                    'free -h'
                ]
                titles = [
                    '>> MEMÓRIA LIVRE <<'
                ]
            elif commandOption == 2:
                commands = [
                    'lsusb'
                ]
                titles = [
                    '>> DISPOSITIVOS CONECTADOS <<'
                ]
            elif commandOption == 3:
                commands = [
                    'cat /etc/os-release',
                    'cat /proc/cpuinfo',
                    'dmidecode -t memory',
                    'parted -l',
                ]
                titles = [
                    '>> SISTEMA OPERACIONAL <<',
                    '>> INFORMAÇÕES DO PROCESSADOR <<',
                    '>> INFORMAÇÕES DA MEMÓRIA RAM <<',
                    '>> INFORMAÇÕES DO ARMAZENAMENTO <<'
                ]
            elif commandOption == 4:
                commands = [
                    'cat /etc/conf.d/estrutura.sh',
                    'cat /etc/conf.d/parametros.sh'
                ]
                titles = [
                    '>> ESTRUTURA.SH <<',
                    '>> PARAMETROS.SH <<'
                ]
            elif commandOption == 5:
                commands = [
                    'echo -n | telnet 127.0.0.1 4096'
                ]
                titles = [
                    '>> VERIFICAÇÃO DE COMUNICAÇÃO VPN GSURF <<'
                ]
            elif commandOption == 6:
                schema = ''
                if 'concentrador' in str(cred['name']).lower():
                    schema = 'concentrador'
                elif 'pdv' in str(cred['name']).lower():
                    schema = 'pdv'
                commands = [
                    f'echo \'SELECT table_schema "{schema}", ROUND(SUM(data_length + index_length)'
                    f' / 1024 / 1024, 1) "Size (MB)" '
                    f'FROM information_schema.tables '
                    f'WHERE table_schema = "{schema}"\' | mysql -ueconect -p123456 {schema} -t'
                ]
                titles = [
                    '>> VERIFICAÇÃO DO TAMANHO DO BD <<'
                ]
            else:
                print('Opção inválida')

            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(cred['host'], 22, cred['user'], cred['passwd'])

            for i, command in enumerate(commands):
                with open('log\\logcmd-' + str(cred['customer']) + 'L' + str(cred['branch']) + '-' +
                          str(cred['name']).replace(" ", "") + '-' +
                          time.strftime("%d%m%Y_%H-%M-%S", time.localtime()) + '.txt', 'w') as outFile:
                    stdin, stdout, stderr = ssh.exec_command(command)
                    output = stdout.readlines()
                    executionErrors = stderr.readlines()
                    # In the case there's no error stored in stderr (normal situation)
                    if not executionErrors:
                        # Check if there's titles
                        if titles[i]:
                            print('\n' + titles[i])
                            outFile.write(titles[i] + '\n')
                        else:
                            pass

                        for line in output:
                            print(line.strip())
                            outFile.write(line)
                        if not output:
                            continue
                        else:
                            print('\n')
                            outFile.write('\n')
                    # In the case there's any error stored in stderr (command return)
                    else:
                        if titles[i]:
                            print(titles[i])
                            outFile.write(titles[i] + '\n')
                        else:
                            pass

                        for line in output:
                            print(line.strip())
                            outFile.write(line)
                        if not output:
                            continue
                        else:
                            outFile.write('\n')

                        print('[!] ERRO')
                        outFile.write('[!] ERRO\n')
                        for errorLine in executionErrors:
                            print(errorLine)
                            outFile.write(f'{time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())} - ')
                            outFile.write(errorLine)

                ssh.close()

                print('Comando executado no ' + str(cred['name']) + ' - ' + 'Loja ' + str(cred['branch']) + '!\n')

        except Exception as excep:
            print(f'Falha ao estabelecer conexão! Erro: {str(excep)}\n')
