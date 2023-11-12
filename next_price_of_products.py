from read_data import read_data
from separate_products import separate_products
from separete_years import separete_years
#   from create_graph import generate_graph

def get_predicted_price_of_products():

    def predict_price(product, years):
        keys = [*years.keys()]
        keys.sort()
        keys.reverse()

        average_price_by_year = []

        for year in keys:
            lst = years[year]
            total_price = 0
            total_units = 0

            for i in range(len(lst)):
                row = data[i]
                total_price += row['PRECIO']
                total_units += row['UNIDADESCONSUMOCONTENIDAS']
                
            average = total_price/total_units
            average_price_by_year.append(average)

        predicted_price = 1
        coef = 1
        suma_coef = 0.0

        for i in range(len(average_price_by_year)-1):
            average1 = average_price_by_year[i]
            average2 = average_price_by_year[i+1]

            suma_coef += coef

            if average1 == 0 or average2 == 0:
                continue

            predicted_price *= (average1/average2)**coef
            coef *= 0.9
        
        predicted_price = predicted_price ** (1/suma_coef)
        predicted_price *= average_price_by_year[0]

        #average_price_by_year.reverse()
        #average_price_by_year.append(predicted_price)
        #keys.reverse()
        #keys.append("24")
        #print(keys)
        #print(average_price_by_year)
        #generate_graph(keys, average_price_by_year, product)
        
        #return average_price_by_year[0]
        return predicted_price

        
    # Read data
    data = read_data()

    data = [data.iloc[i] for i in range(len(data))]

    # Get products dictionary
    products = separate_products(data)      

    # Dictionary of predicted price by product
    predicted_price_by_product = {}

    # Iterate through each product
    for product in products:
        # Get de array data of each product
        product_data = products[product]

        # Separate the data in years
        years = separete_years(product_data)    
        
        # Predicted
        predicted_price = predict_price(product, years)

        predicted_price_by_product[product] = predicted_price
    
    return predicted_price_by_product


#get_predicted_price_of_products()
