from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.total_paginas} páginas[/] no total. Atualmente você está na página [yellow]{self.pagina_atual}[/]")


    def avançar_paginas(self, qtd):
        cont = 0 
        for pagina in range(0, qtd, 1):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f"Página. {self.pagina_atual} :arrow_forward:", end=' ')
                cont += 1
                sleep(0.5)
        print(f"[yellow]Você agora está na página [cyan]{self.pagina_atual}[/]")
        if self.fim_livro():
            print(f":closed_book:[red] Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

# declaração de objetos
l1 = Livro("Harry Potter", 350)
l1.avançar_paginas(20)
