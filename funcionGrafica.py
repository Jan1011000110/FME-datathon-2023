import matplotlib.pyplot as plt
import pandas as pd

def graph(data):
    weeks = [0]*50

    for date in data['FECHAPEDIDO']:
        num = date.split('/')
        num = [int(x) for x in num]
        weeks[1+(num[1]-1)*4 + (num[0]-1)//7] += 1

    plt.bar(range(len(weeks)), weeks)
    plt.title(f'Gráfico de 20{year}')
    plt.xticks(range(1, len(weeks)))

    plt.show()