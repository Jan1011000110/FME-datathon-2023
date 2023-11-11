from next_price_of_products import calculate_T_month_avg
from next_buy_of_products import get_predicted_buy_of_products
from next_price_of_products import get_predicted_price_of_products

prices = get_predicted_price_of_products()
group_amounts = get_predicted_buy_of_products(calculate_T_month_avg(2))

total_amounts = {}

for product in group_amounts:
    total_amounts[product] = add(group_amounts[product])

total_price = 0
product_prices = {}

for product in total_amounts:
    product_price = total_amounts[product] * prices[product]
    product_prices[product] = product_price
    total_price += product_price

print("Total price:", total_price)
print("Product prices:")
print(product_prices)
