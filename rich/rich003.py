from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")
tabela.add_column("Produto:")
tabela.add_column("Preço:")
tabela.add_row("Ovos","12,90")
tabela.add_row("Leite", "5,90")

print(tabela)