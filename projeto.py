from Tarafa import Tarefa
from datetime import date

class Projeto():
    def __init__(self, cod, nome, desc, data_ini, data_fim, mybd):
        self.cod = cod
        self.nome = nome
        self.desc = desc
        self.data_ini = data_ini
        self.data_fim = data_fim
        self.supervisor = None
        self.funcionarios = mybd.trazerfuncionarideproejeton(cod)
        self.tarefas = [Tarefa(i[0],i[1],i[2],i[3],i[4],i[5]) for i in mybd.trazerTarefas(cod)] if mybd.trazerTarefas(cod) else []

    def __str__(self):

        info = f"ID Projetos: {self.cod}\n"
        info += f"Nome: {self.nome}\n"
        info += f"Descrição: {self.desc}\n"
        info += f"Data de Início: {self.data_ini.strftime('%m/%d/%y')}\n"
        info += f"Data de Fim: {self.data_fim.strftime('%m/%d/%y')}\n"

        if self.supervisor:
            info += f"Supervisor: {self.supervisor.nome}\n"

        if self.funcionarios:
            info += "Funcionários:\n"
            for func in self.funcionarios:
                info += f"  - {func[1]}\n"

        if self.tarefas:
            info += "Tarefas:\n"
            for tarefa in self.tarefas:
                info += f"  - {tarefa}\n"

        return info

    def upadate(self, Mybd, valor, newvalor):
        try:
            Mybd.update('funcionario', valor, newvalor, 'idprojeto', self.cod)
            return 1
        except Exception as e:
            return 0


    def get_cod(self):
        return self.cod

    @property
    def get_nome(self):
        return self.nome

    def set_nome(self, Mybd,nome):
        self.upadate(Mybd,'nome',nome)
        self.nome = nome

    @property
    def get_desc(self):
        return self.desc

    def set_desc(self, Mybd, desc):
        self.upadate(Mybd, 'desc', desc)
        self.desc = desc

    @property
    def get_data_ini(self):
        return self.data_ini

    def set_data_ini(self, Mybd, data_ini):
        self.upadate(Mybd, 'data_ini', data_ini)
        self.data_ini = data_ini

    @property
    def get_data_fim(self):
        return self.data_fim

    def set_data_fim(self, Mybd, data_fim):
        self.data_fim = data_fim

    @property
    def get_supervisor(self):
        return self.supervisor

    def set_supervisor(self, Mybd, supervisor):
        self.supervisor = supervisor

    @property
    def get_funcionarios(self):
        return self.funcionarios

    def add_funcionario(self, Mybd, *funcionario):
        Mybd.adicinar('Funcinario',*funcionario)
        self.funcionarios.append(funcionario)

    def remove_funcionario(self, Mybd, funcionario):
        self.funcionarios.remove(funcionario)

    @property
    def get_tarefas(self):
        return self.tarefas

    def add_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remove_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)