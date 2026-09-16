speed = float(input('enter your car speed:'))
    
if speed > 120 :
    print('dangerous')
    
elif  speed > 80 : 
    print('max speed')
    
elif 0 < speed < 80:
    print('normal speed')
    
else:
    print('The car is stationary!')
    
    