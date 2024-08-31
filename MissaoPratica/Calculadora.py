#--------------------------------------------------
# Nome do Programa: Calculadora.py
# Descricao: Classe Calculadora
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

class Calculadora:
    def __init__(self, valorA, valorB, operacao): 
        self.__valorA = valorA
        self.__valorB = valorB
        self.operacao = operacao

    #getters e setters
    @property
    def valorA(self):
        return self.__valorA
    
    @valorA.setter
    def valorA(self, valor):
        self.__valorA=valor

    #getters e setters
    @property
    def valorB(self):
        return self.__valorB
    
    @valorB.setter
    def valorB(self, valor):
        self.__valorB=valor

    def validarOperacao(self):
        return self.operacao in ['+', '-', '*', '/']

    def calcular(self):
        if not self.validarOperacao():
            print("Operacao matematica Invalida!")
            exit(1)

        if self.operacao == '+':
            return self.__valorA + self.__valorB
        elif self.operacao == '-':
            return self.__valorA - self.__valorB
        elif self.operacao == '*':
            return self.__valorA * self.__valorB
        elif self.operacao == '/':
            if self.__valorB == 0:
                print("Nao e permitida a Divisao por zero, troque o numero")
                exit(1)
            else:
                return self.__valorA / self.__valorB
        
    def mostarResultado(self):
        print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))
        
    @staticmethod
    def entradaDados():
        valorA = float(input('Digite o primeiro numero: '))
        valorB = float(input('Digite o segundo numero: '))
        operacao = input('Digite a operacao (+, -, *, /):')
        return Calculadora(valorA, valorB, operacao)
    
