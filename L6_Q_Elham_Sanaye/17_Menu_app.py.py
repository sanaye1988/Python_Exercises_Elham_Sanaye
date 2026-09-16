#17_Menu_app


def menu_order():
    
    list_order = []
    
    while True:
        food_order = input('enter your food:')
        
        if food_order == 'order':
            break
        
        list_order.append(food_order)
        
    return list_order
        
   
    
'''
ye tabe sakhtam ke vorodi nadare,az moshtari mikhad ke ghazasho entekhab kone,
ta vaghti ke order ro entekhab kone edame mide,dar akhar tamame ghazahaye 
entekhab shode ro be list ezafe mikone va dar khoroji barmigardone
'''
    
    
menu = ['pizza', 'burger', 'kabab', 'sandwich', 'chicken']

list_order = menu_order()

print(list_order)