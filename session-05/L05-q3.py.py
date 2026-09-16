product = input('enter your product:')

products = []


while product != 'exit':
    products.append(product)
    product = input('enter your product:')
    
print(products)