# Conta bancária
class ContaBancaria:
    """
    Cria uma conta bancária para fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")
        
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem um saldo de R$\033[32m{self.saldo:,.2f}\033[0m"
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de \033[32mR${valor:,.2f}\033[0m autorizado na conta \033[36m{self.id}\033[0m")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo atual da conta é de R${self.saldo:,.2f}, não foi possível realizar o saque solicitado no valor de R${valor}.")
        else:
            self.saldo -= valor
            print(f"Saque de \033[32mR${valor:,.2f}\033[0m autorizado na conta \033[36m{self.id}\033[0m")

# declaração do objeto
conta1 = ContaBancaria(112, "Victor", 3300)
conta1.depositar(500)
conta1.sacar(2_000_000)
print(conta1)
        