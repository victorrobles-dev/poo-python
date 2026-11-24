# declaração de classe
class Gafanhoto:
    def __init__(self): # <- método construtor
        # atributos de instância
        self.nome = ""
        self.idade = 0

        
    # métodos de instância
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return f"{self.nome} É gafanhoto(a) e tem {self.idade} anos de idade!"
    
# declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 24
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Victor"
g2.idade = 26
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = "João"
g3.idade = 20
g3.aniversario()
print(g3.mensagem())
