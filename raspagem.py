import requests
from time import sleep

from bs4 import BeautifulSoup as bs
import pandas as pd

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver # implementar o driver do navegador

# configuraçõs do navegador. usando o webdriver-manager para não precisar instalar o driver específico do navegador manualmente.
from webdriver_manager.chrome import ChromeDriverManager # driver do navegador. pode alterar o navegador
from selenium.webdriver.chrome.service import Service # executa o webdriver manager
from selenium.webdriver.chrome.options import Options # servirá para configurar tamanho da janela do navegador

class Raspagem:

  def __init__(self):
    self.inicia_nav()
    self.encontra_elem()
    self.interromper()
    

  def inicia_nav(self):
        
    # usa opções para definir tamanho da tela
    opcoes = Options()
    #opcoes.add_argument('headless') # faz com que o navegador fique oculto.
    opcoes.add_argument('window-size=1350,700')

    servico = Service(ChromeDriverManager().install()) # instala o driver no ambiente local

    # Criar uma instância do WebDriver
    self.navegador = webdriver.Chrome(service=servico, options=opcoes) # roda o navegador

    self.pagina = 'https://www.google.com.br/maps/'
    self.busca = 'restaurante, Cariacica - ES'

    self.navegador.get(self.pagina) # abre a página desejada

    sleep(2) # tempo para que a página renderize e não corra o risco de o texto ser "digitado" antes


  def encontra_elem(self):
      
    # encontra o elemento xpath do campo desejado. No lugar de xpath pode colocar outro atributo como class e id
    elem_busca = self.navegador.find_element('xpath','//*[@id="searchboxinput"]')
    elem_busca.click() # seleciona com um click o elemento buscado
    elem_busca.send_keys(self.busca) # envia o texto digitado na variável ou por extenso dentro de aspas para o campo selecionado
    elem_busca.send_keys(Keys.RETURN) # tecla Enter após digitar a busca

    sleep(3) # tempo para que a página renderize e não corra o risco de não renderizar todo o conteúdo buscado.
    page_busca = self.navegador.page_source # pega o caminho da página buscada
    page_conteudo = bs(page_busca,'html.parser') # pega o conteudo html do caminho retornado no navegador

    print(page_conteudo.prettify()) # imprime o código com identação padrão html

  def interromper(self):
    input('pressione alguma tecla para interromper') # precisei colocar pois a página não permanecia aberta após rodar o script

r = Raspagem()

# com bs4
"""

# find(tag, atributo)
# procura com a tag pela notícia
noticias = conteudo_site.findAll(name='div',attrs={'class':'feed-post-body'})


for noticia in noticias:
  # procura com a tag pelo título e imprime o texto titulo
  #feed-post-body-resumo
  titulo = noticia.find(name='a',attrs={'class':'feed-post-link'})
  subtitulo = noticia.find(name='div',attrs={'class':'feed-post-body-resumo'})

  #text busca o texto do atributo da variável
  print()
  print('titulo: ',titulo.text)

  # verifica se existe subtitulo e o imprime
  if (subtitulo):
    print('subtitulo: ',subtitulo.text)

  link = titulo['href'] #pega o link da noticia
  if (link):
    print('link: ',link)
  else:
    print()
"""