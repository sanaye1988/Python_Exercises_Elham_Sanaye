cost_list = [100,200,360,458,259,900]

new_list = []

for i in cost_list:
    i = i + i * 0.1
    new_list.append(i)
    
print(new_list)