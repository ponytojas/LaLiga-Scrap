#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def getManagerData(urls: []):

    managers = []

    for url in urls:
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

        managers.append(result)

    dfManagerData = pd.DataFrame(data={'Manager': managers})
    dfManagerData.to_csv('managers.csv', sep= ';')
