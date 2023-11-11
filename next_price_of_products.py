from read_data import read_data
from separate_products import separate_products
from separete_years import separete_years

def next_price_of_products():

    def predict_price(years):
        years.sort()
        years.reverse()

        average_price_by_year = {}

        for year, list in years:
            total_price = 0
            total_units = 0

            for i in range(len(list)):
                row = data[i]
                total_price += row['PRECIO']
                total_units += row['UNIDADESCONSUMOCONTENIDAS']
            
            average = total_price/total_units

            if not year in year:
                average_price_by_year[year] = [average]
            else:
                average_price_by_year[year].append(average)

        predicted_price = average_price_by_year[0]
        coef = 1/2

        for i in range(len(average_price_by_year)-1):
            average1 = average_price_by_year[i]
            average2 = average_price_by_year[i+1]
            predicted_price += coef*(average1-average2)
            coef *= 1/2


        return predicted_price

        

    data = read_data()

    data = [data.iloc[i] for i in range(len(data))]

    products = separate_products(data)      

    predicted_price_by_product = {}

    for product in products:
        product_data = products[product]

        years = separete_years(product_data)    
        
        predicted_price = predict_price(years)

        if not product in predicted_price_by_product:
            predicted_price_by_product[product] = [predicted_price]
        else:
            predicted_price_by_product[product].append(predicted_price)
    
    return predicted_price_by_product

