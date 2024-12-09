import pyautogui
import time
import win32com.client
from datetime import datetime, timedelta
from auxliar import loopImagens, verificarAberto

def gerarRelatorios():
    pyautogui.PAUSE = 0.1

    verificarAberto()

    local1 = loopImagens('.\\imagens\\img1.png', 20, 0.80)

    pyautogui.moveTo(local1)
    pyautogui.click()
    pyautogui.write("registros da qualidade")
    loopImagens('.\\imagens\\img15.png', 20, 0.80)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
 
    loopImagens('.\\imagens\\img18.png', 20, 0.80)

    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    limpar = loopImagens('.\\imagens\\img7.png', 20, 0.80)
    pyautogui.moveTo(limpar)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('tab')

    dataFinal = datetime.now().date()
    dataInicial = dataFinal - timedelta(days=6*30)
    dataFinal = dataFinal.strftime("%d/%m/%Y")
    dataInicial = dataInicial.strftime("%d/%m/%Y")
    
    pyautogui.write(dataInicial)
    pyautogui.press('enter')
    pyautogui.write(dataFinal)
    local4 = loopImagens('.\\imagens\\img4.png', 20, 0.50)
    pyautogui.moveTo(local4)
    pyautogui.click()

    try:
        local5 = loopImagens('.\\imagens\\img5.png', 30, 0.80)
    except:
        local6 = loopImagens('.\\imagens\\img6.png', 5, 0.80)
        pyautogui.moveTo(local6)
        pyautogui.click()
        local5 = loopImagens('.\\imagens\\img5.png', 20, 0.80)

    pyautogui.moveTo(local5)
    pyautogui.click()
    loopImagens('.\\imagens\\img10.png', 30, 0.80)
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    
    excel = win32com.client.GetActiveObject("Excel.Application")
    workbook1 = excel.ActiveWorkbook
    workbook1.SaveAs("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\CUFtemp.xlsx")
    workbook1.Close()
    excel.Quit()
    del excel

    local1 = loopImagens('.\\imagens\\img1.png', 20, 0.80)
    pyautogui.moveTo(local1)
    pyautogui.click()
    pyautogui.write("interna")
    loopImagens('.\\imagens\\img16.png', 20, 0.80)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

    loopImagens('.\\imagens\\img18.png', 20, 0.80)

    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    limpar = loopImagens('.\\imagens\\img7.png', 20, 0.80)
    pyautogui.moveTo(limpar)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')

    dataFinal = datetime.now().date()
    dataInicial = dataFinal - timedelta(days=10)
    dataFinal = dataFinal.strftime("%d/%m/%Y")
    dataInicial = dataInicial.strftime("%d/%m/%Y")

    pyautogui.write(dataInicial)
    pyautogui.press('enter')
    pyautogui.write(dataFinal)
    local4 = loopImagens('.\\imagens\\img4.png', 20, 0.50)
    pyautogui.moveTo(local4)
    pyautogui.click()

    try:
        local5 = loopImagens('.\\imagens\\img5.png', 30, 0.80)
    except:
        local6 = loopImagens('.\\imagens\\img6.png', 5, 0.80)
        pyautogui.moveTo(local6)
        pyautogui.click()
        local5 = loopImagens('.\\imagens\\img5.png', 20, 0.80)

    pyautogui.moveTo(local5)
    pyautogui.click()
    loopImagens('.\\imagens\\img10.png', 30, 0.80)
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    excel = win32com.client.GetActiveObject("Excel.Application")
    workbook2 = excel.ActiveWorkbook
    workbook2.SaveAs("W:\\Laboratorio\\TUBOS\\Diversos\\Programas\\Arquivos_temp\\LOTEtemp.xlsx")
    workbook2.Close()
    excel.Quit()
    del excel
    pyautogui.hotkey('alt', 'f4')