students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

new_list = []

for student,score in zip(students,scores):
    if score >= 14:
        print(student)
        new_list.append(student)
        
       
        
       
#---------------------------------------------------

students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

new_list = []

for student,score in zip(students,scores):
    if score >= 14:
        print(student)
        print(score)
        new_list.append(score)
        
print(new_list)
        
print(sorted(new_list))