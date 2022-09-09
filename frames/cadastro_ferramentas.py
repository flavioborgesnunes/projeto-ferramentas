from tkinter import *
from tkinter import messagebox, ttk
import csv
from csv import reader

FONT_COLOR = "#16213E"
FONT_TYPE = "arial"
FONT_TAM = 11
FONT_BG = '#BBBFCA'


def botao_cadastroF(self):
    # print('cadastro')
    self.frame_cadastro = Frame(
        self.root, bd=4, bg=FONT_BG, highlightbackground='#aabbcc', highlightthickness=0)
    self.frame_cadastro.place(relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cadastro = Label(self.frame_cadastro, fg="#16213E", text="CADASTRO DE FERRAMENTAS", background='#BBBFCA',
                                font=("Arial", 14, "bold"))
    self.title_cadastro.place(relx=0.25, rely=0.03)

    self.lb_descricao = Label(self.frame_cadastro, fg=FONT_COLOR, text='Descrição da Ferramenta',
                              background=FONT_BG,
                              font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_descricao.place(relx=0.05, rely=0.18)
    self.descricao_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.descricao_entry.place(
        relx=0.05, rely=0.22, relwidth=0.60, relheight=0.04)
    self.lb_fabricante = Label(self.frame_cadastro, text='Fabricante', fg=FONT_COLOR,  background=FONT_BG,
                               font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_fabricante.place(relx=0.05, rely=0.28)
    self.fabricante_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.fabricante_entry.place(
        relx=0.05, rely=0.32, relwidth=0.60, relheight=0.04)

    self.lb_voltagem = Label(self.frame_cadastro, fg=FONT_COLOR, text='Voltagem', background=FONT_BG,
                             font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_voltagem.place(relx=0.05, rely=0.38)
    # self.voltagem_entry = Entry(self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    vlist = ["110", "220", "None"]
    self.voltagem_entry = ttk.Combobox(self.frame_cadastro, values=vlist)
    self.voltagem_entry.set("SELECIONE")
    self.voltagem_entry.place(relx=0.05, rely=0.42,
                              relwidth=0.20, relheight=0.04)

    self.lb_tamanho = Label(self.frame_cadastro, text='Tamanho', fg=FONT_COLOR,  background=FONT_BG,
                            font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tamanho.place(relx=0.5, rely=0.38)

    self.tamanho_entry_1 = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.tamanho_entry_1.place(
        relx=0.5, rely=0.42, relwidth=0.05, relheight=0.04)

    self.lb_tamanho_x = Label(self.frame_cadastro, text='X', fg=FONT_COLOR,  background=FONT_BG,
                              font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tamanho_x.place(relx=0.564, rely=0.42)
    self.tamanho_entry_2 = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.tamanho_entry_2.place(
        relx=0.6, rely=0.42, relwidth=0.05, relheight=0.04)

    self.lb_unidade = Label(self.frame_cadastro, text='Unidade de Medida', fg=FONT_COLOR,
                            background=FONT_BG,
                            font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_unidade.place(relx=0.05, rely=0.48)
    self.unidade_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.unidade_entry.place(relx=0.05, rely=0.52,
                             relwidth=0.60, relheight=0.04)

    self.lb_tipo = Label(self.frame_cadastro, text='Tipo da Ferramenta', fg=FONT_COLOR,
                         background=FONT_BG,
                         font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tipo.place(relx=0.05, rely=0.58)
    list_tip = ["Eletrica", "Manual", "Mecanica", "Grande Porte"]
    self.tipo_entry = ttk.Combobox(self.frame_cadastro, values=list_tip)
    self.tipo_entry.set("SELECIONE")
    # self.tipo_entry = Entry(self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.tipo_entry.place(relx=0.05, rely=0.62, relwidth=0.60, relheight=0.04)

    self.lb_material = Label(self.frame_cadastro, text='Material da Ferramenta', fg=FONT_COLOR,
                             background=FONT_BG,
                             font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_material.place(relx=0.05, rely=0.68)
    self.material_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.material_entry.place(relx=0.05, rely=0.72,
                              relwidth=0.60, relheight=0.04)
    self.lb_tempo = Label(self.frame_cadastro, text='Tempode Reserva', fg=FONT_COLOR,
                          background=FONT_BG,
                          font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tempo.place(relx=0.05, rely=0.78)
    self.tempo_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.tempo_entry.place(relx=0.05, rely=0.82, relwidth=0.10, relheight=0.04)

    self.lb_critica = Label(self.frame_cadastro, fg=FONT_COLOR, text='É Crítica?', background=FONT_BG,
                            font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_critica.place(relx=0.27, rely=0.78)
    # self.voltagem_entry = Entry(self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    vlist = ["SIM", "NAO"]
    self.critica_entry = ttk.Combobox(self.frame_cadastro, values=vlist)
    self.critica_entry.set("SELECIONE")
    self.critica_entry.place(relx=0.27, rely=0.82,
                             relwidth=0.10, relheight=0.04)

    self.lb_quantidade = Label(self.frame_cadastro, text='Quantidade', fg=FONT_COLOR,  background=FONT_BG,
                               font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_quantidade.place(relx=0.5, rely=0.78)
    self.quantidade_entry = Entry(
        self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
    self.quantidade_entry.place(
        relx=0.5, rely=0.82, relwidth=0.10, relheight=0.04)
    # Botao cadastrar
    self.bt_cadastrarF = Button(
        self.frame_cadastro, text='Cadastrar', bg='#F2F2F2', command=lambda: self.cadastrar_ferramentas(self))
    self.bt_cadastrarF.place(relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)
