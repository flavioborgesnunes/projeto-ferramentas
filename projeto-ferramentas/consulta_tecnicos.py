from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from csv import reader
import csv

BACKGROUND = '#BBBFCA'


def botao_consultaTec(self):
    # print('consulta Tec')
    self.frame_consultaTec = Frame(
        self.root, bd=4, bg=BACKGROUND, highlightbackground='#0D0D0D', highlightthickness=0)
    self.frame_consultaTec.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cunsultaTec = Label(self.frame_consultaTec, fg="#16213E", text="CONSULTA TÉCNICOS", background='#BBBFCA',
                                   font=("Arial", 14, "bold"))
    self.title_cunsultaTec.place(relx=0.25, rely=0.02)

    self.lb_codigo = Label(self.frame_consultaTec, text='Código',
                           background='#BBBFCA', foreground='black', font=("Arial", 12, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.16)
    self.codigo_entry = Entry(
        self.frame_consultaTec, highlightbackground='#878787', highlightthickness=1)
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
        self.frame_consultaTec, text='Mostrar Tudo', bg='#F2F2F2', command=lambda: show_table(self))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limparTec = Button(
        self.frame_consultaTec, text='Limpar', bg='#F2F2F2', command=lambda: limpar(self))
    self.bt_limparTec.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_consultaTec, text='Consultar', bg='#F2F2F2', command=lambda: self.consulta_tecnico(self))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_excluirTec = Button(
        self.frame_consultaTec, text='Excluir', bg='#F2F2F2', command=lambda: apagar_tecnico(self))
    self.bt_excluirTec.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)


def limpar(self):
    for i in self.listaTec.get_children():
        self.listaTec.delete(i)


def _elemento_esta_na_linha(elemento: str, linha: list):
    return elemento in linha


def _linha_com_elemento(elemento: str, linha: str):
    if _elemento_esta_na_linha(elemento, linha):
        return linha
    else:
        return None


def _linhas_no_arquivo(elemento: str, arquivo: list):
    """
    Percorre todo o arquivo retornando as linhas que contêm o elemento
    """
    _linhas_com_elemento = []
    for linha in arquivo:
        if linha_com_elemento := _linha_com_elemento(elemento, linha):
            _linhas_com_elemento.append(linha_com_elemento)
    return _linhas_com_elemento if len(_linhas_com_elemento) else None


def consulta_tecnico(self):
    entrada_codigo = self.codigo_entry.get()
    with open('tecnicos.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        linhas = list(csv_reader)
        if linhas_com_elementos := _linhas_no_arquivo(entrada_codigo, linhas):
            for linha in linhas_com_elementos:
                self.listaTec.insert("", END, values=linha)
        else:
            messagebox.showinfo(title="Atenção", message='Não Encontrado')


def apagar_tecnico(self):
    try:
        item_selecionado = self.listaTec.selection()[0]
        valores = self.listaTec.item(item_selecionado, "values")
        self.listaTec.delete(item_selecionado)
        messagebox.showinfo(title="Atenção", message='Item deletado!')
        # print(valores[0])

        # Apagar do arquivo csv
        lines = list()
        members = valores[0]

        with open('tecnicos.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == members:
                        lines.remove(row)

        with open('tecnicos.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    except:
        messagebox.showinfo(
            title="ERRO", message='Selecione um item a ser deletado!')


def show_table(self):
    limpar(self)

    with open('tecnicos.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        linhas = list(csv_reader)
        elemento_lista = False
        for lista in linhas:
            # if lista != linhas[0]:
            self.listaTec.insert("", END, values=lista)
