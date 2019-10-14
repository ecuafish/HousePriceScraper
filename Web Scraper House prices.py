# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:16:22 2019

@author: StevenCaizapanta
"""
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

"""
The header will mimic human interaction and avoid getting locked out
"""
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    
plusvalia = "https://www.plusvalia.com/departamentos-en-venta-en-quito.html"

response = get(plusvalia, headers=headers)

print(response)

html_soup = BeautifulSoup(response.text, 'html.parser')

house_containers = html_soup.find_all('div', class_="posting-info-container")

first = house_containers[0]
title = first.find_all('h3')
print(title)
title = title[0]
print(title)
title = title.findAll('a')
print(title)
title = title[0].text
print(title)

print(first)

main_features = first.find_all('ul', class_="main-features")
print(main_features)



    
def extract_all_links():
    return 0

def extract_content():
    return 0;

