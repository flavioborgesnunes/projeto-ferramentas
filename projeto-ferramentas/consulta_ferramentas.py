from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from csv import reader
import csv

BACKGROUND = '#BBBFCA'


def botao_consultaF(self):

    self.frame_consultaFer = Frame(
        self.root, bd=4, bg=BACKGROUND, highlightbackground='#0D0D0D', highlightthickness=0)
    self.frame_consultaFer.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_cunsulta = Label(self.frame_consultaFer, fg="#16213E", text="CONSULTA FERRAMENTAS", background='#BBBFCA',
                                font=("Arial", 14, "bold"))
    self.title_cunsulta.place(relx=0.25, rely=0.02)

    self.lb_codigo = Label(self.frame_consultaFer, text='Código',
                           background='#BBBFCA', foreground='black', font=("Arial", 12, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.16)
    self.codigo_entry = Entry(
        self.frame_consultaFer, highlightbackground='#878787', highlightthickness=1)
    self.codigo_entry.place(relx=0.05, rely=0.20,
                            relwidth=0.20, relheight=0.04)

    self.listaF = ttk.Treeview(self.frame_consultaFer, height=1, columns=(
        'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11'))
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
        self.frame_consultaFer, text='Mostrar Tudo', bg='#F2F2F2', command=lambda: show_table(self))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limp_all = Button(
        self.frame_consultaFer, text='Limpar', bg='#F2F2F2', command=lambda: limpar(self))
    self.bt_limp_all.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_consultaFer, text='Consultar', bg='#F2F2F2', command=lambda: self.consulta_ferramenta(self))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_excluirF = Button(
        self.frame_consultaFer, text='Excluir', bg='#F2F2F2', command=lambda: apagar_ferramenta(self))
    self.bt_excluirF.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)

def limpar(self):
    for i in self.listaF.get_children():
        self.listaF.delete(i)


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


def consulta_ferramenta(self):
    limpar(self)
    entrada_codigo = self.codigo_entry.get()
    with open('ferramentas.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        linhas = list(csv_reader)
        if linhas_com_elementos := _linhas_no_arquivo(entrada_codigo, linhas):
            for linha in linhas_com_elementos:
                self.listaF.insert("", END, values=linha)
        else:
            messagebox.showinfo(title="Atenção", message='Não Encontrado')


def apagar_ferramenta(self):
    try:
        item_selecionado = self.listaF.selection()[0]
        valores = self.listaF.item(item_selecionado, "values")
        self.listaF.delete(item_selecionado)
        messagebox.showinfo(title="ERRO", message='Item deletado!')

        # Apagar do arquivo csv
        lines = list()
        members = valores[0]

        with open('ferramentas.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == members:
                        lines.remove(row)

        with open('ferramentas.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    except:
        messagebox.showinfo(
            title="ERRO", message='Selecione um item a ser deletado!')


def show_table(self):
    limpar(self)

    with open('ferramentas.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        linhas = list(csv_reader)
        elemento_lista = False
        for lista in linhas:
            # if lista != linhas[0]:
            self.listaF.insert("", END, values=lista)
