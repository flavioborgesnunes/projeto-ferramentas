from tkinter import ttk, Button, Entry, Label, Frame
from modulos.funcoes import excluir, consultar, limpar, mostrar_tudo

BACKGROUND = '#BBBFCA'
arquivoCsv = './arquivos/ferramentas.csv'


def botao_consultaF(self):

    self.frame_consultaFer = Frame(
        self.root, bd=4, bg=BACKGROUND, highlightbackground='#0D0D0D',
        highlightthickness=0)
    self.frame_consultaFer.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cunsulta = Label(self.frame_consultaFer, fg="#16213E",
                                text="CONSULTA FERRAMENTAS",
                                background='#BBBFCA',
                                font=("Arial", 14, "bold"))
    self.title_cunsulta.place(relx=0.25, rely=0.02)

    self.lb_codigo = Label(self.frame_consultaFer, text='Código',
                           background='#BBBFCA', foreground='black',
                           font=("Arial", 12, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.16)
    self.codigo_entry = Entry(
        self.frame_consultaFer, highlightbackground='#878787',
        highlightthickness=1)
    self.codigo_entry.place(relx=0.05, rely=0.20,
                            relwidth=0.20, relheight=0.04)

    self.listaF = ttk.Treeview(self.frame_consultaFer, height=1, columns=(
        'col1', 'col2', 'col3', 'col4', 'col5', 'col6',
        'col7', 'col8', 'col9', 'col10', 'col11'))
    self.listaF.heading('#0', text='')
    self.listaF.heading('#1', text='Código')
    self.listaF.heading('#2', text='Desc')
    self.listaF.heading('#3', text='Fab')
    self.listaF.heading('#4', text='volt')
    self.listaF.heading('#5', text='Tam')
    self.listaF.heading('#6', text='U.Med')
    self.listaF.heading('#7', text='Tipo')
    self.listaF.heading('#8', text='Material')
    self.listaF.heading('#9', text='Res')
    self.listaF.heading('#10', text='Critica')
    self.listaF.heading('#11', text='Quant.')

    self.listaF.column('#0', width=0)
    self.listaF.column('#1', width=50)
    self.listaF.column('#2', width=50)
    self.listaF.column('#3', width=50)
    self.listaF.column('#4', width=50)
    self.listaF.column('#5', width=50)
    self.listaF.column('#6', width=50)
    self.listaF.column('#7', width=50)
    self.listaF.column('#8', width=50)
    self.listaF.column('#9', width=50)
    self.listaF.column('#10', width=50)
    self.listaF.column('#11', width=50)

    self.listaF.place(relx=0.01, rely=0.3, relwidth=0.95, relheight=0.5)

    self.scrollLista = ttk.Scrollbar(
        self.frame_consultaFer, orient='vertical', command=self.listaF.yview)
    self.listaF.configure(yscroll=self.scrollLista.set)
    self.scrollLista.place(relx=0.96, rely=0.3,
                           relwidth=0.04, relheight=0.5)

    self.bt_show_all = Button(
        self.frame_consultaFer, text='Mostrar Tudo', bg='#F2F2F2',
        command=lambda: mostrar_tudo(self.listaF, arquivoCsv))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limp_all = Button(
        self.frame_consultaFer, text='Limpar', bg='#F2F2F2',
        command=lambda: limpar(self.listaF))
    self.bt_limp_all.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_consultaFer, text='Consultar', bg='#F2F2F2',
        command=lambda: consultar(self.listaF, self.codigo_entry, arquivoCsv))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_excluirF = Button(
        self.frame_consultaFer, text='Excluir', bg='#F2F2F2',
        command=lambda: excluir(self.listaF, arquivoCsv))
    self.bt_excluirF.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)
