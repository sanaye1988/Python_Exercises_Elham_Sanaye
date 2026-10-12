try: 
    number1 = float(input('enter your number:'))
    number2 = float(input('enter your number:'))
    
    result = number1 / number2
    print(result)
    
except ZeroDivisionError:
    raise ZeroDivisionError('adad nemitavanad bar sefr taghgsim shavad.')
    