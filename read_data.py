
import pandas as pd


pd.set_option('display.max_columns', 1000)

data = pd.read_excel('consumo_material_clean.xlsx', index_col=0)  

print(data)

