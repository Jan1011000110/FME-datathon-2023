from read_data import read_data
from separate_products import separate_products
from separete_years import separete_years
from create_graph import generate_graph

def calculate_T_month_avg(T):
    # Read data
    data = read_data()

    data = [data.iloc[i] for i in range(len(data))]

    # Get products dictionary
    products = separate_products(data)      

    # Result dictionary
    avg_T_month = {}

    for product in products:
        pdata = products[product]

        rs = []
        cnt_rs = []
        for i in range(9):
            rs.append([])
            cnt_rs.append([])
            for j in range(12//T):
                rs[i].append(0)
                cnt_rs[i].append(0)
        
        for row in pdata:
            tm = row['FECHAPEDIDO']
            year = int(tm.split("/")[2])-15
            month = int(tm.split("/")[1])-1
            rs[year][month//T] += row['CANTIDADCOMPRA']
            cnt_rs[year][month//T] += 1
        
        for i in range(9):
            for j in range(12//T):
                if cnt_rs[i][j] != 0:
                    rs[i][j] /= cnt_rs[i][j]
        
        avg_T_month[product] = rs
    
    return avg_T_month


#print(calculate_T_month_avg(2))
