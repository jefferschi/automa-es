import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver # implementar o driver do navegador

# usando o webdriver-manager para não precisar instalar o driver específico do navegador manualmente.
from webdriver_manager.chrome import ChromeDriverManager # driver do navegador. pode alterar o navegador
from selenium.webdriver.chrome.service import Service # executa o webdriver manager

servico = Service(ChromeDriverManager().install()) # instala o driver no ambiente local

# Criar uma instância do WebDriver
navegador = webdriver.Chrome(service=servico) # roda o navegador

maps = 'https://www.google.com.br/maps/'
g1 = 'https://g1.globo.com/'
busca = 'restaurante, Cariacica - ES'

navegador.get(maps)

"""
copiar o xpath substitui copiar um elemento da página html, como uma classe, uma div, uma tag qualquer.
Para consegui-lo, ao inspecionar uma página, clicar com o botão inverso sobre a área desejada no código,
clicar em copy, e em XPath. 

"""
# encontra o elemento xpath do campo desejado. No lugar de xpath pode colocar outro atributo como class e id
elem_busca = navegador.find_element('xpath','//*[@id="searchboxinput"]')
elem_busca.click() # seleciona com um click o elemento buscado
elem_busca.send_keys(busca) # envia o texto digitado na variável ou por extenso dentro de aspas para o campo selecionado
elem_busca.send_keys(Keys.RETURN) # tecla Enter após digitar a busca

input('manter página aberta até uma informação do teclado')

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