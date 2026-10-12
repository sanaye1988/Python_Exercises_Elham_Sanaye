with open(r'C:\Users\Sanaye\Desktop\python_tamrin\number.txt','r') as file:
    sum_number = 0
    for number in file:
        try:
            new_number = int(number)
            sum_number += new_number
        except ValueError:
            raise ValueError('adad motabar nist.')
            
    print(sum_number)
        