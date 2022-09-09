from tkinter import Button, Frame, Label, Entry

label_style = {
    'bg': '#FFFFFF',
    'foreground': 'black',
    'font': 'fontStyle'
}
FONT_COLOR = "#16213E"
FONT_TYPE = "arial"
FONT_TAM = 11
FONT_BG = '#BBBFCA'


def botao_cadastroTec(self):

    self.frame_cadastroTec = Frame(
        self.root, bg=FONT_BG, highlightbackground='#aabbcc',
        highlightthickness=0)
    self.frame_cadastroTec.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cadastroTec = Label(self.frame_cadastroTec, fg="#16213E",
                                   text="CADASTRO DE TÉCNICOS",
                                   background='#BBBFCA',
                                   font=("Arial", 14, "bold"))
    self.title_cadastroTec.place(relx=0.25, rely=0.03)

    self.lb_cpf = Label(self.frame_cadastroTec, text='CPF',
                        bg=FONT_BG, fg=FONT_COLOR,
                        font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_cpf.place(relx=0.05, rely=0.18)
    self.cpf_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787',
        highlightthickness=1)
    self.cpf_entry.place(relx=0.05, rely=0.22,
                         relwidth=0.60, relheight=0.04)
    self.lb_nome = Label(self.frame_cadastroTec, text='Nome',
                         bg=FONT_BG, fg=FONT_COLOR,
                         font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_nome.place(relx=0.05, rely=0.28)
    self.nome_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787',
        highlightthickness=1)
    self.nome_entry.place(relx=0.05, rely=0.32,
                          relwidth=0.60, relheight=0.04)
    self.lb_telefone = Label(self.frame_cadastroTec, text='Telefone',
                             bg=FONT_BG, fg=FONT_COLOR,
                             font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_telefone.place(relx=0.05, rely=0.38)
    self.telefone_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787',
        highlightthickness=1)
    self.telefone_entry.place(
        relx=0.05, rely=0.42, relwidth=0.60, relheight=0.04)
    self.lb_turno = Label(self.frame_cadastroTec, text='Turno',
                          bg=FONT_BG, fg=FONT_COLOR,
                          font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_turno.place(relx=0.05, rely=0.48)
    self.turno_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787',
        highlightthickness=1)
    self.turno_entry.place(relx=0.05, rely=0.52,
                           relwidth=0.60, relheight=0.04)
    self.lb_equipe = Label(self.frame_cadastroTec, text='Nome da Equipe',
                           bg=FONT_BG, fg=FONT_COLOR,
                           font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_equipe.place(relx=0.05, rely=0.58)
    self.equipe_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787',
        highlightthickness=1)
    self.equipe_entry.place(relx=0.05, rely=0.62,
                            relwidth=0.60, relheight=0.04)

    self.bt_cadastrarTec = Button(
        self.frame_cadastroTec, text='Cadastrar', bg='#F2F2F2',
        command=lambda: self.cadastrar_Tec(self))
    self.bt_cadastrarTec.place(
        relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)
