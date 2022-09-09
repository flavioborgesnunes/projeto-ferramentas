from calendar import calendar
from tkinter import *
from tkinter import messagebox
import csv
from csv import reader
import shutil
from tempfile import NamedTemporaryFile
from datetime import datetime, timedelta
from modulos.funcoes import *


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
    with open('./arquivos/ferramentas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        arquivo = list(csv_reader)
        encontrado = False
        for linhas in arquivo:
            definitiva = linhas
            for item in definitiva:
                if item == self.codigo:
                    encontrado = True
                    ferramenta = definitiva
        if encontrado == False:
            messagebox.showinfo(
                title="Atenção", message='Código de ferramenta Inválido')
            return

    with open('./arquivos/tecnicos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        arquivo = list(csv_reader)
        encontrado = False
        for linhas in arquivo:
            definitiva = linhas
            for item in definitiva:
                if item == self.tecnico:
                    encontrado = True
        if encontrado == False:
            messagebox.showinfo(
                title="Atenção", message='Técnico não cadastrado')
            return

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

    if int(ferramenta[-1]) == 0:
        messagebox.showinfo(title="Atenção", message="Não é possível agendar")
        return
    if (ferramenta[-2] == 'SIM') and int(ferramenta[-1]) <= 1:
        messagebox.showinfo(title="Atenção", message="Somente Emergência")
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

        with open('./arquivos/agenda.csv', 'a', newline='') as csvfile:
            fieldnames = ['codigo', 'descricao',
                          'retirada', 'devolucao', 'tecnico']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'codigo': self.codigo, 'descricao': self.descricao,
                            'retirada': self.retirada, 'devolucao': self.devolucao, 'tecnico': self.tecnico})

        lines = list()
        members = ferramenta
        with open('./arquivos/ferramentas.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
            for busca_ferramenta in lines:
                if busca_ferramenta == members:
                    modificada = int(busca_ferramenta[-1]) - 1
                    busca_ferramenta[-1] = modificada

        with open('./arquivos/ferramentas.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)


# Função Devolução


def devolver(self):
    # Deleta item da lista agenda
    try:
        item_selecionado = self.listaAgendamento.selection()[0]
        valores = self.listaAgendamento.item(item_selecionado, "values")
        self.listaAgendamento.delete(item_selecionado)

        # Apagar do arquivo csv
        lines = list()
        cod_ferramenta = valores[0]
        cpf_tecnico = valores[-1]

        with open('./arquivos/agenda.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                e_fer_selecionada = False
                for field in row:
                    if field == cod_ferramenta:
                        e_fer_selecionada = True
                    if field == cpf_tecnico and e_fer_selecionada:
                        lines.remove(row)

        with open('./arquivos/agenda.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

  # ----------------------------------

        lines2 = list()
        with open('./arquivos/ferramentas.csv', 'r') as readFile2:
            reader2 = csv.reader(readFile2)
            for row in reader2:
                lines2.append(row)
            for busca_ferramenta in lines2:
                ferramenta_encontrada = busca_ferramenta
                for busca_cod in ferramenta_encontrada:
                    if busca_cod == cod_ferramenta:
                        modificada = int(busca_ferramenta[-1]) + 1
                        busca_ferramenta[-1] = modificada

        with open('./arquivos/ferramentas.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines2)

        messagebox.showinfo(
            title="Atenção", message='Devolução realizada com sucesso')

    except:
        messagebox.showinfo(
            title="ERRO", message='Selecione um item a ser devolvido!')
        return
