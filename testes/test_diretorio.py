import os

diretorio = r"T:\DEPARTAMENTOS\AUTOMAÇÃO\XML\NF-e"
competencia = "072021"
empresas = os.listdir(diretorio)

for empresa in empresas:

    diretorio_empresa = fr"{diretorio}\{empresa}\{competencia}"

    if len(os.listdir(diretorio_empresa)) > 0:
        print(empresa)
        xmls = os.listdir(diretorio_empresa)
        for xml in xmls:
            if xml.find(".xml") >= 0:
                print(xml)