class Livro:

    def __init__(self, titulo : str , lancamento : str , autor : str):
        self.titulo= titulo
        self.lancamento = lancamento
        self.autor = autor

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self , titulo):
        self.titulo = titulo

    @property
    def lancamento(self):
        return self.lancamento

    @lancamento.setter
    def lancamento(self,lancamento):
        self.lancamento = lancamento

    @property
    def autor(self):
        return self.autor

    @autor.setter
    def autor(self , autor):
        self.autor = autor