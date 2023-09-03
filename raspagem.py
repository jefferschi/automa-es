import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from selenium import webdriver # implementar o driver do navegador

# usando o webdriver-manager para não precisar instalar o driver específico do navegador manualmente.
from webdriver_manager.chrome import ChromeDriverManager # driver do navegador. pode alterar o navegador
from selenium.webdriver.chrome.service import Service # executa o webdriver manager

servico = Service(ChromeDriverManager().install()) # instala o driver no ambiente local

# Criar uma instância do WebDriver
navegador = webdriver.Chrome(service=servico) # roda o navegador

navegador.get('https://g1.globo.com/')
input('manter página aberta até uma informação do teclado')



# com bs4
"""
site_google = 'https://www.google.com.br/maps/'
site_g1 = 'https://g1.globo.com/'
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