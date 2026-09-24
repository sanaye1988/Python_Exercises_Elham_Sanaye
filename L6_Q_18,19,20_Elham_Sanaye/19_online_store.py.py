#19_online_store.py

def find_product(products:list, code:str)->dict:
    for product in products:
        if product['code'] == code:
            return product
        
    return None


"""
this function is used for find product with code.

Parameters
----------
products : list
    this is a list of products.
code : str
    this is product's code.

Returns
-------
product : dict
    this is a dictionary of product.
"""


products = [
    {'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},

    {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7},

    {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},

    {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}
]

print(find_product(products, 'p3'))

#===================================================================

def add_to_cart(products:list, cart:list, code:str)->list:
    cart = []
    for product in products:
        if product['code'] == code:
            if product['stock']> 0:
                cart.append(product)
                return cart
  

            
"""
 this function is used for check product and add to list.

 Parameters
 ----------
 products : list
     this is a list of products.
 cart : list
         this is a list.
 code : str
     this is product's code.

 Returns
 -------
 cart : list
     this is a list of product.
"""
           
products = [
    {'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},

    {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7},

    {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},

    {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}
]

print(add_to_cart(products, [], 'p3'))

#----------------------------------------------------------------

def check_product(products:list, code:str)->list:
    for product in products:
        if product['code'] == code:
            if product['stock']> 0:
                product['stock'] -= 1
                return products



"""
 this function is used for check product and.

 Parameters
 ----------
 products : list
     this is a list of products.
 code : str
     this is product's code.

 Returns
 -------
 products : list
     this is a list of products.
"""
    

products = [
        {'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},

        {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7},

        {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},

        {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}
    ]

print(check_product(products, 'p2'))

#----------------------------------------------------------------

def add_to_cart_chang_product(products:list, cart:list, code:str)->list:
    cart = []
    for product in products:
        if product['code'] == code:
            if product['stock']> 0:
                cart.append(product['name'])
                product['stock'] -= 1
                return cart,products
 

"""
 this function is used for check product and add to list.

 Parameters
 ----------
 products : list
     this is a list of products.
 cart : list
         this is a list.
 code : str
     this is product's code.

 Returns
 -------
 cart : list
     this is a list of product.
 products : list
     this is a list of products
"""
            
        
products = [
        {'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},

        {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7},

        {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},

        {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}
    ]

print(add_to_cart_chang_product(products, [], 'p1'))