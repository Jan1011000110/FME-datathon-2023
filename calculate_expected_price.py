from calculate_2_month_avg import calculate_T_month_avg
from next_buy_of_products import get_predicted_buy_of_products
from next_price_of_products import get_predicted_price_of_products

prices = get_predicted_price_of_products()
T_avg = calculate_T_month_avg(2)
group_amounts = get_predicted_buy_of_products(T_avg)

total_amounts = {}

for product in group_amounts:
    total_amounts[product] = sum(group_amounts[product])

total_price = 0
product_prices = {}

#print(T_avg['E67462'])

print(total_amounts)
print(prices)
for product in total_amounts:
    product_price = total_amounts[product] * prices[product]
    product_prices[product] = product_price
    total_price += product_price

print("Total price:", total_price)
print("Product prices:")
print(product_prices)
