try: 
    number_user = float(input('enter your number:'))
    
    new_number = number_user * 2
    
    print(new_number)
    
except ValueError:
    raise ValueError('enter only numbers')
    