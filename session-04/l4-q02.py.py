cost = float(input('enter product cost:'))

if cost > 1000000:
    print(cost - (cost * 0.2)) 
    
    
elif cost > 500000:
    print(cost - (cost * 0.15))
    
    
elif cost < 500000:
    print(cost - (cost * 0.1))
   
    