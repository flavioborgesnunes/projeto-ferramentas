from calendar import calendar
import locale
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
from csv import reader
import shutil
from tempfile import NamedTemporaryFile
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta

FONT_COLOR = "#16213E"
FONT_TYPE = "arial"
FONT_TAM = 11
FONT_BG = '#BBBFCA'


def botao_agenda(self):

    self.frame_agenda = Frame(
        self.root, bd=4, bg=FONT_BG, highlightbackground=FONT_BG, highlightthickness=0)
    self.frame_agenda.place(
        relx=0.23, rely=0.0, relwidth=0.77, relheight=1)

    self.title_agenda = Label(self.frame_agenda, fg="#16213E", text="Agendar Ferramenta", background=FONT_BG,
                              font=("Arial", 14, "bold"))
    self.title_agenda.place(relx=0.25, rely=0.03)

    # Entrys
    self.lb_codigo = Label(self.frame_agenda, text='Codigo',
                           bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_codigo.place(relx=0.05, rely=0.12)
    self.codigo_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.codigo_entry.place(relx=0.05, rely=0.17,
                            relwidth=0.30, relheight=0.04)

    self.lb_descricao = Label(self.frame_agenda, text='Descrição',
                              bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
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
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1, width=10)
    self.retirada_entry1.place(relx=0.05, rely=0.27)

    # horário de retirada:
    self.lb_retirada = Label(self.frame_agenda, text='Hora',
                             bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
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
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1, width=10)
    self.devolucao1_entry.place(relx=0.5, rely=0.27,)

    # Horário devolução
    self.lb_devolucao = Label(self.frame_agenda, text='Hora',
                              bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
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
                            bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))
    self.lb_tecnico.place(relx=0.05, rely=0.32)
    self.tecnico_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.tecnico_entry.place(relx=0.05, rely=0.37,
                             relwidth=0.30, relheight=0.04)

    # Botão agendar
    self.bt_agendar = Button(
        self.frame_agenda, text='Agendar', bg='#F2F2F2', command=lambda: self.agendar(self))
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
        self.frame_agenda, orient='vertical', command=self.listaAgendamento.yview)
    self.listaAgendamento.configure(yscroll=self.scrollLista.set)
    self.scrollLista.place(relx=0.96, rely=0.5, relwidth=0.04, relheight=0.3)
    self.lb_codigo_consulta = Label(self.frame_agenda, text='Código',
                                    bg=FONT_BG, fg=FONT_COLOR, font=(FONT_TYPE, FONT_TAM, "bold"))

    self.lb_codigo_consulta.place(relx=0.05, rely=0.80)
    self.codigo_consulta_entry = Entry(
        self.frame_agenda, highlightbackground=FONT_BG, highlightthickness=1)
    self.codigo_consulta_entry.place(relx=0.05, rely=0.85,
                                     relwidth=0.30, relheight=0.04)

    self.bt_show_all = Button(
        self.frame_agenda, text='Mostrar Tudo', bg='#F2F2F2', command=lambda: show_table(self))
    self.bt_show_all.place(
        relx=0.06, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_limparAgenda = Button(
        self.frame_agenda, text='Limpar', bg='#F2F2F2', command=lambda: limpar(self))
    self.bt_limparAgenda.place(
        relx=0.29, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_funcaoFer = Button(
        self.frame_agenda, text='Consultar', bg='#F2F2F2', command=lambda: self.consulta_agendamento(self))
    self.bt_funcaoFer.place(
        relx=0.52, rely=0.9, relwidth=0.2, relheight=0.05)
    self.bt_devolver = Button(
        self.frame_agenda, text='Devolver', bg='#F2F2F2', command=lambda: devolucao(self))
    self.bt_devolver.place(
        relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)

# fuções dos calendarios


def calendario(self):
    self.calendario_retirada = Calendar(self.frame_agenda, locale='pt_br')
    self.calendario_retirada.place(relx=0.05, rely=0.27)
    self.calData_retirada = Button(
        self.frame_agenda, text='Inserir Data', command=lambda: print_cal_retirada(self))
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
        self.frame_agenda, text='Inserir Data', command=lambda: print_cal_devolucao(self))
    self.calData_devolucao.place(relx=0.55, rely=0.54, height=25, width=100)


def print_cal_devolucao(self):
    dataIni = self.calendario_devolucao.get_date()
    self.calendario_devolucao.destroy()
    self.devolucao1_entry.delete('0', 'end')
    self.devolucao1_entry.insert('end', dataIni)
    self.calData_devolucao.destroy()

# Função Mostrar Tudo


def show_table(self):
    limpar(self)

    with open('agenda.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        linhas = list(csv_reader)
        elemento_lista = False
        for lista in linhas:
            # if lista != linhas[0]:
            self.listaAgendamento.insert("", END, values=lista)
# Função Limpar


def limpar(self):
    for i in self.listaAgendamento.get_children():
        self.listaAgendamento.delete(i)

# Função Agendar


def agendar(self):
    self.codigo = self.codigo_entry.get()
    self.descricao = self.descricao_entry.get()

    self.retirada1 = self.retirada_entry1.get()
    self.retirada_hora = self.retirada_hora_entry.get()
    self.retirada = f"{self.retirada1} {self.retirada_hora}"

    self.devolucao1 = self.devolucao1_entry.get()
    self.devolucao_hora = self.devolucao_hora_entry.get()
    self.devolucao = f"{self.devolucao1} {self.devolucao_hora}"

    self.tecnico = self.tecnico_entry.get()
    with open('agenda.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        linhas = list(csv_reader)

    # with open("fer")
    ferramentas = []
    ferramenta = None
    with open('ferramentas.csv', 'r') as arquivo_ferramentas:
        reader = csv.reader(arquivo_ferramentas)
        for row in reader:
            ferramentas.append(row)
    ferramenta_em_lista = [
        item for item in ferramentas if item[0] == self.codigo and len(item)]
    if ferramenta_em_lista:
        ferramenta = ferramenta_em_lista[0]

    if not ferramenta:
        messagebox.showinfo(
            title="Atenção", message='Código de Ferramenta inválido')
        return
    # -------------------------------------------
    tecnicos = []
    tecnico = None
    with open('tecnicos.csv', 'r') as arquivo_tecnicos:
        reader = csv.reader(arquivo_tecnicos)
        for row in reader:
            tecnicos.append(row)
    tecnico_em_lista = [item for item in tecnicos if item[0]
                        == self.tecnico and len(item)]
    if tecnico_em_lista:
        tecnico = tecnico_em_lista[0]

    if not tecnico:
        messagebox.showinfo(title="Atenção", message='Técnico não cadastrado')
        return
    # ------------------------------------------=
    hoje = datetime.today()
    data_retirada = datetime.strptime(self.retirada, '%d/%m/%Y %H:%M')
    delta_retirada = data_retirada - hoje
    if delta_retirada < timedelta(days=1):
        messagebox.showinfo(
            title='Atenção', message='Agendamento com 24H de antecedencia')
        return
    data_devolucao = datetime.strptime(self.devolucao, '%d/%m/%Y %H:%M')
    delta_devolucao = data_devolucao - data_retirada
    tempo_agendamento = int(ferramenta[-3])
    if delta_devolucao > timedelta(hours=tempo_agendamento):
        messagebox.showinfo(
            title='Atenção', message=f'Máximo de agendamento {tempo_agendamento}H')
        return
    if delta_devolucao <= timedelta(minutes=0):
        messagebox.showinfo(title='Atenção', message='Agendamento Inválido')
        return

    # -------------------------------------------
    if int(ferramenta[-1]) == 0:
        messagebox.showinfo(title="Atenção", message="Não é possível agendar")
        return
    if (ferramenta[-2] == 'SIM') and int(ferramenta[-1]) <= 1:
        messagebox.showinfo(title="Atenção", message="Somente Emergência")
        return

    if (not self.codigo
        or not self.descricao
        or not self.retirada1
        or not self.retirada_hora
        or not self.retirada
        or not self.devolucao_hora
        or not self.devolucao1
        or not self.devolucao
        or not self.tecnico
        ):
        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')
        return
    else:
        self.codigo_entry.delete('0', 'end')
        self.descricao_entry.delete('0', 'end')
        self.retirada_entry1.delete('0', 'end')
        self.retirada_hora_entry.delete('0', 'end')
        self.devolucao1_entry.delete('0', 'end')
        self.devolucao_hora_entry.delete('0', 'end')
        self.tecnico_entry.delete('0', 'end')
        messagebox.showinfo(
            title="Atenção", message='Agendamento realizado com sucesso')
        with open('agenda.csv', 'a', newline='') as csvfile:
            fieldnames = ['codigo', 'descricao',
                          'retirada', 'devolucao', 'tecnico']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writer.writeheader()
            writer.writerow({'codigo': self.codigo, 'descricao': self.descricao,
                            'retirada': self.retirada, 'devolucao': self.devolucao, 'tecnico': self.tecnico})

        tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
        filename = 'ferramentas.csv'
        with open(filename, 'r', newline='') as arquivo_ferramentas_leitura, tempfile:
            fieldnames = [
                'codigo',
                'nome',
                'fabricante',
                'voltagem',
                'tamanho',
                'medida',
                'tipo',
                'material',
                'tempo',
                'critica',
                'quantidade'
            ]
            reader = csv.DictReader(
                arquivo_ferramentas_leitura, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for linha in reader:
                if linha['codigo'] == self.codigo:
                    linha['quantidade'] = int(linha['quantidade']) - 1
                linha = {
                    'codigo': linha['codigo'],
                    'nome': linha['nome'],
                    'fabricante': linha['fabricante'],
                    'voltagem': linha['voltagem'],
                    'tamanho': linha['tamanho'],
                    'medida': linha['medida'],
                    'tipo': linha['tipo'],
                    'material': linha['material'],
                    'tempo': linha['tempo'],
                    'critica': linha['critica'],
                    'quantidade': linha['quantidade']
                }
                writer.writerow(linha)
        shutil.move(tempfile.name, filename)


# função colsultar
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


def consulta_agendamento(self):
    entrada_codigo_consulta = self.codigo_consulta_entry.get()
    with open('agenda.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        linhas = list(csv_reader)
        if linhas_com_elementos := _linhas_no_arquivo(entrada_codigo_consulta, linhas):
            for linha in linhas_com_elementos:
                self.listaAgendamento.insert("", END, values=linha)
        else:
            messagebox.showinfo(title="Atenção", message='Não Encontrado')

# Função Devolução


def devolucao(self):
    # Deleta item da lista agenda
    try:
        item_selecionado = self.listaAgendamento.selection()[0]
        valores = self.listaAgendamento.item(item_selecionado, "values")
        self.listaAgendamento.delete(item_selecionado)

        # Apagar do arquivo csv
        lines = list()
        cod_ferramenta = valores[0]
        cpf_tecnico = valores[-1]

        with open('agenda.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                e_fer_selecionada = False
                for field in row:
                    if field == cod_ferramenta:
                        e_fer_selecionada = True
                    if field == cpf_tecnico and e_fer_selecionada:
                        lines.remove(row)

        with open('agenda.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    except:
        messagebox.showinfo(
            title="ERRO", message='Selecione um item a ser devolvido!')
        return

    # self.codigo_consulta = self.codigo_consulta_entry.get()
    # self.tecnico_devolver = self.tecnico_devolver_entry.get()
    with open('agenda.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        linhas = list(csv_reader)

  # ----------------------------------

    with open('agenda.csv', 'a', newline='') as csvfile:
        fieldnames = ['codigo', 'descricao',
                      'retirada', 'devolucao', 'tecnico']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
    filename = 'ferramentas.csv'
    with open(filename, 'r', newline='') as arquivo_ferramentas_leitura, tempfile:
        fieldnames = [
            'codigo',
            'nome',
            'fabricante',
            'voltagem',
            'tamanho',
            'medida',
            'tipo',
            'material',
            'tempo',
            'critica',
            'quantidade'
        ]
        reader = csv.DictReader(
            arquivo_ferramentas_leitura, fieldnames=fieldnames)
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
        for linha in reader:

            if linha['codigo'] == cod_ferramenta:
                linha['quantidade'] = int(linha['quantidade']) + 1
            linha = {
                'codigo': linha['codigo'],
                'nome': linha['nome'],
                'fabricante': linha['fabricante'],
                'voltagem': linha['voltagem'],
                'tamanho': linha['tamanho'],
                'medida': linha['medida'],
                'tipo': linha['tipo'],
                'material': linha['material'],
                'tempo': linha['tempo'],
                'critica': linha['critica'],
                'quantidade': linha['quantidade']
            }
            writer.writerow(linha)
    shutil.move(tempfile.name, filename)
    messagebox.showinfo(
        title="Atenção", message='Devolução realizada com sucesso')
