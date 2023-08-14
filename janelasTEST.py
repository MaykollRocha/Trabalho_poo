from tkinter import *
from tkinter import ttk
from kambanclass import KambamBD
from Tarafa import Tarefa
mybd = KambamBD()
funcs = mybd.trazerUsers()
tarefas = [Tarefa(i[0],i[1],i[2],i[3],i[4],i[6]) for i in mybd.selct('tarefa')] if mybd.selct('tarefa') else []
del mybd
JanelaSkoll = Tk()
JanelaSkoll.title('JanelaSkoll')
JanelaSkoll.geometry('250x300')
JanelaSkoll.resizable(width=False, height=False)

#inicio da seconde label
w1 = LabelFrame(JanelaSkoll)

mycanvas = Canvas(w1, height=200, width=150)  # Dimensionamento do scroll
mycanvas.pack(side=RIGHT)  # Espaço do Scroll

yscroll = ttk.Scrollbar(w1, orient='vertical',
                        command=mycanvas.yview)  # Orientaçao da Barra
yscroll.pack(side=LEFT, fill='y')  # Orientação do Fit

mycanvas.configure(yscrollcommand=yscroll.set)  # Configurações do Scroll

mycanvas.bind('<Configure>', lambda e: mycanvas.config(
    scrollregion=mycanvas.bbox('all')))  # Função que tornar um fit móvel

JanelaSkoll_space = Frame(mycanvas)  # Barra do scroll
# Onde vai ficar a barra de scroll
mycanvas.create_window((0, 0), window=JanelaSkoll_space, anchor='n')

w1.place(x=0)  # Dimensão que ele fica

for i in tarefas:
    Button(JanelaSkoll_space, text=f'Tarefa: {i.get_nome()}\nStatus: {i.get_status()}', width=20, height=3,
           bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,).pack()


JanelaSkoll.mainloop()