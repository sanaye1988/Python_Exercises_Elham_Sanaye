#9_find_max

def find_max(my_list:list)->int:
    max_number = my_list[0]
    for number in my_list:
        if number > max_number:
            max_number = number
    return max_number
        

'''
ye tabe neveshtam k ye vorodi migire ke listi az adade,
bozorgtarin adad ro bayad peida kone,
dar ebteda avalin adad ro be onvane bozorgtarin adad entekhab mikone,
be ezaye har adad dar list shart ro har bar check mikone,
ke age adade dakhele list az bozorgtarin adade avali bozorgtar bood
ono bargardone

'''

        
my_list = [3,100,8,85,75,0,-9,172]

Max = find_max(my_list)

print(Max)

