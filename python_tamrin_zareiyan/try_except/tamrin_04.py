while True:
    try:
        number = float(input('enter your number:'))
        
    except ValueError:
        raise ValueError('faghat adad migirad')
    except TypeError:
        raise TypeError('faghat adad vared konid')
        
    else:
        print(number)
        break
    
    
    
    
    