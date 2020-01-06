import requests
from bs4 import BeautifulSoup
import re
import json

website = requests.get('https://www.marca.com/futbol/primera-division/calendario.html').text
soup = BeautifulSoup(website,'lxml')
jornadas = soup.findAll('table',{'class':'jor agendas'})
jornadas = soup.findAll('tbody')
counter = 0
temp_partido = []
temp_jornada = []
for jornada in jornadas:
    teams = jornada.findAll('span')
    partidos = []
    for team in teams:
        team = str(team)
        if ('equipo_' in team):
            temp_name = re.search('">(.*)</', team)
            temp_name = temp_name.group(1)
            counter += 1
            temp_partido.append(temp_name)
            if(counter == 2):
                partidos.append(temp_partido.copy())
                temp_partido = []
                counter = 0
    temp_jornada.append(partidos)
data_output = {}
contador = 1
for jornada in temp_jornada:
    data_output['Jornada-' + str(contador)] = []
    partido_contador = 0
    for partido in jornada:
        data_output['Jornada-' + str(contador)].append({})
        data_output['Jornada-' + str(contador)][partido_contador]['local'] = partido[0]
        data_output['Jornada-' + str(contador)][partido_contador]['visitante'] = partido[1]
        partido_contador += 1
    contador += 1
with open('matches.json', 'w') as fp:
    json.dump(data_output, fp)
