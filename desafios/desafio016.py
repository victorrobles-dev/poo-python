# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    def apresentar(self):
        print(f"Olá :grin:, me chamo [green]{self.nome}[/], sou do setor de [cyan]{self.setor}[/] e nele atuo como [yellow]{self.cargo}[/].")

# declaração de objetos
f1 = Funcionario("Victor", "TI", "AI Engineer")
f1.apresentar()

f2 = Funcionario("Maria", "Jurídico", "Advogada")
f2.apresentar()
