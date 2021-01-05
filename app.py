# -*- encoding: utf-8 -*-
from Service.PontoAutomagico import PontoAutomagico
import schedule, time, os

#Credenciais MdComune
MD_LOGIN = os.getenv('MD_LOGIN')
MD_PASSWORD = os.getenv('MD_PASSWORD')

pontoMdComune = PontoAutomagico()

#marcar ponto
pontoMdComune.marcar_ponto(MD_LOGIN, MD_PASSWORD)
