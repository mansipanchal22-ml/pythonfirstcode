#Implement a function that accepts product details like name, price and quantity using **kwargs.
# Return total cost.

def product(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]
    return total 

cost = product(name="phone", price=25000, quantity=2)

print("Total Cost=", cost)

