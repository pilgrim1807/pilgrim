# def discounted(price, discount):
#     price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# def название_функции(аргумент1, аргумент2, ...):
#     тело функции
#     ...

def get_summ(one, two, delimiter='&'):  # объявление функции
    a = str(one)
    b = str(two)

    result = a + delimiter + b

    return result

get_summ('learn', 'python', ' ')
r = get_summ('learn', 'python', ' ').upper() # вызов get_summ, передавая ей аргументы 1, 2, 'a'
print(r)

#
#
# get_summ(1, 2, 'a') == '1a2'
# get_summ(1, 2) == '1&2'
# get_summ('hello', 'world', '!') == 'hello!world'


# one = 1
# two = 3
# delimiter = '&'
#
# a = str(one)
# b = str(two)
#
# result = a+delimiter+b
# print(result)


