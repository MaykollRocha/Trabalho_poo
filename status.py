class Status:
    def __init__(self, nome, max_tarefas, cor):
        self.__nome = nome
        self.__max_tarefas = max_tarefas
        self.__cor = cor

    def __str__(self):
        return f'''Nome: {self.__nome}
        Máximo de Tarefas: {self.__max_tarefas}
        Cor: {self.__cor}'''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_max_tarefas(self):
        return self.__max_tarefas

    def set_max_tarefas(self, max_tarefas):
        self.__max_tarefas = max_tarefas

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor