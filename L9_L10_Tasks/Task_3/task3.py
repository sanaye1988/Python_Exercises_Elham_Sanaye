import os
import math

def exists_path(user_path):   
    if os.path.exists(user_path):
        return True


def show_name_files(user_path):
    return os.listdir(user_path)

def calculate_count_files(user_path):
    list_dir = os.listdir(user_path)
    count = 0
    for file in list_dir:
        count += 1
    return count

def calculate_mass_files(user_path):
    list_dir = os.listdir(user_path)
    for file in list_dir:
        path_size = os.path.getsize(file) / 1024
        print(f'{file} : {path_size}')   
        
    ceil_number = math.ceil(path_size)
    print(ceil_number)
 
def calculate_sum_and_average_mass_files(user_path):
    list_dir = os.listdir(user_path)
    total_file = 0
    count = 0
    for file in list_dir:
        path_size = os.path.getsize(file) / 1024
        total_file += path_size
        count += 1
        average_mass = total_file/count
        print(f'sum_mass: {total_file}')
        print(f'average_mass: {average_mass}') 
    
    round_sum = math.ceil(total_file)
    round_average = math.ceil(average_mass)
    print(round_sum)
    print(round_average)

calculate_sum_and_average_mass_files(r"C:\Users\Sanaye\Desktop\L9_L10_Tasks\Task_3")

def find_max_min_files(user_path):
    list_dir = os.listdir(user_path)

    size_files = {}
    
    for file in list_dir:
        full_path = os.path.join(user_path, file)
        
        if os.path.isfile(full_path):
            size_files[file] = os.path.getsize(full_path)
            
    if size_files:
        big_file = max(size_files,key=size_files.get)
        small_file = min(size_files,key=size_files.get)
        
        print(f'biggest file is : {big_file},size:{size_files[big_file]}')
        print(f'smallest file is : {small_file},size:{size_files[small_file]}')
    else:
        print('no file is available!')
        
    
def count_formats(user_path):
    
    format_count = {}
    list_dir = os.listdir(user_path)
    
    for file in list_dir:
        full_path = os.path.join(user_path, file)
        
        if os.path.isfile(full_path):
            format_file = os.path.splitext(file)[1]
            
            if format_file in format_count:
                format_count[format_file] += 1
            else:
                format_count[format_file] = 1
                
    for format_file, count in format_count.items():
        print(f'{format_file}:{count}')


def save_report(user_path):
    report_file = os.path.join(user_path, 'report')
    os.makedirs(report_file, exist_ok=True)
    
    report_path = os.path.join(report_file, 'report.txt')
    
    with open(report_path,'w') as file:
        file.write('report\n')
    
    return report_path
           
