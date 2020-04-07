from func import *


while True:
    temPastaBackup()
    try:
        lista = open('listaNomes.txt', 'r')
    except FileNotFoundError:
        lista = open('listaNomes.txt', 'x')
    finally:
        lista.close()
    op = menu()
    if op == 1:
        registrarPessoa()
    if op == 2:
        mostrarLista()
    if op == 3:
        procurarPessoa()
    if op == 4:
        excluirPessoa()
    if op == 5:
        excluirLista()
    if op == 6:
        fazerBackup()
    if op == 7:
        carregarBackup()
    if op == 8:
        apagarBackup()
    if op == 9:
        print('Finalizando o Programa!')
        exit()