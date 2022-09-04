from tkinter import *
from tkinter import messagebox
import tkinter as tk
from cadastro_ferramentas import *
from cadastro_tecnicos import *
from consulta_ferramentas import *
from consulta_tecnicos import *
from agenda import *
from csv import writer


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
        self.dados = dados
        self.botao_cadastroTec = botao_cadastroTec
        self.dadosTec = dadosTec
        self.botao_consultaF = botao_consultaF
        self.consulta_ferramenta = consulta_ferramenta
        self.botao_consultaTec = botao_consultaTec
        self.consulta_tecnico = consulta_tecnico
        self.botao_agenda = botao_agenda
        self.calendario = calendario
        self.agendar = agendar
        self.consulta_agendamento = consulta_agendamento
        self.devolucao = devolucao
        self.frames_de_tela()
        self.widgets_frame1()
        botao_cadastroF(self)
        self.apagar_ferramenta = apagar_ferramenta
        

    def tela(self):
        self.root.title('Central de Ferramentaria')
        self.root.configure(background='#463A3E', padx=0, pady=0)
        self.root.geometry('900x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=420)

    def frames_de_tela(self):
        self.frame_2 = Frame(self.root, bd=4, bg='#708090',
                             highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_2.place(relx=0, rely=0.0, relwidth=0.23, relheight=1)

        self.frame_cadastroTec = Frame(
            self.root, bd=4, bg='red', highlightbackground='#878787', highlightthickness=0.5)
        self.frame_cadastroTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_cadastro = Frame(
            self.root, bd=4, bg='yellow', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_cadastro.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_consultaFer = Frame(
            self.root, bd=4, bg='red', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaFer.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_consultaTec = Frame(
            self.root, bd=4, bg='green', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_agenda = Frame(
            self.root, bd=4, bg='green', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_agenda.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

    def widgets_frame1(self):
        # Botão cadastar ferramentas
        self.bt_cadastroFer = Button(
            self.frame_2, text=' Ferramentas', bg='#F2F2F2', command=lambda: self.botao_cadastroF(self))
        self.bt_cadastroFer.place(
            relx=0.01, rely=0.1, relwidth=1, relheight=0.05)
        # Botão cadastrar tecnico
        self.bt_cadastroTec = Button(
            self.frame_2, text='Técnicos', bg='#F2F2F2', command=lambda: self.botao_cadastroTec(self))
        self.bt_cadastroTec.place(
            relx=0.01, rely=0.152, relwidth=1, relheight=0.05)
        # Botão consulta Ferramenta
        self.bt_consultaFer = Button(
            self.frame_2, text='Ferramentas', bg='#F2F2F2', command=lambda: self.botao_consultaF(self))
        self.bt_consultaFer.place(
            relx=0.01, rely=0.30, relwidth=1, relheight=0.05)
        # Botão consultar Técnico
        self.bt_consultaTec = Button(
            self.frame_2, text='Técnicos', bg='#F2F2F2', command=lambda: self.botao_consultaTec(self))
        self.bt_consultaTec.place(
            relx=0.01, rely=0.353, relwidth=1, relheight=0.05)
        # Botão agenda
        self.bt_agenda = Button(
            self.frame_2, text='Agenda', bg='#F2F2F2', command=lambda: self.botao_agenda(self))
        self.bt_agenda.place(
            relx=0.01, rely=0.5, relwidth=1, relheight=0.05)
        # texto cadastro
        self.lb_cadastro = Label(
            self.frame_2, text='Cadastro', bg='#130633', foreground='white', font='fontStyle')
        self.lb_cadastro.place(relx=0.01, rely=0.05,
                               relwidth=1, relheight=0.05)
        # texto consulta
        self.lb_consulta = Label(
            self.frame_2, text='Consulta', bg='#130633', foreground='white', font='fontStyle')
        self.lb_consulta.place(relx=0.01, rely=0.25,
                               relwidth=1, relheight=0.05)
        # texto agenda
        self.lb_consulta = Label(
            self.frame_2, text='Agenda', bg='#130633', foreground='white', font='fontStyle')
        self.lb_consulta.place(relx=0.01, rely=0.45,
                               relwidth=1, relheight=0.05)


class Window_login:

    def __init__(self, master):
        self.settings = None
        self.master = master
        self.master.title("Login Central ferramentaria")
        self.master.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="user_200.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0, columnspan=2)
        self.canvas.config(bg=THEME_COLOR, highlightthickness=0)

        # Textos
        self.text_user = Label(text='Usuário')
        self.text_user.grid(column=0, row=1)
        self.text_user.config(bg=THEME_COLOR)
        self.text_senha = Label(text='Senha')
        self.text_senha.grid(column=0, row=2)
        self.text_senha.config(bg=THEME_COLOR)
        self.text_new_cadastro = Label(text='Para cadastrar novo usuário!')
        self.text_new_cadastro.grid(column=0, row=5, columnspan=2)
        self.text_new_cadastro.config(bg=THEME_COLOR)

        # Entradas
        self.entry_user = Entry(width=35)
        self.entry_user.grid(column=1, row=1, columnspan=2, pady=10)
        self.entry_senha = Entry(width=35)
        self.entry_senha.grid(column=1, row=2, columnspan=2, pady=5)

        # Botão
        self.button_entrar = Button(text='Entrar', width=29, command=lambda: self.login())
        self.button_entrar.grid(column=1, row=4, columnspan=2, pady=30)

        self.button_cadastrar = Button(text='Cadastrar', width=10, command=lambda: self.cadastrar_login())
        self.button_cadastrar.grid(column=2, row=5, )

    def chamar_janela_principal(self):
        self.settings = Application()
        self.settings.win.mainloop()

    def login(self):
        self.user = self.entry_user.get()
        self.senha = self.entry_senha.get()

        with open('senha_entrada.csv', 'r') as csv_file:
            csv_reader = reader(csv_file)

            linhas = list(csv_reader)

            elemento_lista = False
            msg = True
            for lista in linhas:

                if self.user == lista[0]:
                    msg = False

            if msg:
                messagebox.showinfo(title="Atenção", message='Usuário não cadastro')

            else:
                msg2 = True
                for lista in linhas:
                    if self.user == lista[0] and self.senha == lista[1]:
                        self.chamar_janela_principal()
                        msg2 = False

                if msg2:
                    messagebox.showinfo(title="Atenção", message='Usuário e senha não confere!')



    def cadastrar_login(self):
        self.user  = self.entry_user.get()
        self.senha = self.entry_senha.get()

        with open('senha_entrada.csv', 'r') as file:
            csv_reader = reader(file)
            linhas = str(csv_reader)
            msg3 = True
            for lista in linhas:
                if self.user == lista[0]:
                    msg3 = False
            if msg3:
                messagebox.showinfo(title="Atenção", message='Usuário já cadastrado')

            else:
                with open('senha_entrada.csv', 'a', newline='') as csvfile2:
                    writer_object = writer(csvfile2)
                    list_data = [self.user, str(self.senha)]
                    writer_object.writerow(list_data)
                    messagebox.showinfo(title="Atenção", message='Novo usuário cadastrado')
                    csvfile2.close()




root = tk.Tk()
window = Window_login(root)

root.mainloop()
