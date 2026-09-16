#14_multiplication_table

def multiplication_table(number:int) -> int :
    for i in range(1,11):
        new_number = number * i
        print(f'{number} * {i} = {new_number}')
        
        

'''
ye tabe tarif kardam ke vorodi ye adad begire va barash jadvale zarb besaze,
ba estefade az halghe for, baze 1 ta 10 ro migire va dar adade morede nazar
zarb mikone va dar akhar print mikone jadval zarb ro

'''


jadval = multiplication_table(7)
print(jadval)