#--------------------------------------------------
# Nome do Programa: main_pessoa.py
# Descricao: Descrever a instanciacao e utilizacao de objetos em Python
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

from Pessoa import Pessoa

#instancia da classe Pessoa
pessoa1 = Pessoa(
    nome = "Joao", 
    dataNascimento = "2000-01-01", 
    cpf = "000.111.222-", 
    rg = "15975388-1", 
    status = False
)

attrs = vars(pessoa1)

print("Instancia da classe Pessoa: ")

print(', '.join("%s: %s" % item for item in attrs.items()))

#Atualiza Valores

pessoa1.nome = "Ana"
pessoa1.dataNascimento = "1990-05-15"
pessoa1.cpf = "123.456.789"  # Incorreto CPF
pessoa1.rg = "98765432-1"

attrs = vars(pessoa1)
print(', '.join("%s: %s" % item for item in attrs.items()))
