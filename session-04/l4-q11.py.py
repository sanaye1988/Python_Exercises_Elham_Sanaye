buy_prices = [100, 200, 150, 400]

sell_prices = [130, 250, 190, 500]

new_list = []

benefit = 0

for i in range(len(buy_prices)):
    benefit = sell_prices[i] - buy_prices[i]
    new_list.append(benefit)
    
print(new_list)


'''
man be jaye range(len(buy_prices)) , buy_prices gharar dadam , ama error 
dad : list index out of range ----az Chatgpt porsidam vali motevajeh nemisham
chera bayad len gharar bedam 
'''
