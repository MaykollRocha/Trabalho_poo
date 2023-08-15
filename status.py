class Status:
    def __init__(self, nome, cod_e):
        self.nome = nome
        self.cod_e = cod_e

    def __str__(self):
        return f'''Código: {self.cod_e}
        Nome: {self.nome}'''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cod_e(){
        return self.cod_e
    }

    def set_cod_e(){
        self.cod_e = cod_e
    }