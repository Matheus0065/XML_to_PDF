from selenium import webdriver
import time
import os
import shutil
from zipfile import ZipFile


class XML_TO_PDF:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.fsist.com.br/converter-xml-nfe-para-danfe"

        self.diretorio = r'C:\Users\matheus.oliveira\Desktop\NF-e'
        self.competencia = "072021"

        self.download = r"C:\Users\matheus.oliveira\Downloads"

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

                        self.driver.find_element_by_id("arquivo").send_keys(fr"{diretorio_empresa}\{_xml}")

                self.driver.find_element_by_class_name("butenviar").click()
                self.driver.find_element_by_id("msgsim").click()

                time.sleep(10)
                try:
                    self.driver.find_element_by_id("butlinktexto").click()

                except:
                    time.sleep(30)
                    self.driver.find_element_by_id("butlinktexto").click()

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
                                self.driver.find_element_by_id("arquivo").\
                                    send_keys(fr"{diretorio_empresa}\{arquivo_xml}")

                            self.driver.find_element_by_class_name("butenviar").click()
                            self.driver.find_element_by_id("msgsim").click()

                            time.sleep(10)
                            try:
                                self.driver.find_element_by_id("butlinktexto").click()

                            except:
                                time.sleep(30)
                                self.driver.find_element_by_id("butlinktexto").click()

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
                    self.driver.find_element_by_id("arquivo"). \
                        send_keys(fr"{diretorio_empresa}\{arquivo_xml}")

                self.driver.find_element_by_class_name("butenviar").click()
                self.driver.find_element_by_id("msgsim").click()

                time.sleep(10)
                try:
                    self.driver.find_element_by_id("butlinktexto").click()

                except:
                    time.sleep(30)
                    self.driver.find_element_by_id("butlinktexto").click()

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
        print(50*'-')
        print("\tPROCESSO FINALIZADO ... ENCERRANDO")
        print(50*'-')
        self.driver.close()


xml = XML_TO_PDF()
xml.navigate()
xml.selecionar_xml()
xml.finalizando_processo()
