from tkinter import ttk, Button, Label, Entry, Frame
from tkcalendar import Calendar
from modulos.funcoes import consultar, limpar, mostrar_tudo
from modulos.funcoes_agenda import devolver, agendar

FONT_COLOR = "#16213E"
FONT_TYPE = "arial"
FONT_TAM = 11
FONT_BG = '#BBBFCA'
arquivoCsv = './arquivos/agenda.csv'


def botao_agenda(self):

    self.frame_agenda = Frame(
        self.root, bd=4, bg=FONT_BG, highlightbackground=FONT_BG,
        highlightthickness=0)
    self.frame_agenda.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_agenda = Label(self.frame_agenda, fg="#16213E",
                              text="Agendar Ferramenta", background=FONT_BG,
                              font=("Arial", 14, "bold"))
    self.title_agenda.place(relx=0.25, rely=0.03)

    # Entrys
    self.lb_codigo = Label(self.frame_agenda, text='Codigo',
                           bg=FONT_BG, fg=FONT_COLOR,
                           font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.12)
    self.codigo_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.codigo_entry.place(relx=0.05, rely=0.17,
                            relwidth=0.30, relheight=0.04)

    self.lb_descricao = Label(self.frame_agenda, text='Descrição',
                              bg=FONT_BG, fg=FONT_COLOR,
                              font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_descricao.place(relx=0.5, rely=0.12)
    self.descricao_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.descricao_entry.place(relx=0.5, rely=0.17,
                               relwidth=0.30, relheight=0.04)

    # Calendario retirada
    self.bt_calendario_retirada = Button(
        self.frame_agenda, text='Data', command=lambda: calendario(self))
    self.bt_calendario_retirada.place(relx=0.05, rely=0.23)

    self.retirada_entry1 = Entry(
        self.frame_agenda, highlightbackground=FONT_BG,
        highlightthickness=1, width=10)
    self.retirada_entry1.place(relx=0.05, rely=0.27)

    # horário de retirada:
    self.lb_retirada = Label(self.frame_agenda, text='Hora',
                             bg=FONT_BG, fg=FONT_COLOR,
                             font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_retirada.place(relx=0.2, rely=0.23)
    vlist = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30",
             "03:00", "03:30", "04:00", "04:30", "05:00", "05:30",
             "06:00", "06:30", "07:00", "07:30", "08:00", "08:30",
             "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
             "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
             "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
             "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
             "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",
             ]
    self.retirada_hora_entry = ttk.Combobox(
        self.frame_agenda, width=10,  values=vlist)
    self.retirada_hora_entry.place(relx=0.2, rely=0.27)

    # calendário devolução
    self.bt_calendario_devolucao = Button(
        self.frame_agenda, text='Data', command=lambda: calendario2(self))
    self.bt_calendario_devolucao.place(relx=0.5, rely=0.23)

    self.devolucao1_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG,
        highlightthickness=1, width=10)
    self.devolucao1_entry.place(relx=0.5, rely=0.27,)

    # Horário devolução
    self.lb_devolucao = Label(self.frame_agenda, text='Hora',
                              bg=FONT_BG, fg=FONT_COLOR,
                              font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_devolucao.place(relx=0.65, rely=0.23)
    vlist = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30",
             "03:00", "03:30", "04:00", "04:30", "05:00", "05:30",
             "06:00", "06:30", "07:00", "07:30", "08:00", "08:30",
             "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
             "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
             "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
             "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
             "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",
             ]
    self.devolucao_hora_entry = ttk.Combobox(
        self.frame_agenda, width=10,  values=vlist)
    self.devolucao_hora_entry.place(relx=0.65, rely=0.27)

    self.lb_tecnico = Label(self.frame_agenda, text='Técnico',
                            bg=FONT_BG, fg=FONT_COLOR,
                            font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tecnico.place(relx=0.05, rely=0.32)
    self.tecnico_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.tecnico_entry.place(relx=0.05, rely=0.37,
                             relwidth=0.30, relheight=0.04)

    # Botão agendar
    self.bt_agendar = Button(
        self.frame_agenda, text='Agendar', bg='#F2F2F2',
        command=lambda: agendar(self))
    self.bt_agendar.place(
        relx=0.7, rely=0.37, relwidth=0.3, relheight=0.05)

    self.listaAgendamento = ttk.Treeview(self.frame_agenda, height=1, columns=(
        'col1', 'col2', 'col3', 'col4', 'col5'))
    self.listaAgendamento.heading('#0', text='')
    self.listaAgendamento.heading('#1', text='Codigo')
    self.listaAgendamento.heading('#2', text='Descrição')
    self.listaAgendamento.heading('#3', text='Retirada')
    self.listaAgendamento.heading('#4', text='Devolução')
    self.listaAgendamento.heading('#5', text='Técnico')

    self.listaAgendamento.column('#0', width=0)
    self.listaAgendamento.column('#1', width=100)
    self.listaAgendamento.column('#2', width=100)
    self.listaAgendamento.column('#3', width=100)
    self.listaAgendamento.column('#4', width=100)
    self.listaAgendamento.column('#5', width=100)

    self.listaAgendamento.place(
        relx=0.01, rely=0.5, relwidth=0.95, relheight=0.3)

    self.scrollLista = ttk.Scrollbar(
        self.frame_agenda, orient='vertical',
        command=self.listaAgendamento.yview)
    self.listaAgendamento.configure(yscroll=self.scrollLista.set)
    self.scrollLista.place(relx=0.96, rely=0.5, relwidth=0.04, relheight=0.3)
    self.lb_codigo_consulta = Label(self.frame_agenda, text='Código',
                                    bg=FONT_BG, fg=FONT_COLOR,
                                    font=(FONT_TYPE, FONT_TAM, "bold"))

    self.lb_codigo_consulta.place(relx=0.05, rely=0.80)
    self.codigo_consulta_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.codigo_consulta_entry.place(relx=0.05, rely=0.85,
                                     relwidth=0.30, relheight=0.04)

    self.bt_show_all = Button(
        self.frame_agenda, text='Mostrar Tudo', bg='#F2F2F2',
        command=lambda: mostrar_tudo(self.listaAgendamento, arquivoCsv))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limparAgenda = Button(
        self.frame_agenda, text='Limpar', bg='#F2F2F2',
        command=lambda: limpar(self.listaAgendamento))
    self.bt_limparAgenda.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_agenda, text='Consultar', bg='#F2F2F2',
        command=lambda: consultar(self.listaAgendamento,
                                  self.codigo_consulta_entry, arquivoCsv))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_devolver = Button(
        self.frame_agenda, text='Devolver', bg='#F2F2F2',
        command=lambda: devolver(self))
    self.bt_devolver.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)

