from polimofirmo.model.formas_geometricas.forma import Forma
import math

class Circulo(Forma):

    def __init__(self,raio):
        self.raio = raio

    def area(self):
        return math.pi  * self.raio ** 2

    def perimetro(self):
        return 2 ** math.pi  * self.raio

    """
        Descrição do circulo
    """
    def descricao(self):
        print('Descrição do circulo')