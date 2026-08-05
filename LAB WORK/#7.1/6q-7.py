#write a python function that accepts an arbitrary number of integer arguments and returns their sum and product.

def sum_product(*args):
    sum = 0
    product = 1

    for i in args:
        sum = sum + i
        product = product * i

    print("sum =", sum)
    print("Product =",product)

sum_product(1,2,3,4,5)

