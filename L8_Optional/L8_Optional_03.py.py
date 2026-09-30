#Optional_3

def profile_create(name,age,**data):   
    print(name)
    print(age)
    print(data)
    print(len(data))
    
    for element in data:
        if element == 'city' :
            print(f'city : {data['city']}')
            
    for element in data:
        if element != 'email' :
            print('email not provided')
      

'''
This function is created to show information of user.

Parameters
----------
name : str
    this is username.
age : int
    this is user age.
**data : dict
    a dictionary of user information.

Returns
-------
None
'''


    
print(profile_create('elham', 37, city='Tehran'))    
  
print(profile_create('elham', 37, city='Tehran', job = 'engineer', email = '@hbjh'))  

print(profile_create('elham', 37,job = 'engineer'))    


