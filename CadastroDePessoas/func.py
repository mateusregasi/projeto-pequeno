from os import listdir, remove, mkdir


def mostrarLinha():
    print('=' * 60)
def titulo(msg):
    mostrarLinha()
    print(f'{msg:^60}')
    mostrarLinha()
def menu():
    titulo('Menu de Opções')
    print('1 - Registrar pessoa.\n'
          '2 - Mostrar lista.\n'
          '3 - Procurar pessoa.\n'
          '4 - Excluir pessoa.\n'
          '5 - Excluir lista.\n'
          '6 - Fazer Backup.\n'
          '7 - Carregar Backup.\n'
          '8 - Apagar Backup.\n'
          '9 - Sair')
    mostrarLinha()
    while True:
        try:
            op = int(input('>> Sua escolha: ').strip())
        except:
            print('Opção inválida!, digite novamente!')
        else:
            if op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op != 7 and op != 8 and op != 9:
                print('Opção inválida!, digite novamente!')
            else:
                break
    return op
def numeroDeLinhas():
    cont = 0
    lista = open('listaNomes.txt', 'r')
    for linha in lista:
        cont += 1
    lista.close()
    return cont
def registrarPessoa():
    titulo('Registro de Pessoa')
    pessoa = {}
    pessoa['codigo'] = numeroDeLinhas()
    while True:
        pessoa['nome'] = input('Nome: ').strip().title()
        if pessoa['nome'].isnumeric() == False:
            break
        else:
            print('Nome digitado inválido! Tente novamente!')
    while True:
        try:
            pessoa['idade'] = f'{int(input("Idade: ").strip())} anos'
        except:
            print('Idade inválida! Digite novamente!')
        else:
            break
    while True:
        pessoa['sexo'] = input("Sexo[M/F]: ").strip()[0].upper()
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('Sexo inválido! Digite novamente!')
        else:
            break
    pessoa = '{:>3} {:<40} {:>7} sexo {}\n'.format(pessoa['codigo'], pessoa['nome'], pessoa['idade'], pessoa['sexo'])
    lista = open('listaNomes.txt', 'a')
    lista.write(pessoa)
    lista.close()
def mostrarLista():
    if numeroDeLinhas() == 0:
        print('A lista não possue nenhum conteúdo!')
    else:
        titulo('Lista de Nomes')
        lista = open('listaNomes.txt', 'r')
        for linha in lista:
            print(linha, end='')
        lista.close()
def procurarPessoa():
    while True:
        nome = input('Digite um nome: ').strip().title()
        if nome.isnumeric() == True:
            print('O nome digitado é inválido!')
        else:
            break
    lista = open('listaNomes.txt', 'r')
    for linha in lista:
        if nome in linha[4:41]:
            print(linha)
    lista.close()
def excluirLista():
    while True:
        try:
            certeza = input('Tem certeza que quer excluir a lista?[S se quiser]: ').strip().upper()[0]
        except:
            certeza = ''
        else:
            if certeza == 'S':
                lista = open('listaNomes.txt', 'w')
                lista.write('')
                lista.close()
            break
def formatarLista():
    cont = 0
    lista = open('listaNomes.txt', 'r')
    listaBackup = lista.readlines()
    quant = len(listaBackup)
    for c in range(0, quant):
        listaBackup[c].replace(listaBackup[c][0:3], f'{c:>3}')
    lista.close()
    lista = open('listaNomes.txt', 'w')
    for c2 in listaBackup:
        lista.writelines(c2)
    lista.close()
def excluirPessoa():
    while True:
        try:
            cod = '{:>3}'.format(input('Código da pessoa que deseja excluir: ').strip())
        except:
            print('Código inváido! Digite novamente!')
        else:
            break
    lista = open('listaNomes.txt', 'r')
    listaBackup = lista.readlines()
    listaExcluir = []
    for linha in listaBackup:
        if linha[0:3] == cod:
            listaExcluir.append(linha)
    lista.close()
    for c1 in listaBackup:
        for c2 in listaExcluir:
            if c1 == c2:
                listaBackup.remove(c2)
    if listaExcluir == []:
        print('O código não existe!')
    else:
        lista = open('listaNomes.txt', 'w')
        for p in listaBackup:
            lista.writelines(p)
        lista.close()
    formatarLista()
def fazerBackup():
    while True:
        nome = input('Escolha um nome para o backup: ').strip().lower()
        if nome == 'sair' or nome.isalpha() == True:
            break
        else:
            print('Nome inválido! Digite novamente!')
    if nome != 'sair':
        try:
            teste = open(f'Backup\{nome}.txt', 'r')
        except:
            quer = 'S'
            backup = open(f'Backup\{nome}.txt', 'x')
            backup.close()
        else:
            while True:
                quer = input(f'Já possui um arquivo chamado {nome}.txt. Deseja salvar por cima?[S/N] ').strip().upper()[0]
                if quer == 'S' or quer == 'N':
                    break
                else:
                    print('Escolha inválida!')
                teste.close()
        finally:
            if quer == 'S':
                listaParaBackup = ''
                lista = open('listaNomes.txt', 'r')
                listaParaBackup = lista.read()
                lista.close()
                backup = open(f'Backup\{nome}.txt', 'w')
                backup.write(listaParaBackup)
                backup.close()
def mostrarBackups():
    titulo('Backups')
    listaBackup = listdir('C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup')
    if listaBackup == []:
        print('Não existe nenhum backup disponível!')
        return False
    else:
        for backup in listaBackup:
            print(f'>> {backup}')
        return True
def carregarBackup():
    tembackup = mostrarBackups()
    if tembackup == True:
        backupApagar = f'{input("Digite o backup que deseja carregar: ").strip()}.txt'
        listaBackup = listdir('C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup')
        if backupApagar not in listaBackup:
            print('O backup solicitado não existe!')
        else:
            listaApagar = open(f'Backup\{backupApagar}', 'r')
            paraLista = listaApagar.readlines()
            listaApagar.close()
            lista = open('listaNomes.txt', 'w')
            lista.writelines(paraLista)
            lista.close()
            remove(f'C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup\{backupApagar}')
def apagarBackup():
    tembackup = mostrarBackups()
    if tembackup == True:
        backupApagar = f'{input("Digite o backup que deseja apagar: ").strip()}.txt'
        listaBackup = listdir('C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup')
        if backupApagar not in listaBackup:
            print('O backup solicitado não existe!')
        else:
            remove(f'C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup\{backupApagar}')
def temPastaBackup():
    listaDePastas = listdir('C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo')
    if 'Backup' not in listaDePastas:
        mkdir('C:\\Users\mateu\PycharmProjects\ProjetinhoBrabo\Backup')