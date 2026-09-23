#exercise 2

def product_inventory(products:dict) -> list:
    
    list_inventory = []
    list_out_of_stock = []
    
    for name,count in products.items():
        if count > 0:
            list_inventory.append(name)
        else:
            list_out_of_stock.append(name)
            
    return list_inventory, list_out_of_stock
            

    
    
    
    
'''
This function is used  to find name of inventory product and out_of_stock .

Parameters
----------
productions : dict
    this is dictionary of products..

Returns
-------
list_inventory, list_out_of_stock : list
    two output returns:list of inventory product and out_of_stock.
    
'''



inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}


inventory, out_of_stock = product_inventory(inventory)
print(inventory)
print(out_of_stock)