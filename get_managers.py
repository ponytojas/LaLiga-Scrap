#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def getManagerData(urls: []):

    managersList = list()
    print(urls)

    for url in urls:
        print(url)
        website = requests.get(url + 'html').text
        soup = BeautifulSoup(website,'lxml')

        managers = soup.find('table',{'id':'taulaentrenadors'})
        managers_names = managers.findAll('span', {'class': 'd-none'})

        managers_names = str(managers_names)
        result = re.search('">(.*)</' ,managers_names)
        result = result.group(1)

        if ("<span" in result):
            temp = result.split('left">')
            temp = temp[-1]
            result = temp

        print(result)
        managersList.append(result)

    if not os.path.exists('./data/'):
        os.makedirs('./data')

    dfManagerData = pd.DataFrame(data={'Manager': managersList})
    dfManagerData.to_csv('./data/managers.csv', sep= ';')
