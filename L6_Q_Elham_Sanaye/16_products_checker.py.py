#16_products_checker
#a-----------------------------------------------------------

def product_price(products:list , code:str) -> int :
    for product in products:
        if code == product['code']:
            return product['price']




'''
ye tabe tarif kardam ba do vorodi,ye list az chan ta dictionary
va yeki code mahsol,
ba estefade az for check mikone dar har mahsool,
age code vared shode ba code mahsool yeki bashe,gheymat ro pas mide
 
'''



products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]


price = product_price(products, 'z6')
print(price)


#b---------------------------------------------

def product_name(products:list , code:str) -> str :
    for product in products:
        if code == product['code']:
            return product['name']



'''
ye tabe tarif kardam ba do vorodi,ye list az chan ta dictionary 
va yeki code mahsol,
ba estefade az for check mikone dar har mahsool,
age code vared shode ba code mahsool yeki bashe,esme mahsool ro barmigardone
 
'''



products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]



name = product_name(products, 'z4')
print(name)


#c---------------------------------------------------

def product_tuple(products:list , code:str) -> tuple :
    for product in products:
        if code == product['code']:
            tuple_product = tuple(product.values())
            return tuple_product



'''
ye tabe tarif kardam ba do ta vorodi,
ye list az chan ta dictionary va yeki code mahsol,
ba estefade az for check mikone dar har mahsool,
age code vared shode ba code mahsool yeki bashe,
kole item haye mahsool ro be soorate tuple bargardone

'''




products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]



new_tuple = product_tuple(products, 'z3')
print(new_tuple)