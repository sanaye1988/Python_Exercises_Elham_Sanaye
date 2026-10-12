with open(r'C:\Users\Sanaye\Desktop\python_tamrin\new_file.txt','r') as file:
    new_file = file.read()
    
    upper_file = new_file.upper()

with open(r'C:\Users\Sanaye\Desktop\python_tamrin\upper_file.txt','w') as file:
    file.write(upper_file)
    
print(upper_file)