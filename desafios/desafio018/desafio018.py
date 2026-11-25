# 
from rich import print
from rich.panel import Panel

class Churrasco:
    # atributos de classe
    consumo_padrao = 0.400
    preço_kg = 82.40

    def __init__(self, titulo, quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        qtd_carne = self.quantidade * self.consumo_padrao
        custo_pessoa = (qtd_carne * self.preço_kg) / self.quantidade
        custo_total = qtd_carne * self.preço_kg

        return Panel(f"Analisando [green]{self.titulo}[/] com [cyan]{self.quantidade}[/] convidados.\nCada participante comerá {self.consumo_padrao}KG e cada KG custa R${self.preço_kg:.2f}.\nRecomendo comprar [blue]{qtd_carne:.2f}KG[/] de carne.\nO custo total será de [green]R${custo_total:.2f}[/]\nCada participante irá pagar [green]R${custo_pessoa}[/] para participar.", title=f"{self.titulo}", expand=False)

# declaração de objetos
c1 = Churrasco("Churrasco Dia 12", 8)
print(c1.analisar())

c2 = Churrasco("Churras de Ano Novo", 20)
print(c2.analisar())
