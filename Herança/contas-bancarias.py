class conta:
    def saque(self):

    def deposito(self):

class contaCorrente(conta):
    def saque(self):
        #o exercício não especifica nada para esse método de conta corrente, o que colocar aqui?

    def deposito(self):
        #o exercício não especifica nada para esse método de conta corrente, o que colocar aqui?

class contaPoupanca(conta):
    def __init__(self, saldoPoupanca):
        self.__saldoPoupanca = saldoPoupanca
        #uma conta poupanca n pode ficar com saldo negativo

    def saque(self, saldoPoupanca):
        taxaSaque = 2.0
        if (saque > saldoPoupanca):
            print('Outro valor do saque: ')
        else:
            saldoPoupanca = saldoPoupanca - taxaSaque

    def deposito(self):
        #o exercício não especifica nada para esse método de conta poupança, o que colocar aqui?

    def rende(self, saldoPoupanca):
        taxaRendimento = 0.095
        saldoPoupanca = saldoPoupanca + saldoPoupanca*taxaRendimento

class main():
    saque = print('Valor do saque: ')
