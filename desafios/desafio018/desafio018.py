# 
from rich import print
from rich.panel import Panel

class Churrasco:
    # atributos de classe
    consumo_padrao:float = 0.400
    preço_kg:float = 82.40

    def __init__(self, titulo, quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.quantidade} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.quantidade * self.__class__.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preço_kg

    def calcular_custo_pessoa(self) -> float:
        return self.calcular_custo_total() / self.quantidade
    
    def analisar(self):
        conteudo = f"Analisando o [blue]{self.titulo}[/] com [cyan]{self.quantidade}[/] convidados."
        conteudo += f"\nCada participante comerá {self.__class__.consumo_padrao}KG e cada KG custa R${self.__class__.preço_kg:,.2f}."
        conteudo += f"\nRecomendo comprar [purple]{self.calcular_qtd_carne():.2f}KG[/] de carne."
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():.2f}[/]."
        conteudo += f"\nCada convidade vai pagar [green]R${self.calcular_custo_pessoa()}[/] para participar."
        painel = Panel(conteudo, title=self.titulo, expand=False)
        print(painel)

# declaração de objetos
c1 = Churrasco("Churrasco Dia 12", 8)
print(c1.analisar())

c2 = Churrasco("Churras de Ano Novo", 20)
print(c2.analisar())
