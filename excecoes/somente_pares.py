class SomentePares(list):

    def append(self,inteiro):
        if not isinstance(inteiro,int):
            raise TypeError('Somente Inteiros')
        if inteiro % 2:
            raise ValueError('Somente Pares')

        super().append(inteiro)
        