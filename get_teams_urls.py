#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def getTeamsURL():

    short_url = 'https://www.bdfutbol.com/es/t/'
    website = requests.get('https://www.bdfutbol.com/es/t/t2019-20.html').text
    soup = BeautifulSoup(website,'lxml')

    teams = soup.find('table',{'class':'taula_estil sortable'})
    allTeams = []
    teams1 = teams.findAll('tr', {'class': 'CHA'})
    teams2 = teams.findAll('tr', {'class': 'UEF'})
    teams3 = teams.findAll('tr', {'class': 'res'})
    teams4 = teams.findAll('tr', {'class': 'prom_baixa'})

    for team in teams1:
        allTeams.append(team)

    for team in teams2:
        allTeams.append(team)

    for team in teams3:
        allTeams.append(team)

    for team in teams4:
        allTeams.append(team)

    urls = []
    names = []
    managers = []
    for team in allTeams:
        url = str(team.findAll('a'))
        temp_url = re.search('/t/(.*)html', url)
        urls.append('https://www.bdfutbol.com/es/t/' + temp_url.group(1))
        temp_name = re.search('">(.*)</', url)
        names.append(temp_name.group(1))

    if not os.path.exists('./data/'):
        os.makedirs('./data')

    dfTeamsData = pd.DataFrame(data={'URL': urls, 'Team': names})
    dfTeamsData.to_csv('./data/teams.csv', sep= ';')

    return urls
