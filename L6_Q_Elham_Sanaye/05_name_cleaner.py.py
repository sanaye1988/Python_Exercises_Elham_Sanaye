#5_name_cleaner

def check_name(name:str , lastname:str)->str:
    name = name.strip().title() + " " +  lastname.strip().title()
    return name


'''
tabei neveshtam ke esme kamele karbar ro begire 
va fasele ha ro hazf kone,va harfe avale hamaro bozorg namayesh bede
va dar nahayat esme dorost ro khoroji pas bede

'''


name = check_name('  amiR','  amiri jafAri    ')
print(name)


#----------------------------------------------------------

'''
in tabe ra be do soorat neveshtam 
yeki ba ye vorodi ke esme kamel ro begire
yeki ham ba do vorodi ke esm va famili ro joda begire

'''

def check_name(full_name:str)->str:
    name = full_name.strip().title()
    return name



name = check_name('  elHam sanAye   ')
print(name)



