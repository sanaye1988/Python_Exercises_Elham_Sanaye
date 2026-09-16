#12_calculator

def calculate_operation(number1:float , number2:float() , operation : str)->float:
    if operation == 'jam':
        result = number1 + number2
        return result

    elif operation == 'tafrigh':
        result = number1 - number2
        return result

    elif operation == 'zarb':
        result = number1 * number2
        return result

    elif operation == 'taghsim':
        result = number1 / number2
        return result

    else:
        return None
        

    
'''
ye tabe neveshtam ke 3 parameter dare,do adad va ye amalgar,
baraye 4 amalgare "jam, tafrigh, zarb, taghsim",mohasebe mikone
va natije ro barmigardone, age hich kodom az ina nabod none pas mide
'''

    
number1 = 9
number2 = 3

result = calculate_operation(9, 3, 'zarb')
print(result)