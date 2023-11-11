import pandas as pd
#from read_data import read_data


def separate_products(data):
    products = {}

    for i in range(len(data)):
        row = data[i]

        product = row['PRODUCTO']

        if not product in products:
            products[product] = [row]
        else:
            products[product].append(row)
    
    return products

"""
data = read_data()

data = [data.iloc[i] for i in range(len(data))]

products = separate_products(data)

keys = [*products.keys()]

keys.sort()

print(keys)
print(len(keys))"""




