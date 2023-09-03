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

# usa opções para definir tamanho da tela
opcoes = Options()
#opcoes.add_argument('headless') # faz com que o navegador fique oculto.
opcoes.add_argument('window-size=1350,700')

servico = Service(ChromeDriverManager().install()) # instala o driver no ambiente local

# Criar uma instância do WebDriver
navegador = webdriver.Chrome(service=servico, options=opcoes) # roda o navegador

pagina = 'https://www.google.com.br/maps/'
busca = 'restaurante, Cariacica - ES'

navegador.get(pagina) # abre a página desejada

sleep(3) # tempo para que a página renderize e não corra o risco de o texto ser "digitado" antes

# encontra o elemento xpath do campo desejado. No lugar de xpath pode colocar outro atributo como class e id
elem_busca = navegador.find_element('xpath','//*[@id="searchboxinput"]')
elem_busca.click() # seleciona com um click o elemento buscado
elem_busca.send_keys(busca) # envia o texto digitado na variável ou por extenso dentro de aspas para o campo selecionado
elem_busca.send_keys(Keys.RETURN) # tecla Enter após digitar a busca



page_busca = bs(navegador.page_source,'html.parser')

print(page_busca.prettify())


input('pressione alguma tecla para interromper') # precisei colocar pois a página não permanecia aberta após rodar o script

"""
proximos passos:
pegar a url do retorno encontrado com a pesquisa, capturar o conteudo da página,
localizar os atributos que preciso e buscar os seus respectivos textos.

colocar em um lista e depois vem o tratamento em pandas


"""

# com bs4
"""

req_response = requests.get(site_g1)
conteudo = req_response.content

# usando o metodo beautifullsoup
conteudo_site = bs(conteudo,'html.parser')

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