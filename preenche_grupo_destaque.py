import pyautogui as pyag
import pymsgbox as pymsg


"""preenche o campo grupo de destaque do cadastro de clientes da aba Complemento a partir de uma 
planilha. Preencher por estrela e acertar a quantidade de downs clicks para escolher o grupo
"""
pyag.PAUSE = 0.3

qtd_cli = pymsg.prompt(text='Digite a quantidade de clientes')
estrelas = pymsg.prompt(text='Digite a quantidade de estrelas')

cont = 0

confirma = pymsg.confirm(text='%s clientes a fazer. \nVai começar! \nFique na tabela excel, com a tela de cadastro de cliente alternada'%qtd_cli,
buttons=['Ok','Cancelar'])

if confirma == 'Cancelar':
    quit()

elif confirma == 'Ok':

    pyag.click(x=63,y=267, interval=0.3) #seleciona A2 na tabela
    pyag.click(x=63,y=267, interval=0.15)


    pyag.hotkey('ctrl','c') #copia cod cliente da tabela
    pyag.hotkey('alt','tab') #alterna para tela de cadastro do cliente no target

    while int(qtd_cli) > cont:

        pyag.doubleClick(x=334, y=136) # cod cliente target
        pyag.hotkey('ctrl','v')
        pyag.hotkey('tab')
        pyag.hotkey('alt','a')

        pyag.click(x=964, y=432) #seleciona a aba Complemento
        
        pyag.click(x=790, y=481, interval=0.15) #seleciona o campo grupo de destaque
        pyag.press('home') #vai para o topo da combobox

        pyag.press('down', presses=int(estrelas)) #seleciona a opção desejada (estrelas) do grupo destaque
        pyag.hotkey('tab')
        pyag.hotkey('alt','e')
        pyag.hotkey('alt','o', interval=0.1)


        pyag.hotkey('alt','tab') #retorna para a tabela
        pyag.press('right', presses=2)
        pyag.write('x') #registro X no cliente como feito 
        pyag.press('down')
        pyag.press('home')
        pyag.hotkey('ctrl','c')

        pyag.hotkey('alt','tab')# retorna ao target
        
        cont += 1


#posição grupo destaque (x=790, y=481)
#posição celula A2 (x=63, y=267)



