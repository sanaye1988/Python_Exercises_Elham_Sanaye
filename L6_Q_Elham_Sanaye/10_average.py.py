#10_average

def calculate_average(my_list:list) -> float:
    total = 0
    count = 0
    for number in my_list:
        total = total + number
        count += 1
        average = total / count
    return average
    

'''
ye tabe neveshtam baraye mohasebe miangine adade dakhele list,
ye vorodi az jense list migire,ba halghe for,har adad ro be ezafe adade ghabli mikone,
va mirize dar total,va har adad ro mishmore ba estefade az count,
dar akhar majmooe adad ro taghsim bar tedad mikone va miangin ro be dast miare

'''
        

my_list = [13,78,43,29,12,6]
ave = calculate_average(my_list)
print(ave)
    