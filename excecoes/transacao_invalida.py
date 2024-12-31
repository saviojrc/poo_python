class TransacaoInvalida(Exception):

    def __init__(self , saldo_atual , quantidade):
        super().__init__('Sua conta não tem R${}'.format(quantidade))
        self.quantidade = quantidade
        self.saldo_atual = saldo_atual

    def excesso(self):
        return self.quantidade - self.saldo_atual



