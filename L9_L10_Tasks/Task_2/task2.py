def add_user(identifier,name,email,status):  
    
    user_list = []
        
    try:
        with open('users.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                user = line.strip().split(',')

                if len(user) == 4:
                    user_list.append([item.strip() for item in user])

    except FileNotFoundError:
        raise FileExistsError('file is not available!')
        
    identifier = str(identifier).strip()
    email = email.strip()

    for user in user_list:
        if user[0] == identifier:
            raise ValueError('This identifier already exists!')

        if user[2] == email:
            raise ValueError('This email already exists!')

    with open('users.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{identifier}, {name}, {email}, {status}\n')
                   

def find_user(identifier,name):
    
    user_list = []
    
    with open('users.txt','r',encoding='UTF-8') as file:
        for line in file:
            user_line = line.strip().split(',')
            user_list.append(user_line)
            
    for user in user_list:
        if user[0] or user[1] in user_list:
            return name,identifier
       
        
def delete_user(identifier):
    identifier = str(identifier).strip()

    try:
        with open('users.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileExistsError('file is not available!')

    new_lines = []
    found = False

    for line in lines:
        user = [item.strip() for item in line.strip().split(',')]

        if user and user[0] == identifier:
            found = True
        else:
            new_lines.append(line)

    if found:
        with open('users.txt', 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        print('User deleted!')
    else:
        print('User not found!')
     
  
def update_user(identifier):
    try:
        with open('users.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileExistsError('file is not available!')

    found = False
    new_lines = []

    for line in lines:
        user = [item.strip() for item in line.strip().split(',')]

        if len(user) != 4:
            new_lines.append(line)
            continue

        if user[0] == identifier:
            found = True
            
            user[2] = input('Enter new email:').strip()
            user[3] = input('Enter new status:').strip()

            new_lines.append(', '.join(user) + '\n')
        else:
            new_lines.append(line)

    if found:
        with open('users.txt', 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        print('User updated successfully!')
    else:
        print('User not found!')

         

def list_users():
    
    user_list = []

    try:
        with open('users.txt', 'r', encoding='utf-8') as file:
            for line in file:
                user = line.strip().split(',')
                user_list.append(user[1].strip())

        return user_list

    except FileNotFoundError:
        raise FileExistsError('file is not available!')


def generate_report():
    active = 0
    blocked = 0
    total = 0

    try:
        with open('users.txt', 'r', encoding='utf-8') as file:
            for line in file:
                user = line.strip().split(',')

                if len(user) != 4:
                    continue

                total += 1
                status = user[3].strip()

                if status == 'active':
                    active += 1
                elif status == 'blocked':
                    blocked += 1

        print('Active users:', active)
        print('Blocked users:', blocked)
        print('Total users:', total)

    except FileNotFoundError:
        raise FileExistsError('file is not available!')


while True:
    print('1. Add user')
    print('2. Find user')
    print('3. Delete user')
    print('4. Update user')
    print('5. List users')
    print('0. Exit')

    choice = input('Enter your choice:').strip()

    if choice == '1':
        identifier = input('Enter identifier: ')
        name = input('Enter name: ')
        email = input('Enter email: ')
        status = input('Enter status: ')

        try:
            add_user(identifier, name, email, status)
        except Exception() as e:
            print(e)

    elif choice == '2':
        identifier = input('Enter identifier:')
        name = input('Enter name:')

        user = find_user(identifier, name)

        if user:
            print(user)
        else:
            print('User not found!')

    elif choice == '3':
        identifier = input('Enter identifier:')
        delete_user(identifier)

    elif choice == '4':
        identifier = input('Enter identifier:')
        update_user(identifier)

    elif choice == '5':
        users = list_users()

        if users:
            for user in users:
                print(user)
        else:
            print('No users found!')

    elif choice == '0':
        print('Goodbye!')
        break

    else:
        print('Invalid choice! Please try again.')