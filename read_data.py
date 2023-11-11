
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.expand_frame_repr', False)

def read_data():
    data = pd.read_excel('consumo_material_clean.xlsx')  
    return data

#print(read_data())