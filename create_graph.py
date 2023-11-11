import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def generate_graph(names, values, product):
    plt.clf()
    plt.plot(np.array(names), np.array(values))
    plt.show(block=True)
    plt.savefig("./prices/{}.png".format(product))

def week_graph(data, year, name):
    plt.clf()
    weeks = [0]*50

    for row in data:
        date = row['FECHAPEDIDO']
        num = date.split('/')
        num = [int(x) for x in num]
        weeks[1+(num[1]-1)*4 + (num[0]-1)//7] += int(row['CANTIDADCOMPRA'])

    plt.bar(range(len(weeks)), weeks)
    plt.title(f'Gráfico de 20{year}')
    plt.xticks(range(1, len(weeks)))

    plt.savefig(name)


def prices_graph(data, year, name):
    plt.clf()
    months = [0]*(200)
    months_cnt = [0]*(200)

    for row in data:
        date = row['FECHAPEDIDO']
        num = date.split('/')
        num = [int(x) for x in num]
        months[1+(num[1]-1) + (num[2]-15)*12] += int(row['IMPORTELINEA'])/int(row['CANTIDADCOMPRA'])
        months_cnt[1+(num[1]-1) + (num[2]-15)*12] += 1
    
    for i in range(len(months)):
        if months_cnt[i] != 0:
            months[i] = months[i] / months_cnt[i]

    plt.bar(range(len(months)), months)
    plt.title(f'Gráfico de 20')
    plt.xticks(range(1, len(months)))
    plt.savefig(name)
    plt.clear()