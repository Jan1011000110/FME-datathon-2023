import os
from read_data import read_data
from separate_hospitals import separate_hospitals
from separate_products import separate_products
from separete_years import separete_years
from create_graph import week_graph


data = read_data()

hospitals = separate_hospitals(data)

for hospital in hospitals:
    hdata = hospitals[hospital]

    products = separate_products(hdata)

    try:
        os.mkdir("/home/sergio/prg/github/datathon/{hs}/".format(hs=hospital))
    except:
        pass

    for product in products:
        pdata = products[product]

        years = separete_years(pdata)
        
        try:
            os.mkdir("/home/sergio/prg/github/datathon/{hs}/{pr}/".format(hs=hospital, pr=product))
        except:
            pass
        
        for year in years:
            ydata = years[year]

            week_graph(ydata, year, "/home/sergio/prg/github/datathon/{hs}/{pr}/{yr}.png".format(hs=hospital, pr=product, yr=year))

