# Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.
from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preço=0):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        etq = Panel(f"{self.nome}\nR${self.preço:,.2f}", title="Etiqueta", style="cyan", width=50)
        print(etq)

p1 = Produto("Iphone 18 Pro Max", 10_000)
p2 = Produto("Moto Royal Enfield Hunter 350", 20_900)

p1.etiqueta()
p2.etiqueta()
