import pandas as pd
from read_data import read_data

def separete_years(data):
    years = {}
    for i in range(len(data)):
        row = data[i]
        date = row['FECHAPEDIDO']
        year = date[-2:]
        
        if not year in years:
            years[year] = [row]
        else:
            years[year].append(row)
    
    return years
