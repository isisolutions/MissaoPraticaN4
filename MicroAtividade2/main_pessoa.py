#--------------------------------------------------
# Nome do Programa: main_pessoa.py
# Descricao: Descrever a instanciacao e utilizacao de objetos em Python
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

from Pessoa import Pessoa

#instancia da classe Pessoa
pessoa_ins = Pessoa("Joao", "2000-01-01", "000.111.222-33", "15975388-1")

attrs = vars(pessoa_ins)

print("Instancia da classe Pessoa: ")
print(', '.join("%s: %s" % item for item in attrs.items()))