# Fancy Houses
"""
Calculate and output the number of houses
that have a price that is above the average.
"""

prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

avg_price = int(int(sum(prices)) / int(len(prices)))

print(avg_price)

number_abv_avg = len([p for p in prices if p > avg_price])
# for price in prices:
#     if price > avg_price:

print("Number of houses above the average price:", number_abv_avg)
