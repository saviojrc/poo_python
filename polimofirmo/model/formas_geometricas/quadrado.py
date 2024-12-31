from polimofirmo.model.formas_geometricas.forma import Forma

class Quadrado(Forma):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4