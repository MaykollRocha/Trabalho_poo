
class QuadroKanban :
    def __init__(self):
        self.__projetos = []
        self.__status = []

    def __str__(self):
        texto = ""
        if (self.__projetos):
            texto += "Projetos: "
            for proj in self.__projetos:
                texto += proj.nome + "\n"

        if (self.__status):
            texto += "Status: "
            for status in self.__status:
                texto += status + " "

        return texto

    def add_projeto(self, projeto):
        self.__projetos.append(projeto)

    def remove_projeto(self, projeto):
        self.__projetos.remove(projeto)

    def add_status(self, status):
        self.__status.append(status)

    def remove_status(self, status):
        self.__status.remove(status)