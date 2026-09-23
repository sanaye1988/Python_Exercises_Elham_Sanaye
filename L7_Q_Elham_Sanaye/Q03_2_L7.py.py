# exercise 3-2

def manage_price(sales:list)->dict:
    
    sales_dict = {}
    
    for name,product,price in sales:
        if name not in sales_dict:
            sales_dict[name] = 0
            
        sales_dict[name] += price
                
    return sales_dict

'''
This function is used to calculate sum of each person's sales.

Parameters
----------
sales : list
    this is a list each person's sales information.

Returns
-------
sales_dict : dict
    this is a dictionary from sum of each person's sales .

'''



sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]

print(manage_price(sales))

#--------------------------------------------------------------------

def manage_count(sales:list)->dict:
    
        sales_dict = {}
        
        for name,product,price in sales:
            if product not in sales_dict:
                sales_dict[product] = 0
            
            sales_dict[product] += 1
                    
        return sales_dict


'''
This function is used to calculate of count of each product.

Parameters
----------
sales : list
    this is a list each person's sales information.

Returns
-------
sales_dict : dict
    this is a dictionary from sum of count of each product.

'''


sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]

print(manage_count(sales))


#--------------------------------------------------------------------

def total_sales(sales:list)->int:
    
    total_price = 0
    
    for name,product,price in sales:
        total_price += price
        
    return total_price


'''
This function is used to calculate total sales.

Parameters
----------
sales : list
    this is a list each person's sales information.

Returns
-------
sales_dict : dict
    this is total of sales.

'''

sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]

print(total_sales(sales))