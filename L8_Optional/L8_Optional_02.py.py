#Optional_2

def products_available(products:dict)->str:
    for name,stock in products.items():
        if stock > 0:
            yield name
            

'''
This function is created to generate one by one, name of products 
that have a stock greater than zero.

Parameters
----------
products : dict
    a dictionary of products.

Yields
------
str
    name of product.
'''

            
products = {
    'laptop': 3,
    'phone': 0,
    'tablet': 5,
    'mouse': 0,
    'keyboard': 2
}
         
generator_products = products_available(products)
print(generator_products)


next(generator_products)