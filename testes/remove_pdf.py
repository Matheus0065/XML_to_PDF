import os

diretorio = r"T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\NF-e"
competencia = "072021"

lista_empresas = os.listdir(diretorio)
for empresa in lista_empresas:
    print(empresa)

    lista_arquivos = os.listdir(fr"{diretorio}\{empresa}\{competencia}")

    if len(lista_arquivos) == 0:
        pass

    else:
        for arquivo in lista_arquivos:
            if arquivo.find("FSist") >= 0:
                print(arquivo)
                os.remove(fr"{diretorio}\{empresa}\{competencia}\{arquivo}")