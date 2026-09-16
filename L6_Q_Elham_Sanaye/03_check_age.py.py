#3_check_age

def check_age(age:int)->str :
    if age < 18:
        sen = 'Access denied'
        return sen
    else:
        sen = 'Welcome!'
        return sen

'''
ye tabe neveshtam ke sen ro voroodi begire,
shart ro check kone, age zire 18 bood 'Access denied' bargardone,
age balaye 18 bood 'Welcome!' bargardone.
'''
    
sen = check_age(16)
print(sen)