from tkinter import messagebox, Button, Frame, Label, Entry, Canvas, PhotoImage
import tkinter as tk
from frames.cadastro_ferramentas import botao_cadastroF
from frames.cadastro_tecnicos import botao_cadastroTec
from frames.consulta_ferramentas import botao_consultaF
from frames.consulta_tecnicos import botao_consultaTec
from frames.agenda import botao_agenda, calendario
from modulos.funcoes import (excluir, excluir_user, cadastrar_login, consultar,
                             cadastrar_Tec, cadastrar_ferramentas)
from modulos.funcoes_agenda import devolver, agendar
from csv import reader

THEME_COLOR = '#BBBFCA'


class Application:

    def __init__(self):
        self.win = tk.Toplevel()
        self.win.withdraw()
        self.tempo_reserva = None
        self.material_ferramenta = None
        self.tipo_ferramenta = None
        self.unidade_medida = None
        self.tamanho = None
        self.part_number = None
        self.voltagem = None
        self.fabricante = None
        self.descricao = None

        self.root = root
        self.tela()
        self.botao_cadastroF = botao_cadastroF
        self.cadastrar_ferramentas = cadastrar_ferramentas
        self.botao_cadastroTec = botao_cadastroTec
        self.cadastrar_Tec = cadastrar_Tec
        self.botao_consultaF = botao_consultaF
        self.consultar = consultar
        self.botao_consultaTec = botao_consultaTec
        self.botao_agenda = botao_agenda
        self.calendario = calendario
        self.agendar = agendar
        self.devolver = devolver
        self.cadastrar_login = cadastrar_login
        self.excluir_user = excluir_user
        self.frames_de_tela()
        self.widgets_frame1()
        self.excluir = excluir
        botao_agenda(self)

    def tela(self):
        self.root.title('Central de Ferramentaria')
        self.root.configure(background='#463A3E', padx=0, pady=0)
        self.root.geometry('900x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=420)

    def frames_de_tela(self):
        self.frame_2 = Frame(self.root, bd=4, bg='#708090',
                             highlightbackground='#0D0D0D',
                             highlightthickness=0)
        self.frame_2.place(relx=0, rely=0.0, relwidth=0.23, relheight=1)

        self.frame_cadastroTec = Frame(
            self.root, bd=4, highlightbackground='#878787',
            highlightthickness=0.5)
        self.frame_cadastroTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)
        self.frame_cadastroFer = Frame(
            self.root, bd=4,  highlightbackground='#878787',
            highlightthickness=0.5)
        self.frame_cadastroFer.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)
        self.frame_consultaFer = Frame(
            self.root, bd=4, highlightbackground='#0D0D0D',
            highlightthickness=0)
        self.frame_consultaFer.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)
        self.frame_consultaTec = Frame(
            self.root, bd=4, highlightbackground='#0D0D0D',
            highlightthickness=0)
        self.frame_consultaTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)
        self.frame_agenda = Frame(
            self.root, bd=4,  highlightbackground='#0D0D0D',
            highlightthickness=0)
        self.frame_agenda.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

    def widgets_frame1(self):
        # Bot??o cadastar ferramentas
        self.bt_cadastroFer = Button(
            self.frame_2, text=' Ferramentas', bg='#F2F2F2',
            command=lambda: self.botao_cadastroF(self))
        self.bt_cadastroFer.place(
            relx=0.01, rely=0.1, relwidth=1, relheight=0.05)
        # Bot??o cadastrar tecnico
        self.bt_cadastroTec = Button(
            self.frame_2, text='T??cnicos', bg='#F2F2F2',
            command=lambda: self.botao_cadastroTec(self))
        self.bt_cadastroTec.place(
            relx=0.01, rely=0.152, relwidth=1, relheight=0.05)
        # Bot??o consulta Ferramenta
        self.bt_consultaFer = Button(
            self.frame_2, text='Ferramentas', bg='#F2F2F2',
            command=lambda: self.botao_consultaF(self))
        self.bt_consultaFer.place(
            relx=0.01, rely=0.30, relwidth=1, relheight=0.05)
        # Bot??o consultar T??cnico
        self.bt_consultaTec = Button(
            self.frame_2, text='T??cnicos', bg='#F2F2F2',
            command=lambda: self.botao_consultaTec(self))
        self.bt_consultaTec.place(
            relx=0.01, rely=0.353, relwidth=1, relheight=0.05)
        # Bot??o agenda
        self.bt_agenda = Button(
            self.frame_2, text='Agenda', bg='#F2F2F2',
            command=lambda: self.botao_agenda(self))
        self.bt_agenda.place(
            relx=0.01, rely=0.5, relwidth=1, relheight=0.05)
        # Bot??o cadastrar usu??rio
        self.button_cadastrar = Button(
            self.frame_2, text='Cadastrar Usu??rio', bg='#F2F2F2',
            command=lambda: self.cadastrar_login(self))
        self.button_cadastrar.place(
            relx=0.09, rely=0.9, relwidth=0.75, relheight=0.042)
        # Bot??o Excluir Usu??rio
        self.button_excluir_usuario = Button(
            self.frame_2, text='Excluir Usu??rio', bg='#F2F2F2',
            command=lambda: self.excluir_user(self))
        self.button_excluir_usuario.place(
            relx=0.09, rely=0.95, relwidth=0.75, relheight=0.042)
        # texto cadastro
        self.lb_cadastro = Label(
            self.frame_2, text='Cadastro', bg='#130633',
            foreground='white', font='fontStyle')
        self.lb_cadastro.place(relx=0.01, rely=0.05,
                               relwidth=1, relheight=0.05)
        # texto consulta
        self.lb_consulta = Label(
            self.frame_2, text='Consulta', bg='#130633',
            foreground='white', font='fontStyle')
        self.lb_consulta.place(relx=0.01, rely=0.25,
                               relwidth=1, relheight=0.05)
        # texto agenda
        self.lb_consulta = Label(
            self.frame_2, text='Agenda', bg='#130633',
            foreground='white', font='fontStyle')
        self.lb_consulta.place(relx=0.01, rely=0.45,
                               relwidth=1, relheight=0.05)
        # Texto cadastro login
        self.text_new_cadastro = Label(
            text='Para cadastrar novo usu??rio!', bg='#708090')
        self.text_new_cadastro.place(relx=0.01, rely=0.75,
                                     relwidth=0.2, relheight=0.03)

        self.entry_user_cadastro = Entry(width=35)
        self.entry_user_cadastro.place(relx=0.01, rely=0.8,
                                       relwidth=0.2, relheight=0.03)
        self.entry_senha_cadastro = Entry(width=35)
        self.entry_senha_cadastro.place(relx=0.01, rely=0.85,
                                        relwidth=0.2, relheight=0.03)


