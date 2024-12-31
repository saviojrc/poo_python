import unittest
from excecoes.transacao_invalida import TransacaoInvalida

class MyTestCase(unittest.TestCase):
    def test_something(self):


        try:
            raise TransacaoInvalida(10,20)
        except TransacaoInvalida as e:
            print('Você não tem saldo suficiente : , falta R${}.'.format(e.excesso()))




if __name__ == '__main__':
    unittest.main()
