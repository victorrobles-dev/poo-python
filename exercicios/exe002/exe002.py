# declaração de classe
class Gafanhoto:
    """
    Classe que cria um novo Gafanhoto, com nome e idade:
    
    nome: Recebe o nome do Gafanhoto
    idade: Recebe a idade do Gafanhoto
    """
    def __init__(self, nome="vazio", idade=0): # <- método construtor
        # atributos de instância
        self.nome = nome
        self.idade = idade

        
    # métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self): # Dunder Method
        return f"{self.nome} É gafanhoto(a) e tem {self.idade} anos de idade!"
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    
# declaração de objetos
g1 = Gafanhoto("Maria", 24)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())

g2 = Gafanhoto("Victor", 26)
print(g2)
print(g2.__getstate__())
print(g1.__class__)
