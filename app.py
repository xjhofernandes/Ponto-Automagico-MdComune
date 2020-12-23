# -*- encoding: utf-8 -*-

from Service import EmailSender, PontoAutomagico
import schedule, time, os

MD_LOGIN = os.getenv('MD_LOGIN')
MD_PASSWORD = os.getenv('MD_PASSWORD')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

pontoMdComune = PontoAutomagico.PontoAutomagico()
email = EmailSender.EmailSender(EMAIL_SENDER, EMAIL_PASSWORD)
goodMessage = email.create_email("Ponto realizado com sucesso!!", "O ponto foi realizado com sucesso! Caso seja preciso, verificar Dashboard do MdComune.")
badMessage = email.create_email("ERRO, não foi possível realizar o ponto!", "Houve algum erro interno e não foi possivel realizar o ponto. Stacktrace: ")

def job():
    try:
        pontoMdComune.marcar_ponto(MD_LOGIN, MD_PASSWORD)
        email.send_email(goodMessage, EMAIL_RECEIVER)
    except:
        email.send_email(badMessage, EMAIL_RECEIVER)

schedule.every().day.at("08:49").do(job)
schedule.every().day.at("17:00").do(job)

while True:
    schedule.run_pending()
    print('verificando hora')
    time.sleep(60)