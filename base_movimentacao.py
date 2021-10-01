import os


class Conferir_Movimentacao:
    def __init__(self, competencia):
        self.competencia = competencia

        self.diretorio_nfe = r"T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\NF-e"
        self.diretorio_nfce = r"T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\NFC-e"

    def conferencia_nfe(self):
        lista_empresas = os.listdir(self.diretorio_nfe)
        for empresa in lista_empresas:
            print(empresa)
            lista_arquivos = os.listdir(fr"{self.diretorio_nfe}\{empresa}\{self.competencia}")

            if len(lista_arquivos) == 0:
                print("EMPRESA NAO POSSUI MOVIMENTACAO")

            else:
                if lista_arquivos[0].find('.xml') >= 0 or lista_arquivos[0].find('.pdf') >= 0:
                    print("EMPRESA TEM MOVIMENTACAO")


conf = Conferir_Movimentacao('092021')
conf.conferencia_nfe()
