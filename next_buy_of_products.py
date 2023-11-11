NUMBER_OF_BUYS = 6

def get_predicted_buy_of_products(data):
    
    def predict_buy(years, buy):
        buys_by_year = []

        for lst_buy in years:
            buys_by_year.append(lst_buy[buy])
        
        buys_by_year.reverse()
        
        predicted_buy = buys_by_year[0]
        coef = 1/2

        for i in range(len(buys_by_year)-1):
            buy1 = buys_by_year[i]
            buy2 = buys_by_year[i+1]

            predicted_buy += coef*(buy1-buy2)
            coef *= 1/2
        
        return predicted_buy

    
    predicted_buy_by_product = {}

    for buy in range(NUMBER_OF_BUYS):
        for product, years in data.items():
            predicted_buy = predict_buy(years, buy)

            if not product in predicted_buy_by_product:
                predicted_buy_by_product[product] = [predicted_buy]
            else:
                predicted_buy_by_product[product].append(predicted_buy)
    
    return predicted_buy_by_product
