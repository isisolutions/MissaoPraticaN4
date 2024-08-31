#--------------------------------------------------
# Nome do Programa: Pessoa.py
# Descricao: Criacao de Classe Pessoa - Adquirir conhecimento de orientacao objetos
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

class Pessoa:
    def __init__(self, nome, dataNascimento, cpf, rg):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.rg = rg
        self.status = False

    def alterarStatus(self, status):
        self.status = status
    

        