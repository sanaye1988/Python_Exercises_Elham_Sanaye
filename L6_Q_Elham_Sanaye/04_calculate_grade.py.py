#4_calculate_grade


def list_nomre(nomreh:int)-> str:
    if 90 <= nomreh <= 100:
        nomreh = 'A'
        return nomreh
    elif 80 <= nomreh <= 89:
        nomreh = 'B'
        return nomreh
    elif 70 <= nomreh <= 79:
        nomreh = 'C'
        return nomreh
    elif 60 <= nomreh <= 69:
        nomreh = 'D'
        return nomreh
    elif nomreh < 60:
        nomreh = 'F'
        return nomreh
    
    
'''
ye tabe neveshtam ke ye vorodi dare, nomreye daneshjoo ro migire,
ba tavajoh be shart check mikone ke dar kodom baze hast va 
emtiaze dorost ro barmigardone.

'''


    
adad = list_nomre(75)
print(adad)