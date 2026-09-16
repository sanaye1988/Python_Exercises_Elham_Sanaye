#15_check_stock

def check_product(products : dict , name_product : str) -> bool :
    if products[name_product] != 0:
        return True
    else:
        return False
    
    
'''

''' 
    
    
products = {"iphone": 5,"macbook": 2,"airpods": 0}

answer = check_product(products, "iphone")

print(answer)