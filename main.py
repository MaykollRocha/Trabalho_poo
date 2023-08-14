# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kambanclass import KambamBD
from funcionarioclass import Funcionario
from projeto import Projeto


def area_func(eufunc):
    print(eufunc)
    print(eufunc.get_projetos())
    while True:
        match int(input('1- adicinar\n 2.tirar\n')):
            case 1:
                eufunc.add_projeto(mybd,11)
            case 2:
                eufunc.remove_projeto(mybd,11)
            case 0:break




def login(funcinarios):
    cod = int(input("Codigo: "))
    senha = input("Senha: ")
    for i in funcinarios:
        if cod == i.get_rga() and senha == i.get_senha():
            area_func(i)
            return
    print("Erro")
    return

# abre o banco de dados onde tem as informaçoes dos funcinairos
mybd = KambamBD()
funcs = mybd.trazerUsers()


funclist = []
for i in funcs:
    funclist.append(Funcionario(i[0], i[1], i[2], i[3], i[4],mybd))
    print(i[4])

for i in funclist:
    print(i)

login(funclist)

del mybd
