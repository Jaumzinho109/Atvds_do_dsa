#Crie uma classe chamada "ContaBancaria" que represente uma conta bancária básica. A classe deve ter os
#  atributos: titular da conta (nome), número da conta e saldo.
#  Ela deve ter métodos para depositar dinheiro, sacar dinheiro e exibir o saldo atual.

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo_atual = saldo

    def depositar(self):
        deposito = float(input('Quantos você irá depositar? '))
        self.saldo_atual += deposito

    def sacar(self):
        saque = float(input('Quantos reais você irá sacar? '))
        self.saldo_atual -= saque

    def exibir_saldo(self):
        print(f'O saldo da conta do titular {self.titular}, número de conta: {self.numero_conta} é igual a {self.saldo_atual}')

teste = ContaBancaria('João', '07060658165', 50000)
teste.depositar()
teste.exibir_saldo()
