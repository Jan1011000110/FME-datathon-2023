from datetime import datetime
import os
from read_data import read_data
from separate_hospitals import separate_hospitals
from separate_products import separate_products
from separete_years import separete_years
from create_graph import prices_graph


data = read_data()

data = [data.iloc[i] for i in range(len(data))]

products = separate_products(data)

try:
    os.mkdir("/home/sergio/prg/github/datathon/prices/")
except:
    pass

for product in products:
    pdata = products[product]
    
    prices_graph(pdata, 0, "/home/sergio/prg/github/datathon/prices/{pr}.png".format(pr=product))

