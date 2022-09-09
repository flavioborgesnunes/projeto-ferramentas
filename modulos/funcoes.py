from tkinter import messagebox, END
from csv import reader
from csv import writer
import csv

CAMINHO_SENHA_ENTRADA = './arquivos/senha_entrada.csv'


def cadastrar_ferramentas(self):
    self.descricao = self.descricao_entry.get().title()
    self.fabricante = self.fabricante_entry.get().title()
    self.voltagem = self.voltagem_entry.get()
    self.tamanho_1 = self.tamanho_entry_1.get()
    self.tamanho_2 = self.tamanho_entry_2.get()
    self.tamanho = f"{self.tamanho_1} X {self.tamanho_2}"
    self.unidade_medida = self.unidade_entry.get()
    self.tipo_ferramenta = self.tipo_entry.get()
    self.material_ferramenta = self.material_entry.get().title()
    self.tempo_reserva = self.tempo_entry.get()
    self.critica = self.critica_entry.get()
    self.quantidade = self.quantidade_entry.get()
    # validação
    try:
        with open('./arquivos/ferramentas.csv', 'r') as csv_file:
            csv_reader = reader(csv_file)
            # Passing the cav_reader object to list() to get a list of lists
            linhas = list(csv_reader)
            codigo = int(linhas[-1][0])

    except IndexError:
        codigo = 0

    if not self.descricao \
       or not self.fabricante \
       or not self.voltagem \
       or (self.voltagem == 'SELECIONE') \
       or not self.tamanho_1 \
       or not self.tamanho_2 \
       or not self.unidade_medida \
       or not self.tipo_ferramenta \
       or (self.tipo_ferramenta == 'SELECIONE') \
       or not self.material_ferramenta \
       or not self.tempo_reserva \
       or not self.critica \
       or (self.critica == 'SELECIONE') \
       or not self.quantidade:

        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')

    else:
        codigo += 1
        self.descricao_entry.delete('0', 'end')
        self.fabricante_entry.delete('0', 'end')
        self.voltagem_entry.delete('0', 'end')
        self.tamanho_entry_1.delete('0', 'end')
        self.tamanho_entry_2.delete('0', 'end')
        self.unidade_entry.delete('0', 'end')
        self.tipo_entry.delete('0', 'end')
        self.material_entry.delete('0', 'end')
        self.tempo_entry.delete('0', 'end')
        self.critica_entry.delete('0', 'end')
        self.quantidade_entry.delete('0', 'end')
        messagebox.showinfo(
            title="Atenção",
            message='O código da ferramenta é: ' + str(f'{codigo:04}')
        )

        with open('./arquivos/ferramentas.csv', 'a', newline='') as csvfile:
            fieldnames = ['codigo', 'Descricao', 'Fabricante',
                          'Voltagem', 'Tamanho', 'Unidade_de_Medida',
                          'Tipo', 'Material',
                          'tempo_reserva', 'critica', 'quantidade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writer.writeheader()
            writer.writerow({'codigo': str(f'{codigo:04}'),
                            'Descricao': self.descricao.title(),
                             'Fabricante': self.fabricante.title(),
                             'Voltagem': self.voltagem,
                             'Tamanho': self.tamanho,
                             'Unidade_de_Medida': self.unidade_medida.title(),
                             'Tipo': self.tipo_ferramenta.title(),
                             'Material': self.material_ferramenta.title(),
                             'tempo_reserva': self.tempo_reserva,
                             'critica': self.critica,
                             'quantidade': self.quantidade})


def cadastrar_Tec(self):

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

    if not self.cpf \
       or not self.nome \
       or not self.telefone \
       or not self.turno \
       or not self.equipe:

        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')
        return
    else:
        self.cpf_entry.delete('0', 'end')
        self.nome_entry.delete('0', 'end')
        self.telefone_entry.delete('0', 'end')
        self.turno_entry.delete('0', 'end')
        self.equipe_entry.delete('0', 'end')

        with open('./arquivos/tecnicos.csv', 'a', newline='') as csvfile:
            fieldnames = ['cpf', 'nome', 'telefone', 'turno', 'equipe']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writer.writeheader()
            writer.writerow(
                {
                    'cpf': self.cpf,
                    'nome': self.nome,
                    'telefone': self.telefone,
                    'turno': self.turno,
                    'equipe': self.equipe
                }
            )
        messagebox.showinfo(
            title="Atenção", message='Cadastro realizado com sucesso')


def mostrar_tudo(lista, arquivoCsv):
    limpar(lista)
    with open(arquivoCsv, 'r') as csv_file:
        csv_reader = reader(csv_file)
        linhas = list(csv_reader)
        for item in linhas:
            lista.insert("", END, values=item)


def limpar(lista):
    for i in lista.get_children():
        lista.delete(i)


def consultar(lista, entrada, arquivoCsv):
    limpar(lista)
    entrada_codigo = entrada.get()
    with open(arquivoCsv, 'r') as csv_file:
        csv_reader = reader(csv_file)
        arquivo = list(csv_reader)
        encontrado = False
        for linhas in arquivo:
            definitiva = linhas
            for item in definitiva:
                if item == entrada_codigo:
                    encontrado = True
                    lista.insert("", END, values=definitiva)
        if not encontrado:
            messagebox.showinfo(title="Atenção", message='Não Encontrado')


def excluir(lista, arquivoCsv):
    try:
        item_selecionado = lista.selection()[0]
        valores = lista.item(item_selecionado, "values")
        MsgBox = messagebox.askquestion(
            title='Atenção', message='Deseja Exlcuir ?', icon='error')
        if MsgBox == 'yes':
            lista.delete(item_selecionado)
            messagebox.showinfo(title="Atenção", message='Item deletado!')
            # Apagar do arquivo csv
            lines = list()
            members = valores[0]
            with open(arquivoCsv, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == members:
                            lines.remove(row)
            with open(arquivoCsv, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
        else:
            return
    except IndexError:
        messagebox.showinfo(
            title="ERRO", message='Selecione um item a ser deletado!')


def cadastrar_login(self):

    self.user_cadastro = self.entry_user_cadastro.get()
    self.senha_cadastro = self.entry_senha_cadastro.get()
    if (not self.user_cadastro or not self.senha_cadastro):
        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')
        return
    self.entry_user_cadastro.delete('0', 'end')
    self.entry_senha_cadastro.delete('0', 'end')

    with open(CAMINHO_SENHA_ENTRADA, 'r') as file:
        csv_reader = reader(file)
        linhas = str(csv_reader)
        msg3 = False
        for lista in linhas:
            if self.user_cadastro == lista[0]:
                msg3 = True
        if msg3:
            messagebox.showinfo(
                title="Atenção", message='Usuário já cadastrado')

        else:
            with open(CAMINHO_SENHA_ENTRADA, 'a', newline='') as csvfile2:
                writer_object = writer(csvfile2)
                list_data = [self.user_cadastro, str(self.senha_cadastro)]
                writer_object.writerow(list_data)
                messagebox.showinfo(
                    title="Atenção", message='Novo usuário cadastrado')
                csvfile2.close()


def excluir_user(self):

    self.user_cadastro = self.entry_user_cadastro.get()
    self.senha_cadastro = self.entry_senha_cadastro.get()
    if (not self.user_cadastro or not self.senha_cadastro):
        messagebox.showinfo(
            title="Atenção", message='Preencha todos os Campos')
        return

    MsgBox = messagebox.askquestion(
        title='Atenção', message='Deseja Exlcuir ?', icon='error')
    if MsgBox == 'yes':

        lines = list()
        compara = [self.user_cadastro, self.senha_cadastro]
        verifica_cadastro = False
        with open(CAMINHO_SENHA_ENTRADA, 'r') as file:
            csv_reader = csv.reader(file)
            for lista in csv_reader:
                lines.append(lista)
                if lista == compara:
                    verifica_cadastro = True
                    lines.remove(lista)
                    messagebox.showinfo(
                        title='Atenção', message='Usuário Deletado')

        with open(CAMINHO_SENHA_ENTRADA, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        if not verifica_cadastro:
            messagebox.showinfo(
                title="Atenção", message='Usuário não cadastrado')

    else:
        return
