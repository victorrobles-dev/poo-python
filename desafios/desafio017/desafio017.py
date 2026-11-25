# Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.
from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preço=0):
        # atributos de instância
        self.nome = nome
        self.preço = preço

    def __str__(self):
        return f"{self.nome} custa R${self.preço:,.2f}"    

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        preçof = f"R${self.preço:,.2f}"
        conteudo += f"{preçof.center(30, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=34, style="cyan")
        print(etiqueta)

p1 = Produto("Iphone 18 Pro Max", 10_000)
p2 = Produto("Moto Royal Enfield Hunter 350", 20_900)

p1.etiqueta()
p2.etiqueta()
