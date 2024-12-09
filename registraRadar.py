import pyautogui
import time
from auxliar import loopImagens, verificarAberto

def registraRadar(df):
    listaRegistro = df
    pyautogui.PAUSE = 0.1

    verificarAberto()

    local1 = loopImagens('.\\imagens\\img1.png', 20, 0.80)

    pyautogui.moveTo(local1)
    pyautogui.click()
    pyautogui.write("registros da qualidade")
    loopImagens('.\\imagens\\img15.png', 20, 0.80)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

    for i, f in listaRegistro.iterrows():
        loopImagens('.\\imagens\\img12.png', 20, 0.80)
        pyautogui.press('tab')

        data = listaRegistro.iloc[i,1]

        pyautogui.write(data)
        pyautogui.press('tab')
        pyautogui.write('1.1.4.01.01')
        pyautogui.press('tab')
        pyautogui.press('tab')
        loopImagens('.\\imagens\\img13.png', 20, 0.80)

        identificacao = listaRegistro.iloc[i,0]

        pyautogui.write(identificacao)
        pyautogui.press('tab')

        hora = listaRegistro.iloc[i,2]

        pyautogui.write(hora)
        pyautogui.press('tab')
        local14 = loopImagens('.\\imagens\\img14.png', 20, 0.80)
        pyautogui.moveTo(local14)
        pyautogui.click()
        loopImagens('.\\imagens\\img17.png', 20, 0.80)
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')

        pyautogui.press('tab')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')

        valorCobre = listaRegistro.iloc[i,3]

        pyautogui.write(valorCobre)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')

        valorFos = listaRegistro.iloc[i,4]

        pyautogui.write(valorFos)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('tab')

        local2 = loopImagens('.\\imagens\\img2.png', 20, 0.50)

        pyautogui.moveTo(local2)
        pyautogui.click()
        pyautogui.press('tab')
        pyautogui.press('tab')

        pyautogui.press('tab')
        pyautogui.press('down')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

    pyautogui.hotkey('alt', 'f4')