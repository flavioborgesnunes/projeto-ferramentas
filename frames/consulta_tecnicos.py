from tkinter import ttk, Button, Entry, Label, Frame
from modulos.funcoes import excluir, consultar, limpar, mostrar_tudo

BACKGROUND = '#BBBFCA'
arquivoCsv = './arquivos/tecnicos.csv'


def botao_consultaTec(self):
    # print('consulta Tec')
    self.frame_consultaTec = Frame(
        self.root, bd=4, bg=BACKGROUND, highlightbackground='#0D0D0D',
        highlightthickness=0)
    self.frame_consultaTec.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cunsultaTec = Label(self.frame_consultaTec, fg="#16213E",
                                   text="CONSULTA TÉCNICOS",
                                   background='#BBBFCA',
                                   font=("Arial", 14, "bold"))
    self.title_cunsultaTec.place(relx=0.25, rely=0.02)

    self.lb_codigo = Label(self.frame_consultaTec, text='CPF',
                           background='#BBBFCA', foreground='black',
                           font=("Arial", 12, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.16)
    self.codigo_entry = Entry(
        self.frame_consultaTec, highlightbackground='#878787',
        highlightthickness=1)
    self.codigo_entry.place(relx=0.05, rely=0.20,
                            relwidth=0.60, relheight=0.04)

    self.listaTec = ttk.Treeview(self.frame_consultaTec, height=1, columns=(
        'col1', 'col2', 'col3', 'col4', 'col5'))
    self.listaTec.heading('#0', text='')
    self.listaTec.heading('#1', text='CPF')
    self.listaTec.heading('#2', text='Nome')
    self.listaTec.heading('#3', text='Telefone')
    self.listaTec.heading('#4', text='Turno')
    self.listaTec.heading('#5', text='Equipe')

    self.listaTec.column('#0', width=0)
    self.listaTec.column('#1', width=100)
    self.listaTec.column('#2', width=100)
    self.listaTec.column('#3', width=100)
    self.listaTec.column('#4', width=100)
    self.listaTec.column('#5', width=100)

    self.listaTec.place(relx=0.01, rely=0.3, relwidth=0.95, relheight=0.3)

    self.scrollLista = ttk.Scrollbar(
        self.frame_consultaTec, orient='vertical', command=self.listaTec.yview)
    self.listaTec.configure(yscroll=self.scrollLista.set)
    self.scrollLista.place(relx=0.96, rely=0.3, relwidth=0.04, relheight=0.3)

    self.bt_show_all = Button(
        self.frame_consultaTec, text='Mostrar Tudo', bg='#F2F2F2',
        command=lambda: mostrar_tudo(self.listaTec, arquivoCsv))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limparTec = Button(
        self.frame_consultaTec, text='Limpar', bg='#F2F2F2',
        command=lambda: limpar(self.listaTec))
    self.bt_limparTec.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_consultaTec, text='Consultar', bg='#F2F2F2',
        command=lambda: consultar(self.listaTec, self.codigo_entry,
                                  arquivoCsv))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_excluirTec = Button(
        self.frame_consultaTec, text='Excluir', bg='#F2F2F2',
        command=lambda: excluir(self.listaTec, arquivoCsv))
    self.bt_excluirTec.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)
