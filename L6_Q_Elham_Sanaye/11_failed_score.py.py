#11_failed_score
#a-----------------------------------------------


def pass_score(list_nomreh:list) -> list:
    new_list = []
    for nomreh in list_nomreh:
        if nomreh < 12:
            continue
        if nomreh >= 12:
            new_list.append(nomreh)
    return new_list
    

'''
ye tabe sakhtam ke ye vorodi az jense list begire,
ke nomrehaye daneshjoo ha hast,nomrehaye zire 12 ro hazf kone,
balaye 12 ke ghabool shodan ro be liste jadid ezafe kone

'''


list_nomreh = [15,17,20,9,18,11,8]
new_list = pass_score(list_nomreh)
print(new_list)


#b----------------------------------------------------

def failed_score(list_nomreh:list) -> list:
    new_list = []
    for nomreh in list_nomreh:
        if nomreh >= 12:
            continue
        if nomreh < 12:
            new_list.append(nomreh)
    return new_list


'''
dar in tabe ye vorodi az jense list begire,
ke nomrehaye daneshjoo ha hast,nomrehaye balaye 12 ro hazf kone,
paein tar az 12 ke failed shodan ro be liste jadid ezafe kone

'''


list_nomreh = [15,17,20,9,18,11,8]
new_list = failed_score(list_nomreh)
print(new_list)


#c---------------------------------------------------------------------

def count_pass_score(list_nomreh:list) -> list:
    count = 0
    for nomreh in list_nomreh:
        if nomreh < 12:
            continue
        if nomreh >= 12:
            count += 1
    return count

'''
dar in tabe ye vorodi az jense list begire,
ke nomrehaye daneshjoo ha hast,
tedade nomrehaye balaye 12 ke ghabool shodan ro beshmore va pas bede

'''


list_nomreh = [15,17,20,9,18,11,8]
count = count_pass_score(list_nomreh)
print(count)