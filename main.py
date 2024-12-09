import flet as ft
import pandas as pd
import pyautogui
from datetime import datetime
from gerarRelatorios import gerarRelatorios
from registraRadar import registraRadar
from organizaPlanilha import organizar
from juntarPlanilhas import juntarPlanilhas

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 620
    page.window_resizable = False
    tabelaResultados = pd.DataFrame(columns=['Identificação', 'Data', 'Horário', 'Cobre', 'Fósforo'])

    def completo(evento):
        page.remove(paginaInicial)
        page.add(paginaLancamento1, paginaLancamento2)

    def lancamento(evento):
        page.remove(paginaInicial)
        page.add(paginaLancamento1, paginaLancamento3)

    def atualizarPlanilha(evento):
        page.remove(paginaInicial)
        page.add(textoAguardando)
        pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
        gerarRelatorios()
        organizar()
        pyautogui.alert('Verifique se a planilha de OP não esta aberta!')
        juntarPlanilhas()
        pyautogui.alert('O código finalizou!')
        page.remove(textoAguardando)
        page.add(textoFinalizado)

    def gravar(evento):
        formato = "%d/%m/%Y"
        try:
            datetime.strptime(campoData.value, formato)
        except ValueError:
            page.dialog = popupDataErro
            popupDataErro.open = True
            page.update()
            return()
        
        if campoCobre.value < "99,90" or campoFosforo.value < "0,015" or campoFosforo.value > "0,04":
            page.dialog = popupValoresErros
            popupValoresErros.open = True
            page.update()
            return()
        
        tabelaResultados.loc[len(tabelaResultados)] = [campoIdentificacao.value, campoData.value, campoHorario.value, campoCobre.value, campoFosforo.value]
        campoIdentificacao.value = ""
        campoHorario.value = ""
        campoCobre.value = ""
        campoFosforo.value = ""
        print(tabelaResultados)
        page.update()

    def remover(evento):
        nonlocal tabelaResultados
        tabelaResultados = tabelaResultados.drop(tabelaResultados.index[-1])
        print(tabelaResultados)
        page.update()

    def confirmar(evento):
        tabelaResultados.loc[len(tabelaResultados)] = [campoIdentificacao.value, campoData.value, campoHorario.value, campoCobre.value, campoFosforo.value]
        campoIdentificacao.value = ""
        campoHorario.value = ""
        campoCobre.value = ""
        campoFosforo.value = ""
        popupValoresErros.open = False
        print(tabelaResultados)
        page.update()

    def lancarResultadosComleto(evento):
        page.remove(paginaLancamento1, paginaLancamento2)
        page.add(textoAguardando)
        pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
        registraRadar(tabelaResultados)
        gerarRelatorios()
        organizar()
        pyautogui.alert('Verifique se a planilha de OP não esta aberta!')
        juntarPlanilhas()
        pyautogui.alert('O código finalizou!')
        page.remove(textoAguardando)
        page.add(textoFinalizado)

    def lancarResultados(evento):
        page.remove(paginaLancamento1, paginaLancamento3)
        page.add(textoAguardando)
        pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
        registraRadar(tabelaResultados)
        pyautogui.alert('O código finalizou!')
        page.remove(textoAguardando)
        page.add(textoFinalizado)

    botaoCompleto = ft.ElevatedButton("Completo", on_click=completo, width=200)
    botaoLancar = ft.ElevatedButton("Lançar Cobre/Fósforo", on_click=lancamento, width=200)
    botaoPlanilha = ft.ElevatedButton("Atualizar Planilha", on_click=atualizarPlanilha, width=200)
    paginaInicial = ft.Column([botaoCompleto, botaoLancar, botaoPlanilha], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    textoLancamento = ft.Text("Resultados do teor de cobre/fósforo")
    campoIdentificacao = ft.TextField(label="Identificação", width=200)
    campoData = ft.TextField(label="Data", width=200)
    campoHorario = ft.TextField(label="Horário", width=200)
    campoCobre = ft.TextField(label="Cobre", width=200)
    campoFosforo = ft.TextField(label="Fósforo", width=200)
    botaoAdicionar = ft.ElevatedButton("Adicionar", on_click=gravar, width=150, height=40)
    botaoConcluir1 = ft.ElevatedButton("Concluir", on_click=lancarResultadosComleto, width=150, height=40)
    botaoConcluir2 = ft.ElevatedButton("Concluir", on_click=lancarResultados, width=150, height=40)
    botaoRemover = ft.ElevatedButton("Remover Ultimo Lançamento", on_click=remover, width=240, height=40)
    popupDataErro = ft.AlertDialog(open=False, modal=False,title=ft.Text("Data incorreta!"))
    popupValoresErros = ft.AlertDialog(open=False, modal=False,title=ft.Text(f'Você confirma os valores de cobre e fosforo?'), actions=[ft.ElevatedButton("Confirmar", on_click=confirmar)])
    paginaLancamento1 = ft.Column([textoLancamento, campoIdentificacao , campoData, campoHorario, campoCobre, campoFosforo], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    paginaLancamento2 = ft.Column([botaoAdicionar, botaoConcluir1, botaoRemover], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    paginaLancamento3 = ft.Column([botaoAdicionar, botaoConcluir2, botaoRemover], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    textoAguardando = ft.Text("Aguarde Finalizar!")
    textoFinalizado = ft.Text("Programa Finalizado!")

    page.add(paginaInicial)
    page.update()

ft.app(target=main)