class Window_login:

    def __init__(self, master):
        self.settings = None
        self.master = master
        self.master.title("Login Central ferramentaria")
        self.master.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="./arquivos/user_200.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0, columnspan=2)
        self.canvas.config(bg=THEME_COLOR, highlightthickness=0)

        # Textos
        self.text_user = Label(text='Usu??rio')
        self.text_user.grid(column=0, row=1)
        self.text_user.config(bg=THEME_COLOR)
        self.text_senha = Label(text='Senha')
        self.text_senha.grid(column=0, row=2)
        self.text_senha.config(bg=THEME_COLOR)

        # Entradas
        self.entry_user = Entry(width=35)
        self.entry_user.grid(column=1, row=1, columnspan=2, pady=10)
        self.entry_senha = Entry(width=35)
        self.entry_senha.grid(column=1, row=2, columnspan=2, pady=5)

        # Bot??o
        self.button_entrar = Button(
            text='Entrar', width=29, command=lambda: self.login())
        self.button_entrar.grid(column=1, row=4, columnspan=2, pady=30)

    def chamar_janela_principal(self):
        self.settings = Application()
        self.settings.win.mainloop()

    def login(self):
        self.user = self.entry_user.get()
        self.senha = self.entry_senha.get()

        with open('./arquivos/senha_entrada.csv', 'r') as csv_file:
            csv_reader = reader(csv_file)
            linhas = list(csv_reader)
            msg = True
            for lista in linhas:
                if self.user == lista[0]:
                    msg = False
            if msg:
                messagebox.showinfo(
                    title="Aten????o", message='Usu??rio n??o cadastradoS')
            else:
                msg2 = True
                for lista in linhas:
                    if self.user == lista[0] and self.senha == lista[1]:
                        self.chamar_janela_principal()
                        msg2 = False
                if msg2:
                    messagebox.showinfo(
                        title="Aten????o",
                        message='Usu??rio e senha n??o conferem!')


root = tk.Tk()
window = Window_login(root)

root.mainloop()
