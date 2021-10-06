# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:31:01 2021

@author: gusta
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:01:43 2021

@author: Gustavo Esporte dos Santos
"""

from bs4 import BeautifulSoup #to webscrapping

import requests #helps to downloand de webpage

import re #to use the function re.compile

import pandas as pd #to create a data frame

import itertools #to remove duplicate values 

#To save the link of the webpage that will be scrapped
url = "https://br.loccitaneaubresil.com"

#to get the contents of the webpage in text format and store in the variable data
data = requests.get(url).text

#create a BeautifulSoup object
soup = BeautifulSoup(data,"html5lib")

#create a list to save all links in the webpage
lista = []
l_pname=[]
l_prices=[]
d={}

#to save all the links in the list "lista"
for link in soup.find_all("a",href=re.compile("https")):
    lista.append(link.get('href'))

#this line was made just to check if the code get all link on the page        
#print(len(lista))

for i in range(len(lista)):
    data_i = requests.get(lista[i]).text
    soup_i = BeautifulSoup(data_i,"html5lib")
    
    
    for p_name in (soup_i.find_all(class_=re.compile('product-name'))):
        l_pname.append((p_name.get_text().replace("\n","").replace("\t","")))

    for p_price in (soup_i.find_all(class_=re.compile('offer-price'))):
        l_prices.append(p_price.get_text().replace("\xa0","").replace(" ",""))


#to create a dictionary in this fromat: "name of product: price of product"    
d = dict(zip(l_pname,l_prices))

print(d)

df = pd.DataFrame(list(d.items()),columns = ['Produto','Preco (R$)'])

#Just to test if the dataframe was working correctly
print(df)

#defining the path where I will save my CSV file
path = "C:/Users/gusta/OneDrive/Área de Trabalho/L'occitane/produtos_precos_teste6.csv"

#to export the data frame in a CSV file
df.to_csv(path,encoding='utf-8-sig') 
