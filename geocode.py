"""app para coletar geolocalização inserindo o endereço de forma rápida sem precisar acessar google maps"""


import pandas as pd
import geopy as gpd
from geopy.geocoders import Nominatim
import pymsgbox as pymb


endereco = pymb.prompt(text='digite o endereço completo')

if endereco == '':
    quit
else:
    localizador = Nominatim(user_agent="geocode")
    localizacao = localizador.geocode(endereco)
    
    print(localizacao.latitude,localizacao.longitude)
    
#endereco = 'Rua José Monteiro, 9 - Campo Grande, Cariacica - ES'

#-20.337939989407, -40.38909293784665

# o retorno é incompleto





