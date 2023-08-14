from projeto import Projeto


class Funcionario():

    # Método construtor
    def __init__(self, rga, nome, funcao, story_p, senha, mybd):
        self.nome = nome
        self.rga = rga
        self.story_p = story_p
        self.funcao = funcao
        self.senha = senha
        self.projeto = [Projeto(i[0],i[1],i[2],i[3],i[4],mybd) for i in mybd.trazerProjetos(rga)] if mybd.trazerProjetos(rga) else []




    # Método para exibir informações do funcionário
    def __str__(self):
        return f"Nome: {self.nome}, RGA: {self.rga}, Story Points: {self.story_p}, Projetos: {len(self.projeto)}"
    def get_rga(self):
        return self.rga

    def get_nome(self):
        return self.nome

    def get_story_p(self):
        return self.story_p

    def get_funcao(self):
        return self.funcao

    def get_senha(self):
        return self.senha

    def get_projs(self):
        return self.projeto
    def get_projetos(self):
        projt = f"Numero de Projetos: {len(self.projeto)}\n"

        for i in self.projeto:
            projt += f'{i}' + '\n'
        return projt
    # sets
    def upadate(self,Mybd,valor,newvalor):
        try:
            Mybd.update('funcionario',valor,newvalor,'RGA',self.rga)
            return 1
        except Exception as e:
            return 0

    def set_story_p(self,Mybd,story_p):
        self.upadate(Mybd,'story_p',story_p)
        self.story_p = story_p

    def set_funcao(self,mybd,func):
        self.upadate(mybd,'funcao',func)
        self.funcao = func

    def add_projeto(self,mydb,codproj):
        try:
            nproj = mydb.selct('projeto','idprojeto',codproj)

            if nproj:
                sql = f"""INSERT INTO trabalha_em VALUES ({self.rga},{codproj}); """
                mydb.curse.execute(sql)
                mydb.con.commit()
                self.projeto.append(nproj)
        except:
            ...
    def remove_projeto(self,mydb,codproj):
        try:
            sql = f"""delete from trabalha_em where funcionario_rga = {self.rga} and projeto_idprojeto = {codproj}; """
            mydb.curse.execute(sql)
            mydb.con.commit()
            for i in self.projeto:
                if i.get_cod() == codproj:
                    self.projeto.remove(i)
                    break
        except:
            ...



