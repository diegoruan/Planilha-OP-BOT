import pyautogui
import time
import usuario

def loopImagens(imagem, segundos, numeroConfidence):
    contador = 0
    segundosProg = segundos*4

    while contador < segundosProg:
        time.sleep(0.25)

        try:
            local = pyautogui.locateCenterOnScreen(imagem,confidence=numeroConfidence)
            contador = segundosProg
        except:
            contador += 1

    return local

def verificarAberto():
    try:
        loopImagens('.\\imagens\\img1.png', 2, 0.80)
    except:
        try:
            local3 = loopImagens('.\\imagens\\img3.png', 2, 0.80)
            pyautogui.moveTo(local3)
            pyautogui.click()
            loopImagens('.\\imagens\\img1.png', 5, 0.80)
        except:
            try:
                local8 = loopImagens('.\\imagens\\img8.png', 20, 0.98)
                pyautogui.moveTo(local8)
                pyautogui.click()

                pyautogui.write(usuario.login)
                pyautogui.press('tab')
                pyautogui.write(usuario.senha)
                pyautogui.press('enter')
            except:
                pyautogui.press('win')
                pyautogui.write('wk Radar')
                pyautogui.press('enter')

                local8 = loopImagens('.\\imagens\\img8.png', 50, 0.98)
                pyautogui.moveTo(local8)
                pyautogui.click()

                pyautogui.write(usuario.login)
                pyautogui.press('tab')
                pyautogui.write(usuario.senha)
                pyautogui.press('enter')