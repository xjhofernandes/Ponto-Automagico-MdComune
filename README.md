# Ponto-Automagico-MdComune
Automatizador de pontos para o site MdComune. 

Variaveis globais:
* MD_LOGIN = Seu login MdComune (geralmente é o e-mail corporativo)
* MD_PASSWORD = Sua senha MdComune
* EMAIL_SENDER = E-mail google que será responsável pelo o envio dos avisos de ponto.
* EMAIL_PASSWORD = Senha do e-mail google que enviará e-mails.
* EMAIL_RECEIVER = E-mail que receberá os avisos de pontos. 
* WEBDRIVER_PATH = Caminho que ficará o seu binário do webdriver.

É necessário ativar a configuração aplicativos menos seguros do Google para o envio de e-mails. 

![Image](https://devanswers.co/wp-content/uploads/2017/02/gmail-allow-less-secure-apps.png)

URL: https://myaccount.google.com/lesssecureapps


Instalar modulos:
pip install -r requirements.txt 

Webdrivers Chrome:
https://chromedriver.chromium.org/downloads
