class Data:
    
    def __init__(self,dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)

    @classmethod
    def de_string(cls,data_string):
        dia,mes,ano = map(int,data_string.split('-'))
        return cls(dia=dia,mes=mes,ano=ano)


    @staticmethod
    def is_data_valid(data_string : str):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia<=31 and mes <=12 and ano <= 3999