# fuções dos calendarios


def calendario(self):
    self.calendario_retirada = Calendar(self.frame_agenda, locale='pt_br')
    self.calendario_retirada.place(relx=0.05, rely=0.27)
    self.calData_retirada = Button(
        self.frame_agenda, text='Inserir Data',
        command=lambda: print_cal_retirada(self))
    self.calData_retirada.place(relx=0.1, rely=0.54, height=25, width=100)


def print_cal_retirada(self):
    dataIni = self.calendario_retirada.get_date()
    self.calendario_retirada.destroy()
    self.retirada_entry1.delete('0', 'end')
    self.retirada_entry1.insert('end', dataIni)
    self.calData_retirada.destroy()


def calendario2(self):
    self.calendario_devolucao = Calendar(self.frame_agenda, locale='pt_br')
    self.calendario_devolucao.place(relx=0.5, rely=0.27)
    self.calData_devolucao = Button(
        self.frame_agenda, text='Inserir Data',
        command=lambda: print_cal_devolucao(self))
    self.calData_devolucao.place(relx=0.55, rely=0.54, height=25, width=100)


def print_cal_devolucao(self):
    dataIni = self.calendario_devolucao.get_date()
    self.calendario_devolucao.destroy()
    self.devolucao1_entry.delete('0', 'end')
    self.devolucao1_entry.insert('end', dataIni)
    self.calData_devolucao.destroy()
