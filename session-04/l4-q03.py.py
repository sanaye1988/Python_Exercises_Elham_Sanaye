products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

UserProduct = input('enter your product:')

if UserProduct in products:
    print('your product is available')
    
else:
    print('your product is not available')
    
    
    
    
'''   
.upper().strip()
ba ezafe kardane in 2 tabe taghiri ijad nemikonad
'''


'''
man fek mikardam bayad == bezaram , javab nagereftam , 
az chatgpt porsidam va in gozashtam
'''

#be in shekl ham hal kardfam khodam

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

UserProduct = input('enter your product:')

if UserProduct == products[0] or UserProduct == products[1] or UserProduct == products[2] or UserProduct == products[3]:
    print('your product is available')
    
else:
    print('your product is not available')
    