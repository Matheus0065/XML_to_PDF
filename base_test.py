from selenium import webdriver
import time
import os


class XML_TO_PDF:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.fsist.com.br/converter-xml-nfe-para-danfe"

        self.arquivo_xml = r'T:\DEPARTAMENTOS\AUTOMAÇÃO\XML\NF-e\43-DOSSEL AMBIENTAL - CONSULTORIA E ' \
                           r'PROJETOS\072021'

        self.arquivos = '"53210710538220000127550010000015581963165903.xml""53210710538220000127550010000015571027827345.xml"'

    def navigate(self):
        self.driver.get(self.url)

    def selecionar_xml(self):
        self.driver.find_element_by_id("arquivo").send_keys(fr"{self.arquivo_xml}\{self.arquivos}")
        self.driver.find_element_by_class_name("butenviar").click()
        self.driver.find_element_by_id("msgsim").click()

        time.sleep(1)
        self.driver.find_element_by_id("butlinktexto").click()


xml = XML_TO_PDF()
xml.navigate()
xml.selecionar_xml()