with open(r'C:\Users\Sanaye\Desktop\python_tamrin\data.txt','r',encoding='UTF-8') as file:
    
    new_file = file.read()
    
    line = len(new_file.splitlines())
    word = len(new_file.split())
    char = len(new_file)
    
    print(f'تعداد خطوط: {line}')
    print(f'تعداد کلمات: {word}')
    print(f'تعداد حروف: {char}')
    
 
