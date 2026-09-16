username = input('enter your username:')

password = input('enter your password:')

while username!='admin' and password!='1234':
    print('incorrect username or password')
    username = input('enter your username:')
    password = input('enter your password:')
    
print('you have successfully logged in')