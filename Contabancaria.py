class ContaBancaria:
    def __init__(self, numero, tipoConta, saldo=0):

        self.__numero = numero
        self.__tipoConta = tipoConta
        self.__saldo = saldo

    def get_numero(self):
        return self.__numero

    def get_tipoConta(self):
        return self.__tipoConta

    def get_saldo(self):
        return self.__saldo

    def set_numero(self, novo_numero):
        self.__numero = novo_numero

    def set_tipoConta(self, novo_tipoConta):
        self.__tipoConta = novo_tipoConta

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def verificarSituacao(self):
        if self.__saldo > 0:
            return f"O saldo da conta {self.__numero} está positivo"
        elif self.__saldo < 0:
            return f"O saldo da conta {self.__numero} está negativo"
        else:
            return f"A conta {self.__numero} não tem saldo"

numero = int(input("Digite o número da conta: "))
tipoConta = input("Digite o tipo da conta: ")
saldo = float(input("Digite o saldo inicial: "))

conta = ContaBancaria(numero, tipoConta, saldo)

novo_saldo = float(input("Digite o novo saldo: "))
conta.set_saldo(novo_saldo)

print(conta.verificarSituacao())

print(f"O saldo atual da conta número {conta.get_numero()} é: {conta.get_saldo()}")

novo_tipoConta = input("Digite o novo tipo de conta: ")
conta.set_tipoConta(novo_tipoConta)

print(f"O novo tipo de conta é: {conta.get_tipoConta()}")