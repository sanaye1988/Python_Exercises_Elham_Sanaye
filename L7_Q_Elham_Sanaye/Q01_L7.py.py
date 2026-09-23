#exercise 1


def find_max_price(products:dict) -> int :
      
    list_products = list(products.values())
    max_price = list_products[0]
    
    for element in list_products:
        if element > max_price:
            max_price = element
    
    return max_price
    
  
    
  
'''
This function is used  to get maximum price in dictionary of products.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
max_price : int
    this is maximum price.
    
'''
    
    
    
products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}



maxprice = find_max_price(products)

print(maxprice)


#----------------------------------------------------------------------

def find_name_max_price(products:dict) -> str :
    
    list_products = list(products.items())
    max_price = list_products[0][1]
    name_product = list_products[0][0]
    for name,price in list_products:
        if price > max_price:
            max_price = price
            name_product = name
        
    return name_product
    


'''
This function is used  to get name of product with maximum price in dictionary of products.
this dictionary is converted to a list of tuples that contains name and price.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
name_product : str
    this is name of product with maximum price.
    
'''


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


name_product = find_name_max_price(products)

print(name_product)
  

#---------------------------------------------------------------------------

def find_min_price(products:dict) -> int :
      
    new_list_products = list(products.values())
    min_price = new_list_products[0]
    
    for element in new_list_products:
        if element < min_price:
            min_price = element
    
    return min_price


'''
This function is used to get minimum price in dictionary of products.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
min_price : int
    this is minimum price.
    
'''


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}



minprice = find_min_price(products)

print(minprice)


#---------------------------------------------------------------------------


def find_name_min_price(products:dict) -> str :
    
    list_products = list(products.items())
    max_price = list_products[0][1]
    name_product = list_products[0][0]
    for name,price in list_products:
        if price < max_price:
            max_price = price
            name_product = name
        
    return name_product



'''
This function is used to get name of product with minimum price in dictionary of products.
this dictionary is converted to a list of tuples that contains name and price.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
name_product : str
    this is name of product with minimum price.
    
'''


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


name_product = find_name_min_price(products)

print(name_product)


#---------------------------------------------------------------------------

def total_price_product(products:dict)->int:
      
    total_price = 0
    for price in products.values():
        total_price = total_price + price
        
    return total_price
    

'''
This function is used to get sum of price in dictionary of products.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
total_price : int
    this is sum of price.
    
'''


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


total_price = total_price_product(products)

print(total_price)


#---------------------------------------------------------------------------


def average_product(products:dict)->int:
      
    total_price = 0
    count = 0
    for price in products.values():
        total_price = total_price + price
        count += 1
        avg = total_price / count
        
    return avg


'''
This function is used to get average of products in dictionary of products.

Parameters
----------
products : dict
    this is dictionary of products.

Returns
-------
avg : int
    this is average of products.
    
'''


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


average = average_product(products)

print(average)
