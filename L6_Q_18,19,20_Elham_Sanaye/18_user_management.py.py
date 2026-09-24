#18_user_management.py

def add_user(users:list, username:str, age:int, city:str)->list:
    user = {
    'username':username,
    'age':age,
    'city':city,
    'active':True
    }
    
    users.append(user)
    return users
    
    
''' 
 This function is used for add new user as dictionary to last list.

 Parameters
 ----------
 users : list
     this is a list of users.
 username : str
     this is name of user.
 age : int
     this is age of user.
 city : str
     this is city of user.

 Returns
 -------
 users : list
     this is a list of users.

 '''    
    
    
users = [
    
    {
     'username':'ali',
     'age':25,
     'city':'Tehran',
     'active':True
     },
    {
     'username':'sara',
     'age':17,
     'city':'Tabriz',
     'active':True
     },
    {
     'username':'amir',
     'age':40,
     'city':'Tehran',
     'active':True
     },
    ]
    
    
    
print(add_user(users, 'elham', 37, 'Tehran'))

#-------------------------------------------------------

def find_user(users:list, username:str)->dict:
    for user in users:
        if user['username'] == username:
            return user
        
    return None
            

''' 
 This function is used for find user in list.

 Parameters
 ----------
 users : list
     this is a list of users.
 username : str
     this is name of user.

 Returns
 -------
 user : dict
     this is a dictionary of user.

 '''    
    

users = [
    
    {
     'username':'ali',
     'age':25,
     'city':'Tehran',
     'active':True
     },
    {
     'username':'sara',
     'age':17,
     'city':'Tabriz',
     'active':True
     },
    {
     'username':'amir',
     'age':40,
     'city':'Tehran',
     'active':True
     },
    ]
    

print(find_user(users, 'amir'))

#-------------------------------------------------------

def check_access(users, username):
    for user in users:
        if user['username'] == username:
            if user['age'] >= 18: 
                if user['active'] == True:
                    return True
 
    return False



''' 
 This function is used to check access of user in list.

 Parameters
 ----------
 users : list
     this is a list of users.
 username : str
     this is name of user.

 Returns
 -------
 boolean

 '''    
    
 

users = [
    
    {
     'username':'ali',
     'age':25,
     'city':'Tehran',
     'active':True
     },
    {
     'username':'sara',
     'age':17,
     'city':'Tabriz',
     'active':True
     },
    {
     'username':'amir',
     'age':40,
     'city':'Tehran',
     'active':True
     },
    ]
    

print(check_access(users, 'amir'))

#-----------------------------------------------------

def get_adult_users(users):
    
    new_list = []
    
    for user in users:
        if user['age'] > 18: 
            new_list.append(user['username'])
            
    return new_list
  

''' 
 This function is used to get users above 18 years old.

 Parameters
 ----------
 users : list
     this is a list of users.

 Returns
 -------
 new_list:list
     this is a list of users above 18 years old.

 '''    
          

users = [
    
    {
     'username':'ali',
     'age':25,
     'city':'Tehran',
     'active':True
     },
    {
     'username':'sara',
     'age':17,
     'city':'Tabriz',
     'active':True
     },
    {
     'username':'amir',
     'age':40,
     'city':'Tehran',
     'active':True
     },
    ]
    

print(get_adult_users(users))