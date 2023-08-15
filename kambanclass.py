import mysql.connector


class KambamBD:

    def __init__(self):
        # Depois de conectar na nuvem ele estará funcional
        self.con = mysql.connector.connect(
            host='localhost',
            database='gerencia_de_projetos',
            user='root',
            password='12347'
        )
        # Verifica se conectou
        if self.con.is_connected():
            print("CONECTED")
        # Deixa um cursor sempre setado
        self.curse = self.con.cursor()

    def adicionar(self, table, *args):
        try:
            sql = f"INSERT INTO {table} VALUES {tuple(args)};"
            self.curse.execute(sql)
            self.con.commit()
        except Exception as e:
            print("ERRO ERRO!! não entrou.", e)

    def delete(self, tabel, valor, expcfic):
        try:
            sql = f"""DELETE FROM {tabel} WHERE {valor} = {expcfic if str != type(expcfic) else f"'{expcfic}'"}; """
            self.curse.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)

    def select(self,table,id,idref):
        try:
            sql = f"SELECT * FROM {table} WHERE {id} = {idref};"
            self.curse.execute(sql)
            self.con.commit()
        except Exception as e:
            print("ERRO ERRO!! não entrou.", e)

    def trazerUsers(self):
        try:
            self.curse.execute(f"SELECT * FROM funcionario;")
            linhas = self.curse.fetchall()
            return linhas
        except:
            return 0

    def trazerProjetos(self,id):
        try:
            self.curse.execute(f"select distinct p.* from projeto as p,  trabalha_em as t, funcionario as f where t.funcionario_RGA = {id} and t.projeto_idprojeto = p.idprojeto;")
            linhas = self.curse.fetchall()
            return linhas
        except:
            return 0

    def trazerTarefas(self,codproj):
        try:
            self.curse.execute(f"""
            select
              t.idtarefa,t.nome,t.desc,t.prazo,t.time,e.nome
            from
              tarefa as t,
              etapa as e
            where
              t.idproj= {codproj} and t.etapa_cod_e = e.cod_e;
            """)
            linhas = self.curse.fetchall()
            return linhas
        except:
            return 0
        
    def trazerStatus(self,codproj):
        try:
            self.curse.execute(f"""
            select
              t.idtarefa,t.nome,t.desc,t.prazo,t.time,e.nome
            from
              tarefa as t,
              etapa as e
            where
              t.idproj= {codproj} and t.etapa_cod_e = e.cod_e;
            """)
            linhas = self.curse.fetchall()
            return linhas
        except:
            return 0


    def trazerFuncionariodeProjeto(self,codproj):
        try:
            self.curse.execute(f"""
                select distinct
                          f.rga,f.nome
                from
                          funcionario as f,
                          trabalha_em as t
                where
                         t.projeto_idprojeto = {codproj};
                """)
            linha = self.curse.fetchall()
            return linha
        except:
            return 0

    def update(self, tabel, valor, newvalor, key1, parametro):
        try:
            sql = f"""UPDATE {tabel} SET {valor} = {newvalor if str != type(newvalor) else f"'{newvalor}'"} WHERE {key1} = {parametro}; """
            self.curse.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)

    def __del__(self):
        self.curse.fetchall()
        self.curse.close()  # Desconecta o curso do dataBase
        self.con.close()  # Desconecta do DataBase
        print("Desconected")
