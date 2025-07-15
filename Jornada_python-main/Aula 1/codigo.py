# PASSO 1 - Acessar o sistema da empresa
# link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Para utilizar o autoGui, é necessário instalar com Py (pip install pyautogui)
# Em pyautogui no Google, é possível obter a documentação de apoio

import pyautogui
import time
import pandas as pd

#pyautogui.write -> escrever texto
#pyautogui.click -> clicar com o mouse
#pyautogui.press -> pressiona alguma tecla
#pyautogui.hotkey -> apertar atalho de teclado (ctrl, C)
#pyautogui.press("enter")
#pyautogui.press("ctrl")
# para o mac, pyautogui.hotkey("command", "enter")
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#pyautogui.PAUSE = 0.5 - pausa entre cada comando
#dar pausa após um comando específico
time.sleep(0.5)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")


# PASSO 2 - Fazer login - qualquer email e qualquer senha

time.sleep(1.0)
pyautogui.click(x=426, y=24, clicks=2)

pyautogui.click(x=500, y=400)
pyautogui.write("qualqueremail@dominio.com")
# time.sleep(0.5)
# pyautogui.click(x=492, y=506)
# pyautogui.write("Alguma senha")
# ou, para passar para o próximo,
pyautogui.press("tab")
pyautogui.write("Alguma senha")

time.sleep(0.3)
pyautogui.click(x=643, y=561)

time.sleep(1)

# PASSO 3 - Importar base de dados

tabela = pd.read_csv("auxiliares/produtos.csv")
print(tabela)

# PASSO 4: Cadastrar 1 produto

# PASSO 5: Repetir passo 4 até acabarem os produtos
#para cada linha na tabela, executar
for linha in tabela.index:

    pyautogui.click(x=474, y=293)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    #verifica se está vazia a observação
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    #pyautogui.scroll(5000)
    pyautogui.press("home")
    time.sleep(0.2)
