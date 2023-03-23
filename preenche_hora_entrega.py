
import pyautogui as pyag
import pymsgbox as pyb

# para colcoar para a planilha, adicionar um prompt para informar a quantidade de clientes que irá fazer a ação



# preenche um quantidade clientes informado pelo usuário com horario inicio e fim a partir de uma planilha


def preenche_plan():    
    """ Automação para o preenchimento do horário de entrega dos clientes no cadastro ERP
    Target. Caminho no ERP -> Vendas -> Operacionais -> Cadastros -> Clientes -> Cadastro
    
    Usuário informa a quantidade de clientes da lista que quer preencher, deve deixar a tela de cadastro de clientes aberta, 
    alternando com a planilha de dados.
    A planilha de cliente deve contar as informações na seguinte ordem: códido do cliente, hora início, hora fim

    """
    cont_cli = 0
    

    while int(qtd_cli) > cont_cli:     

        pyag.PAUSE = 0.15
         
        pyag.hotkey('alt','tab',interval=0.1)
        pyag.doubleClick(x=334, y=136) # cod cliente target
        pyag.hotkey('ctrl','v')
        pyag.press('tab')
        
        pyag.hotkey('alt','g') # abre guia entrega
        pyag.click(x=1041, y=504) # botão horario recebimento
        pyag.hotkey('alt','g',interval=0.1) #gera horário padrão
        pyag.hotkey('alt','s', interval=0.1)
        
        pyag.hotkey('alt','tab',interval=0.1)
        pyag.press('right', presses=2)
        pyag.hotkey('ctrl','c', interval=0.1) #pega horario inicio planilha

        pyag.hotkey('alt','tab', interval=0.1)
        pyag.doubleClick(x=628, y=411) # clique duplo sobre primeiro horário inicio no erp
    
        desce1 = 0 # loop para hora inicio
        while desce1 < 7:       
            pyag.hotkey('ctrl','v')
            pyag.press('down')
            desce1 += 1

        
        pyag.hotkey('alt','tab')
        pyag.press('right')
        pyag.hotkey('ctrl','c', interval=0.1) # pega horario fim planilha
       
        pyag.hotkey('alt','tab', interval=0.1)
        pyag.doubleClick(x=688, y=408) # sobre primeiro horário fim

        desce2 = 0 # loop para hora fim
        while desce2 < 7:
            pyag.hotkey('ctrl','v')
            pyag.press('down')
            desce2 += 1
            
        pyag.click(x=842, y=500) # salva horarios
        pyag.click(x=901, y=218, interval=0.1) # fecha tela horarios

        cont_cli += 1
       
        pyag.hotkey('alt','tab',interval=0.1)
        pyag.press('right', presses=2)
        pyag.write('x')
        pyag.press('down')
        pyag.press('home')
        pyag.hotkey('ctrl','c') # pega próximo cod cliente

        if  int(qtd_cli) == cont_cli:
            pyb.alert(text='preenchido')
            exit

# preenche um cliente por vez com horario inicio e fim informado pelo usuário
def preenche():
    """ Usuário deve estar na tela de agendamento do recebimento do cliente específio. Irá fornecer a hora início e
    hora fim de recebimento do mesmo.
    """
    pyag.PAUSE = 0.15

    cont = 0
    inicio = pyb.prompt(text='hora início',title='inicio')
    fim = pyb.prompt(text='hora fim',title='fim')
    pyag.doubleClick(x=628, y=411) # sobre primeiro horário inicio

    while cont < 7:
        pyag.write(inicio)
        pyag.press('tab')
        pyag.write(fim)
        pyag.press('tab', presses=3)
            
        cont += 1

    if cont == 7:
        pyag.click(x=842, y=500)
        alerta2 = pyb.confirm(text='Continuar próximo cliente?',buttons=['Sim','Não'],title='ALERTA!')
        if alerta2 == 'Sim':
            preenche()
        else:
            exit
            

"""primeira tela para definir qual meio de preenchimento dos dados será usado: lista de clientes
em uma planilha ou o usuário informar apenas os horários já na tela do cliente específico.
"""    

meio = pyb.confirm(text='preenche pela planilha?',buttons=['sim','não'],title='ALERTA!!!',)

if meio == 'não':
    alerta1 = pyb.confirm(text='Fique na tela horario de recebimento',title='ALERTA!',buttons=['Ok','Cancelar'])
    
    if alerta1 == 'Ok':
        preenche()
    else:
        exit
else:
    
    alerta1 = pyb.confirm(text='fique na tela da planilha e deixe a tela cadastro aberta',title='ALERTA!',buttons=['Ok','Cancelar'])
    
    if alerta1 == 'Ok':
        
        qtd_cli = pyb.prompt(text='qtd clientes',title='clientes da planilha')
        pyag.alert('vai começar')
        
        pyag.PAUSE = 0.5

        pyag.click(x=58, y=253,interval=0.25) # célula A2 planilha
        pyag.click(x=58, y=253,interval=0.25) 
        pyag.hotkey('ctrl','c',interval=0.25) 
        

        pyb.confirm(text='Continuar?',buttons=['sim','nao'])

        preenche_plan()
    else:
        exit


#pyag.click(x=53, y=235) #posiciona excel célula A1
#pyag.sleep(3)
#print(pyag.position())
#pyag.click(resultado do position)
