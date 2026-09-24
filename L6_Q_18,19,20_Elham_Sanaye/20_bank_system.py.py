#20_bank_system.py

def login(accounts:list, username:str, password:str)->bool:
    for account in accounts:
        if account['username'] != username:
           return None 
        if account['username'] == username:
            if account['password'] == password:
                return True
        return False


"""
This function is used to login user for bank account.

Parameters
----------
accounts : list
    this is a list of bank account.
username : str
    name of user.
password : str
    user's password.

Returns
-------
bool
    return True or False.
"""


accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]


print(login(accounts, 'ali', '1234'))

#------------------------------------------------------------------------------

def withdraw(accounts:list,amount:int)->list:
    for account in accounts:
        account['balance'] = account['balance'] - amount 
        
    return accounts
  
"""
This function is used to calculate balance.

Parameters
----------
accounts : list
    this is a list of bank account.
amount : int
    number of withdraw.
    
Returns
-------
accounts : list
    return update list.
"""  

accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]


print(withdraw(accounts, 1000))

#========================================================

def transactions_withdraw(accounts:list,amount:int,transactions:list)->list:    
    for account in accounts:
        account['balance'] = account['balance'] - amount 
        account['transactions'].append(amount)
        
    return accounts


"""
This function is used to calculate balance and transaction.

Parameters
----------
accounts : list
    this is a list of bank account.
amount : int
    number of withdraw.
transactions : list
    a list of withdraw.
    
Returns
-------
accounts : list
    return update list.
"""  


accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]


print(transactions_withdraw(accounts, 2000,[]))

#-------------------------------------------------------------

def deposit (accounts:list,deposit_amount:int)->list:
    for account in accounts:
        account['balance'] = account['balance'] + deposit_amount 
        
    return accounts


"""
This function is used to calculate balance.

Parameters
----------
accounts : list
    this is a list of bank account.
deposit_amount : int
    number of deposit.
    
Returns
-------
accounts : list
    return update list.
"""  


accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]


print(deposit(accounts, 1000))

#===================================================================

def transactions_deposit(accounts:list,deposit_amount:int,transactions:list)->list:    
    for account in accounts:
        account['balance'] = account['balance'] + deposit_amount 
        account['transactions'].append(deposit_amount)
        
    return accounts


"""
This function is used to calculate balance and transaction.

Parameters
----------
accounts : list
    this is a list of bank account.
deposit_amount : int
    number of deposit.
transactions : list
    a list of deposit.
    
Returns
-------
accounts : list
    return update list.
"""  


accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]


print(transactions_deposit(accounts, 3000,[]))

#------------------------------------------------------------------------

def show_transactions(account:dict)->list:
    transactions = account['transactions']
    
    return transactions
    
"""
This function is used to show transactions.

Parameters
----------
account : dictionary
    this is a dictionary of bank account.
    
Returns
-------
transactions : list
    return transactions list.
"""  
             
account = {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': [2000,7000]}


print(show_transactions(account = {
        'username': 'ali',
        'password': '1234',
        'balance': 5000,
        'transactions': [2000,7000]}))

#-----------------------------------------------------

def transfer(accounts:list, sender_username:str, receiver_username:str, amount:int)->list:
    
    for account in accounts:
        if account['username'] == sender_username :
            sender_username = account
        if account['username'] == receiver_username:
            receiver_username = account
    sender_username['balance'] -= amount
    receiver_username['balance'] += amount
    
    sender_username['transactions'].append(amount)
    receiver_username['transactions'].append(amount)
        
    return accounts

"""
This function is used to calculate transfer.

Parameters
----------
accounts : list
    this is a list of bank account.
sender_username : str
    name of sender.  
receiver_username : str
    name of receiver.
amount : int
    a number for transfer.
    
Returns
-------
accounts : list
    return update list.
"""  

accounts = [
    {
        'username': 'ali',

        'password': '1234',

        'balance': 5000,

        'transactions': []
    },
    {
        'username': 'sara',

        'password': '5678',

        'balance': 8000,

        'transactions': []
    }
]

print(transfer(accounts, 'ali', 'sara', 1000))

#================================================================

def get_balance(account:list,currency='USD')->int:
    balance = account['balance']
    if currency == 'RIAL':
        balance = account['balance'] * 240000
    
    return balance
    
"""
This function is used to get balance.

Parameters
----------
account : list
    this is a list of bank account.
currency : str
    by default is USD.if that is RIAL , calculate to dollar.
Returns
-------
balance : int
    return balance.
"""      
    
print(get_balance({
    'username': 'sara',

    'password': '5678',

    'balance': 8000,

    'transactions': []
},'RIAL'))

print(get_balance({
    'username': 'ali',

    'password': '1234',

    'balance': 5000,

    'transactions': []
}))