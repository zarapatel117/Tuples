from functools import reduce

def calculate_product(tup):
    return reduce(lambda x, y: x * y, tup)

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

product1 = calculate_product(tup1)
product2 = calculate_product(tup2)

print("Product of tup1: ", product2)
print("Product of tup2:", product2)
