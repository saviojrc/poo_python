class TratandoExcecoes:

    def tratar_excecao(self):
        try:
            raise ValueError('Este é um argumento')
        except ValueError  as e:
            print('Os argumentos da exceção foram:',e.args)
        finally:
            print('Isso sempre será executado')


    def divisao(self,divisor):
        try:
            if divisor == 13:
                raise ValueError(f"Número não permitido:{divisor}")
            return 10 / divisor
        except ZeroDivisionError:
            return 'Divisão por zero'
        except TypeError:
            return 'Entre com um valor númerico'
        except ValueError:
            print('Não utilize o número 13')
            raise
        finally:
            print('Isso sempre será executado')

