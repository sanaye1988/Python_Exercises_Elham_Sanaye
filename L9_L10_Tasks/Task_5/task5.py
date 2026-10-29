account_numbers = [] 
class BankAccount:   
    
    def __init__(self,owner,account_number,balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        balance = 100000
        self.transactions = []
        
        if account_number in account_numbers:
            raise ValueError('account number is duplicate.')
        else:
            account_numbers.append(account_number)
        
    def __str__(self):
        return f'{self.owner} : {self.account_number}'
    
    def get_balance(self):
        print(f'your balance is {self.balance}')
        
        
    def deposit(self,amount):
        if amount <= 0 :
            raise ValueError('amount cannot be negative.')
        elif amount > self.balance:
            raise ValueError('amount cannot exceed the balance.')
        else:
            self.balance += amount
            self.transactions.append(f'+ {amount}')
            print('deposit completed successfully.')
    
    
    def withdraw(self,amount):
        if amount <= 0 :
            raise ValueError('amount cannot be negative.')
        elif amount > self.balance:
            raise ValueError('amount cannot exceed the balance.')
        else:
            self.balance -= amount
            self.transactions.append(f'- {amount}')
            print('withdraw completed successfully.')
        
    
    def transfer(self,customer_account,amount):
        if amount <= 0 :
            raise ValueError('amount cannot be negative.')
        elif amount > self.balance:
            raise ValueError('amount cannot exceed the balance.')
        else:
            self.balance -= amount
            customer_account.balance += amount
            self.transactions.append(f'transfer:{amount}')
            print('this amount was deposited into the customers account.')
            print(f'customer balance:{customer_account.balance}')
  
        
    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
            
        
        
owner1 = BankAccount('elham', '035467', 12000000) 
print(owner1)

owner2  = BankAccount('mina', '17887', 45000000) 
print(owner2)

owner3  = BankAccount('mina', '17887', 45000000) 
print(owner3)

owner4  = BankAccount('amir', '56388', 24000000) 
print(owner4)


owner1.deposit(10000)
owner1.balance

owner1.get_balance()
owner1.transaction_history()

owner1.withdraw(2500000)

transfer = owner1.transfer(owner2,450000)
print(transfer)
