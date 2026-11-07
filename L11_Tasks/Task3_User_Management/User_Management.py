import os

class User:
    def __init__(self,username,password,email,status):
        if status not in ['active', 'blocked']:
            raise ValueError('Invalid status!')
            
        self.username = username
        self.password = password
        self.email = email
        self.status = status
        
        
        
    def __str__(self):
        return f'User:{self.username}'
        
        
        
    def to_format(self):
        return f'{self.username}|{self.password}|{self.email}|{self.status}'
            
            

class FileManager:
    def __init__(self,file_name):
        self.file_name = file_name
        
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="UTF-8"):
                self.file_name.write()
        
        
    def read_users(self):
        users = []
        with open(self.file_name, "r", encoding="UTF-8") as file:
            for line in file:
                parts = line.strip().split('|')
                username = parts[0]
                password = parts[1]
                email = parts[2]
                status = parts[3]
                
                
                user = User(username,password,email,status)
                users.append(user)
                
            return users
        

    
    
    def find_user(self,username):
        users = self.read_users()
        
        for user in users:
            if user.username == username:
                return user
            


    def add_user(self,user):
        if self.find_user(user.username):
            raise ValueError('User exists!')
            
        if user.status not in ['active', 'blocked']:
            raise ValueError('Invalid status!')

        with open(self.file_name, "a", encoding="UTF-8") as file:
            file.write(user.to_format() + "\n")

        print('User added successfully!')

    
    def delete_user(self,username):
        users = self.read_users()
        
        for user in users:
            if user.username == username:
                users.remove(user)

        with open(self.file_name, "w", encoding="UTF-8") as file:
            for user in users:
                file.write(user.to_format() + "\n")


    
    def update_status(self,username,change_status):
        if change_status not in ['active', 'blocked']:
            raise ValueError('Invalid status!')

        users = self.read_users()

        for user in users:
            if user.username == username:
                user.status = change_status
    
                with open(self.file_name, "w", encoding="UTF-8") as file:
                    for user in users:
                        file.write(user.to_format() + "\n")
    
                print('Status updated!')
            
    
    def login(self,username,password):
        user = self.find_user(username)

        if user is None:
            print('Incorrect username!')

    
        elif user.password != password:
            print('Incorrect password!')
            
        elif user.status == 'blocked':
            print('User is blocked!')
    
        else:
            print('Login successful!')
    
    
    def generate_report(self):
        users = self.read_users()

        active_count = 0
        blocked_count = 0
    
        for user in users:
            if user.status == 'active':
                active_count += 1
    
            elif user.status == 'blocked':
                blocked_count += 1
    
        print(f'Active Users: {active_count}')
        print(f'Blocked Users: {blocked_count}')
      

file_manager = FileManager("users.txt")

while True:
    print("======User Management======")
    print("1. Add User")
    print("2. Find User")
    print("3. Delete User")
    print("4. Update Status")
    print("5. Login")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter your choice: ")
    
    
    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        status = input("Status: ")

        user = User(username, password, email, status)
        file_manager.add_user(user)
        
    elif choice == '2':
        username = input("Username: ")
        user = file_manager.find_user(username)

        if user:
            print(user)
        else:
            print("User not found!")
            
    elif choice == '3':
        sername = input("Username: ")
        file_manager.delete_user(username)

    elif choice == '4':
        username = input("Username: ")
        status = input("New status: ")
        file_manager.update_status(username, status)

    elif choice == '5':
        username = input("Username: ")
        password = input("Password: ")
        file_manager.login(username, password)

    elif choice == '6':
        file_manager.generate_report()

    elif choice == '7':
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")