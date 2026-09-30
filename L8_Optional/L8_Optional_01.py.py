#Optional_1

def numbers_even(n:int)->int:
    for i in range(2,n+1):
        if i%2==0:
            yield i

'''
This function is created to generate even numbers one by one, from 2 to n.

n
 ----------
 n : int
     this is a integer number.

Yields
 ------
 int
     generate integer number and even number one by one .
'''
 
 
            
generator_code = numbers_even(8)
print(generator_code)

print(next(generator_code))
print(next(generator_code))
print(next(generator_code))

