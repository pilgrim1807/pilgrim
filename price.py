def format_price(price):
    a = int(price)
    # return "Цена: ЧИСЛО руб."
    b = "Цена: {} руб.".format(a)
    return b
a = format_price(56.24)
print(a)