#exercise 3


def employee_max_salary(employees:list)->str:
    
    maximum_salary = employees[0]['salary']
    name_employee = employees[0]['name']
    
    for employee in employees:
        if employee['salary'] > maximum_salary :
            maximum_salary = employee['salary']
            name_employee = employee['name']
    
    return name_employee
     
       
    
'''
This function is used to find name of employee that receives maximum salary.

Parameters
----------
employees : list
    this is list of employees.

Returns
-------
name_employee : str
    this is name of employee that receives maximum salary.

'''
     
    
    
employees = [
    {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
    
    ]


print(employee_max_salary(employees))

#------------------------------------------------------------------

def employee_min_salary(employees:list)->str:
    
    minimum_salary = employees[0]['salary']
    name_employee = employees[0]['name']
    
    for employee in employees:
        if employee['salary'] < minimum_salary :
            minimum_salary = employee['salary']
            name_employee = employee['name']
    
    return name_employee


'''
This function is used to find name of employee that receives minimum salary.

Parameters
----------
employees : list
    this is list of employees.

Returns
-------
name_employee : str
    this is name of employee that receives minimum salary.

'''


employees = [
    {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
    
    ]


print(employee_min_salary(employees))

#------------------------------------------------------------------------

def employee_max_3000(employees:list)->list:
    
    list_employees = []
    
    for employee in employees:
        if employee['salary'] > 3000 :
            list_employees.append(employee['name'])
    
    return list_employees



'''
This function is used to find name of employee that receives above 3000 salary.

Parameters
----------
employees : list
    this is list of employees.

Returns
-------
list_employees : list
    this is list of employees that receives above 3000 salary.

'''


employees = [
    {
        "name": "Ali",
        "age": 28,
        "salary": 3200
    },

    {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
    
    ]


print(employee_max_3000(employees))


#-------------------------------------------------------------------------

def employee_check_salary(employees:list,number:int)->list:
    
    list_employees = []
    
    for employee in employees:
        if employee['salary'] > number :
            list_employees.append(employee['name'])
    
    return list_employees



''' 
 This function is used to find name of employees that receives above the specified salary.

 Parameters
 ----------
 employees : list
     this is list of employees..
 number : int
     this is the specified salary.

 Returns
 -------
 list_employees : list
     this is list of employees that receives above the specified salary.

'''


employees = [
    {
        "name": "Ali",
        "age": 28,
        "salary": 3200
    },

    {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
    
    ]


print(employee_check_salary(employees,3000))

#------------------------------------------------------------

def average_salary(employees:list)->int :
    
    salary = 0
    count = 0
    
    for employee in employees:
        salary += employee['salary']
        count += 1
        average = salary / count
        
    return average

'''
This function is used to find average of salaries.

Parameters
----------
employees : list
    this is list of employees.

Returns
-------
average : int
    this is list of average of salaries.

'''

employees = [
    {
        "name": "Ali",
        "age": 28,
        "salary": 3200
    },

    {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
    
    ]


print(average_salary(employees))

#----------------------------------------------------

