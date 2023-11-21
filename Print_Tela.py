# Importando bibliotecas
import pyautogui as py
import time

# Fechando o vscode movendo o cursor e simulando um clique
time.sleep(0.5)
py.moveTo(1249, 8)
py.click()
time.sleep(5)
x_y_1= py.position()
time.sleep(5)
x_y_2= py.position()


# arrasta a tela para baixo (quando os sites de fornecedores atualizavam após mudar a cor do produto)
"""
x_origem, y_origem = 1356, 216
x_destino, y_destino = 1356, 272
py.moveTo(x_origem, y_origem, duration=1)  
py.mouseDown()
py.moveTo(x_destino, y_destino, duration=1)  
py.mouseUp()
time.sleep(0.5)
"""

# Looping que simula o 'control' e ' Print Screen SysRq', afim de tirar print da tela repetidas vezes. 
for x in range(5):
    py.hotkey('ctrl', 'prtSc')

# seleciona os pontos para captura de tela e simula o mouse pressionando a tela até encontrar os pontos, formando prints de tamanhos idênticos
    x_origem, y_origem = x_y_1
    x_destino, y_destino = x_y_2
    py.moveTo(x_origem, y_origem, duration=1)  
    py.mouseDown()
    py.moveTo(x_destino, y_destino, duration=1)  
    py.mouseUp()
    time.sleep(5)

