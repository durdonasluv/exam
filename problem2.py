def find_top_seller(products, sales):
    full_price = {}
    for product in products:
        price = products[product] * sales[product]
        full_price[product] = price
    highest_revenue = max(full_price, key=lambda x: x[1])
    return highest_revenue








print(find_top_seller(
    {"apple": 5000, "banana": 8000, "grape": 7000},
    {"apple": 10,   "banana": 5,    "grape": 8}
))