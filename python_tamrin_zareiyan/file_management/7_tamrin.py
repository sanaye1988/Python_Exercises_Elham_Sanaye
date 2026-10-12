import os

file_name = 'tamrin.txt'

if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        file_read = file.read()
        print(file_read)
        
else:
    with open(file_name, 'w') as file:
        raise ValueError('file mojood nabod, baraye shoma sakhte shod!')