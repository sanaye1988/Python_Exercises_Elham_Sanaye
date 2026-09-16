username = input('enter your username:')

password = input('enter your password:')

count = 0

while username!='admin' or password!='1234':
    
    print('incorrect username or password')
    count = count + 1   
    
    if count>=3:
        print('lock your account!!')
        break
    
    username = input('enter your username:')
    password = input('enter your password:')
   
   
if username=='admin' and password=='1234':
    print('you have successfully logged in')