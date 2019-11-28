#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def getPlayersData(urls: [], teams: []):
    index = 0
    if not os.path.exists('./data/teams/'):
        os.makedirs('./data/teams')

    for url in urls:
        playerList = list()
        print(url)

        website = requests.get(url + 'html').text
        soup = BeautifulSoup(website,'lxml')

        players = soup.find('table',{'id':'taulaplantilla'})
        
        playersTemp = players.findAll('span', {'class': 'd-none'})

        for player in playersTemp:
            playerName = str(player)
            result = re.search('">(.*)</' ,playerName)
            resultPlayer = result.group(1)
            playerList.append(str(resultPlayer))

        print(playerList)

        dfManagerData = pd.DataFrame(data={'Player': playerList})
        dfManagerData.to_csv('./data/teams/' + teams[index] + '.csv', sep= ';')
        index += 1
