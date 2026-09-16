product = input('enter your product:')

cost = float(input('enter your cost:'))

code = input('enter discount code:')

if code.upper().strip() == 'Z14':
    print(cost*1/5)
    
else:
    print('incorrect code')
