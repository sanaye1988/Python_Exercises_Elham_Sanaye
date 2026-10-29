def add_grades():
    name = input('enter name:')
    grade = int(input('enter grade:'))
    try:
        with open('grades.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{name},{grade}\n')
    except ValueError:
        raise ValueError('The grade is outside of range.')
    except TypeError:
        raise TypeError('enter integer number for grade not text.')
       
    
def read_grades():
    try:
        with open('grades.txt', 'r', encoding='UTF-8') as file:
            grades_file = file.read()
            print(grades_file)
    except FileExistsError:
        raise FileExistsError('file not exist.')
        
        
def calculate_average():
    sum_grades = 0
    count = 0
    try:
        with open('grades.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                new_list = line.strip().split(',')
                sum_grades += float(new_list[1])
                count += 1  
                
            average_grades = sum_grades/count
            print(average_grades)
    except FileExistsError:
        raise FileExistsError('file not exist.')
    except Exception:
        print('information is not right.')            


def find_top_student():
    try:
        with open('grades.txt', 'r', encoding='UTF-8') as file:
            new_line = file.readline().split(',')
            max_grade = float(new_line[1])
            top_student = new_line[0]
            for line in file:
                new_list = line.split(',')
                name = new_list[0]
                grade = float(new_list[1])
                if grade > max_grade:
                    max_grade = grade
                    top_student = name                   
            
            print(f'top student is: {top_student}')
                    
    except FileExistsError:
        raise FileExistsError('file not exists.')

