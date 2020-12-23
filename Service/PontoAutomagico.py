from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import os

WEBDRIVER_PATH = os.getenv('WEBDRIVER_PATH')

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--disable-gpu')
option.add_argument('--log-level=3') 
browser = webdriver.Chrome(WEBDRIVER_PATH, options=option)

class PontoAutomagico(object):
    def marcar_ponto(self, loginMd, senha):
        print('Acessando MdComune')
        browser.get('https://www.mdcomune.com.br')

        print('Colocando User/password')
        login = browser.find_element_by_name('LogOnModel.UserName')
        password = browser.find_element_by_name('LogOnModel.Password')
        button = browser.find_element_by_xpath('/html/body/nav/div/div[2]/form/button')

        login.send_keys(loginMd)
        password.send_keys(senha)

        button.click()
        print('Logando...')

        print('acessando tela de marcação')
        button = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[10]/span')
        button.click()

        botaoSalvar = browser.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[2]/div[3]/div[1]/input")
        botaoSalvar.click()
        print('Ponto realizado com sucesso!! :) ')
