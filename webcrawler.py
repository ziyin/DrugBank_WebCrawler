# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd 
import openpyxl

ismFile = '/content/drive/My Drive/Colab File/Bug_file.xlsx'
excel=pd.read_excel(ismFile)

print(excel)

import time
import random

workbook=openpyxl.load_workbook('/content/drive/My Drive/Colab File/Bug_file.xlsx')
worksheet=workbook.worksheets[0]

#excel.shape[0]
for i in range(662):
  time.sleep((random.random()*3)+5)
  response = requests.get('https://go.drugbank.com/structures/small_molecule_drugs/'+excel['DrugBank ID'][i]+'.smiles')
  soup = BeautifulSoup(response.text, "html.parser")
  soup=soup.prettify()
  soup=soup.strip()
  if(soup!=''):
    worksheet.cell((i+2),3,soup)
    workbook.save('/content/drive/My Drive/Colab File/Bug_file.xlsx')
    print(i)

