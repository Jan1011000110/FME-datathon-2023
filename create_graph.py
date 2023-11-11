import matplotlib.pyplot as plt
import pandas as pd

def week_graph(data, year, name):
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