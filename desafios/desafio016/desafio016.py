# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    # atributos de classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # atributos de instância
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    def apresentar(self) -> str:
        return f"Olá :grin:, me chamo [green]{self.nome}[/], sou do setor de [cyan]{self.setor}[/] e nele atuo como [yellow]{self.cargo}[/] na empresa {self.__class__.empresa}."

# declaração de objetos
f1 = Funcionario("Victor", "TI", "AI Engineer")
print(f1.apresentar())
# inspect(f1, methods=True)

f2 = Funcionario("Maria", "Jurídico", "Advogada")
print(f2.apresentar())
# inspect(Funcionario)
