import os

diretorio = r"C:\Users\matheus.oliveira\Desktop\NF-e"
competencia = "072021"
empresas = os.listdir(diretorio)

"""lista_test = []

for empresa in empresas:

    diretorio_empresa = fr"{diretorio}\{empresa}\{competencia}"

    if len(os.listdir(diretorio_empresa)) > 0:
        print(empresa)
        xmls = os.listdir(diretorio_empresa)
        for xml in xmls:
            if xml.find(".xml") >= 0:

                lista_test.append(xml)

                if len(lista_test) == 100:
                    print(len(lista_test))
                    print(lista_test)
                    print("ADICIONAR ESSA LISTA NO FSIST...")
                    print("BAIXANDO O ARQUIVO PDF")
                    print("MOVENDO O ARQUIVO E EXTRAINDO")

                    lista_test = []
                    print(lista_test)

        print(len(lista_test))
        print(lista_test)
"""

test_diretorio = r"C:\Users\matheus.oliveira\Desktop\NF-e\695-COPA PRODUTOS DE LIMPEZA\072021"
arquivo = "_JUNTO.pdf"

os.rename(fr"{test_diretorio}\{arquivo}", fr"{test_diretorio}\_JUNTO_83.pdf")