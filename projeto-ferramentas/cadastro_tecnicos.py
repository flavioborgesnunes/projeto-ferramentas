from tkinter import *
from tkinter import messagebox
import csv
from tempfile import NamedTemporaryFile

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
        self.root, bg=FONT_BG, highlightbackground='#aabbcc', highlightthickness=0)
    self.frame_cadastroTec.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cadastroTec = Label(self.frame_cadastroTec, fg="#16213E", text="CADASTRO DE TÉCNICOS", background='#BBBFCA',
                                   font=("Arial", 14, "bold"))
    self.title_cadastroTec.place(relx=0.25, rely=0.03)

    self.lb_cpf = Label(self.frame_cadastroTec, text='CPF',
                        bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_cpf.place(relx=0.05, rely=0.18)
    self.cpf_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
    self.cpf_entry.place(relx=0.05, rely=0.22,
                         relwidth=0.60, relheight=0.04)
    self.lb_nome = Label(self.frame_cadastroTec, text='Nome',
                         bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_nome.place(relx=0.05, rely=0.28)
    self.nome_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
    self.nome_entry.place(relx=0.05, rely=0.32,
                          relwidth=0.60, relheight=0.04)
    self.lb_telefone = Label(self.frame_cadastroTec, text='Telefone',
                             bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_telefone.place(relx=0.05, rely=0.38)
    self.telefone_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
    self.telefone_entry.place(
        relx=0.05, rely=0.42, relwidth=0.60, relheight=0.04)
    self.lb_turno = Label(self.frame_cadastroTec, text='Turno',
                          bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_turno.place(relx=0.05, rely=0.48)
    self.turno_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
    self.turno_entry.place(relx=0.05, rely=0.52,
                           relwidth=0.60, relheight=0.04)
    self.lb_equipe = Label(self.frame_cadastroTec, text='Nome da Equipe',
                           bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_equipe.place(relx=0.05, rely=0.58)
    self.equipe_entry = Entry(
        self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
    self.equipe_entry.place(relx=0.05, rely=0.62,
                            relwidth=0.60, relheight=0.04)

    self.bt_cadastrarTec = Button(
        self.frame_cadastroTec, text='Cadastrar', bg='#F2F2F2', command=lambda: self.dadosTec(self))
    self.bt_cadastrarTec.place(
        relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)


def dadosTec(self):

    self.cpf = self.cpf_entry.get()
    if len(self.cpf) != 11 or not self.cpf.isdigit():
        messagebox.showinfo(title="Atenção", message='Digite um CPF válido.')
        self.cpf = None
        return
    self.nome = self.nome_entry.get().title()

    self.telefone = self.telefone_entry.get()
    if len(self.telefone) != 9 or not self.telefone.isdigit():
        messagebox.showinfo(
            title="Atenção", message='Digite um telefone válido.')
        self.telefone = None
        return

    self.turno = self.turno_entry.get().title()
    self.equipe = self.equipe_entry.get().title()
    with open('tecnicos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        linhas = list(csv_reader)

    if (not self.cpf
                or not self.nome
                or not self.telefone
                or not self.turno
                or not self.equipe
            ):
        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')
        return

    else:
        self.cpf_entry.delete('0', 'end')
        self.nome_entry.delete('0', 'end')
        self.telefone_entry.delete('0', 'end')
        self.turno_entry.delete('0', 'end')
        self.equipe_entry.delete('0', 'end')
        messagebox.showinfo(
            title="Atenção", message='Cadastro realizado com sucesso')

        with open('tecnicos.csv', 'a', newline='') as csvfile:
            fieldnames = ['cpf', 'nome', 'telefone', 'turno', 'equipe']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writer.writeheader()
            writer.writerow({'cpf': self.cpf, 'nome': self.nome,
                            'telefone': self.telefone, 'turno': self.turno, 'equipe': self.equipe})
