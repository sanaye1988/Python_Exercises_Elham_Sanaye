foods = ['barg', 'chenjeh', 'soltani', 'pizza', 'sandwich', 'burger']

factor = []

for food in foods:
    print(food)
    
while True:
    ordering = input('enter your food')
    
    if ordering == 'order':
        break
    
    if ordering in foods:
        factor.append(ordering)
        
    
print(factor)