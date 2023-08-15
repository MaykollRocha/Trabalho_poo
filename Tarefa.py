
class Tarefa:
    def __init__(self,cod, nome, desc, prazo,time,etapa):
        self.cod = cod
        self.nome = nome
        self.desc = desc
        self.prazo = prazo
        self.equipe = time
        self.status = etapa

    def __str__(self):
        info = f'Codigo: {self.cod}\n'
        info += f"Nome: {self.nome}\n"
        info += f"Descrição: {self.desc}\n"
        info += f"Prazo: {self.prazo}\n"
        info += f"Equipe: {self.equipe}\n"
        info += f"Status: {self.status}\n"

        return info

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome


    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        self.desc = desc

    def get_prazo(self):
        return self.prazo

    def set_prazo(self, prazo):
        self.prazo = prazo

    def get_equipe(self):
        return self.equipe

    def set_equipe(self, equipe):
        self.equipe = equipe

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status