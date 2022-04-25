from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil
from zipfile import ZipFile
import getpass
from datetime import date
import datetime


class XML_TO_PDF:
    def __init__(self, competencia):

        # ------ Log Usuario ------ #
        user = getpass.getuser()
        horario = datetime.datetime.now()
        with open(r"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Log_programs\log_sist.txt", 'a') as arquivo:
            arquivo.write(f"XMLtoPDF | Iniciado | {user} | {horario} \n")

        arquivo.close()

        self.driver = webdriver.Chrome()
        self.url = "https://www.fsist.com.br/converter-xml-nfe-para-danfe"

        # FIXME: Alternar entre os caminhos.

        self.diretorio = r'T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\.Saidas\NFC-e\2022'
        # self.diretorio = r'T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\.Saidas\NF-e\2022'
        # self.diretorio = r'T:\CLIENTES\1 - MOVIMENTAÇÃO FISCAL\.XML_agencia_net\.Entradas\NF-e\2022'
        self.competencia = competencia

        user = getpass.getuser()
        self.download = rf"C:\Users\{user}\Downloads"

    def navigate(self):
        self.driver.get(self.url)

    def selecionar_xml(self):
        empresas = os.listdir(self.diretorio)
        for empresa in empresas:
            print(empresa)
            diretorio_empresa = fr"{self.diretorio}\{empresa}\{self.competencia}"

            arquivos_xmls = os.listdir(diretorio_empresa)

            if len(arquivos_xmls) == 0:
                print("SEM MOVIMENTO")
                pass

            elif 0 < len(arquivos_xmls) < 100:
                for _xml in arquivos_xmls:
                    if _xml.find(".xml") >= 0:

                        self.driver.find_element(By.ID, "arquivo").send_keys(fr"{diretorio_empresa}\{_xml}")

                self.driver.find_element(By.CLASS_NAME, "butenviar").click()
                self.driver.find_element(By.ID, "msgsim").click()

                time.sleep(10)
                try:
                    self.driver.find_element(By.ID, "butlinktexto").click()

                except:
                    time.sleep(30)
                    self.driver.find_element(By.ID, "butlinktexto").click()

                time.sleep(5)
                self.driver.refresh()
                # SALVAR O PDF NA PASTA DA EMPRESA
                arquivos_download = os.listdir(self.download)
                print(arquivos_download)
                for arquivo in arquivos_download:
                    if arquivo.find(f"FSist") >= 0:
                        shutil.move(fr"{self.download}\{arquivo}", fr"{diretorio_empresa}")

                        time.sleep(3)
                        z = ZipFile(fr"{diretorio_empresa}\{arquivo}", 'r')
                        z.extractall(fr"{diretorio_empresa}")
                        z.close()

            elif len(arquivos_xmls) > 100:
                lista_xml = []
                idx = 0
                print(f"MOVIMENTAÇÃO MAIOR QUE 100")
                for _xml in arquivos_xmls:
                    if _xml.find(".xml") >= 0:

                        lista_xml.append(_xml)

                        if len(lista_xml) == 100:
                            for arquivo_xml in lista_xml:
                                self.driver.find_element(By.ID, "arquivo").\
                                    send_keys(fr"{diretorio_empresa}\{arquivo_xml}")

                            self.driver.find_element(By.CLASS_NAME, "butenviar").click()
                            self.driver.find_element(By.ID, "msgsim").click()
                            self.driver.implicitly_wait(50)
                            time.sleep(5)
                            try:
                                self.driver.find_element(By.ID, "butlinktexto").click()

                            except:
                                time.sleep(30)
                                self.driver.find_element(By.ID, "butlinktexto").click()

                            time.sleep(5)
                            self.driver.refresh()
                            # SALVAR O PDF NA PASTA DA EMPRESA
                            arquivos_download = os.listdir(self.download)
                            print(arquivos_download)
                            for arquivo in arquivos_download:
                                if arquivo.find(f"FSist") >= 0:
                                    shutil.move(fr"{self.download}\{arquivo}", fr"{diretorio_empresa}")

                                    time.sleep(3)
                                    z = ZipFile(fr"{diretorio_empresa}\{arquivo}", 'r')
                                    z.extractall(fr"{diretorio_empresa}")
                                    z.close()

                                    os.rename(fr"{diretorio_empresa}\_JUNTO.pdf",
                                              fr"{diretorio_empresa}\_JUNTO_{len(lista_xml)}({idx}).pdf")

                            lista_xml = []
                            idx += 1

                for arquivo_xml in lista_xml:
                    self.driver.find_element(By.ID, "arquivo"). \
                        send_keys(fr"{diretorio_empresa}\{arquivo_xml}")

                self.driver.find_element(By.CLASS_NAME, "butenviar").click()
                self.driver.find_element(By.ID, "msgsim").click()

                time.sleep(10)
                try:
                    self.driver.find_element(By.ID, "butlinktexto").click()

                except:
                    time.sleep(30)
                    self.driver.find_element(By.ID, "butlinktexto").click()

                time.sleep(5)
                self.driver.refresh()
                # SALVAR O PDF NA PASTA DA EMPRESA
                arquivos_download = os.listdir(self.download)
                print(arquivos_download)
                for arquivo in arquivos_download:
                    if arquivo.find(f"FSist") >= 0:
                        shutil.move(fr"{self.download}\{arquivo}", fr"{diretorio_empresa}")

                        time.sleep(3)
                        z = ZipFile(fr"{diretorio_empresa}\{arquivo}", 'r')
                        z.extractall(fr"{diretorio_empresa}")
                        z.close()

    def finalizando_processo(self):

        # ------ Log Usuario ------ #
        user = getpass.getuser()
        horario = datetime.datetime.now()
        with open(r"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Log_programs\log_sist.txt", 'a') as arquivo:
            arquivo.write(f"XMLtoPDF | Finalizado | {user} | {horario} \n")

        arquivo.close()

        print(50*'-')
        print("\tPROCESSO FINALIZADO ... ENCERRANDO")
        print(50*'-')
        self.driver.close()


if __name__ == '__main__':
    # DEFINIR O PERIODO DE CONSULTA DAS NOTAS
    # MES_ATUAL = date.today().month - 1
    MES_ATUAL = date.today().month
    ANO_ATUAL = date.today().year
    first_day = date(ANO_ATUAL, MES_ATUAL, 1)
    comp = first_day.strftime('%m%Y')
    print(comp)

    xml = XML_TO_PDF(comp)
    xml.navigate()
    xml.selecionar_xml()
    xml.finalizando_processo()
