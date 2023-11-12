from read_data import read_data
from separate_products import separate_products
from separete_years import separete_years
from sklearn import linear_model

def get_predicted_price_of_products():

    def predict_price(product, years):
        keys = [*years.keys()]
        keys.sort()
        keys.reverse()

        
        
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