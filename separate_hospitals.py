
from read_data import read_data


data = read_data()

hospitals = {}

for i in range(len(data)):
    row = data.iloc(i)
    print(row)
    break
