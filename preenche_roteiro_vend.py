import pyautogui as pyag
import pymsgbox as msg


def preenche_rota():
    """ Preenche a sequencia de atendimento da rota. Colocar a relação dos clientes do último para o primeiro em
    ordem de atendimeto.
    """
    pyag.PAUSE = 0.15

    qtd_cli = int(msg.prompt(text='Quantidade de clientes da rota: ', title='Preencha'))
    cont = 0

    pyag.alert('vai começar')
    pyag.click(x=639, y=286,interval=0.25) #clica na tela do erp
    pyag.hotkey('alt','tab')
    pyag.click(x=63, y=236,interval=0.25) # seleciona A1 na planilha

    while cont < qtd_cli: 
        pyag.hotkey('ctrl','c')
        pyag.hotkey('alt','tab') #volta para erp
        pyag.click(x=228, y=253,interval=0.25) #posiciona sobre a entrada do código do cliente
        pyag.hotkey('ctrl','v')
        pyag.click(x=523, y=253)
        pyag.hotkey('alt','tab')
        pyag.press('right')
        pyag.write('x')
        pyag.press('down')
        pyag.press('home')
        cont += 1

        if cont == qtd_cli:
            msg.alert('preenchido!')
            quit
    


alerta1 = msg.confirm(text="1- Fique na tela CRIAÇÃO DO ROTEIRO DE VISITA \n"
"2- Deixe selecionado o vendedor e o dia do roteiro \n3- Deixe alternada a tela da planilha com os códigos",
    buttons=['Ok','Cancelar'], title='ATENÇÃO!')

if alerta1 == 'Ok':
    preenche_rota()
else:
    print('sair')
    quit




# posições do mouse na tela criação roteiro de visita
# (x=468, y=211) -> posição vendedor
# (x=228, y=253) -> posição cliente
# (x=523, y=253) -> cliente seta baixo
# (x=665, y=251) -> frequencia
# (x=685, y=255) -> frequencia seta baixo
# (x=750, y=253) -> hora inicio
# (x=814, y=250) -> intervalo
# (x=842, y=252) -> intervalo seta baixo
# (x=1091, y=251) -> sequencia automatica
# (x=763, y=210) -> avança dia