
number1 = float(input('enter your number'))
number2 = float(input('enter your number'))

operator = input('enter your operator:')


if operator == '+':
    print(number1+number2)
    
elif operator == '-':
    print(number1-number2)
    
elif operator == '*':
    print(number1*number2)
    
elif operator == '/':
    print(number1/number2)
    
else:
    print('nothing')