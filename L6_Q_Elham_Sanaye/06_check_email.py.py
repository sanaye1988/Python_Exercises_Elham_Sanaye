#6_check_email

def check_email(email:str) -> str :
    if '@' in email and '.com' in email and ' ' not in email:
        return True
    else:
        return False
    

    
'''
tabei neveshtam ke ye email be onvane vorodi begire 
check kone ke age sharthaye email ro dasht True bargardone,
age na False

'''

email = check_email('sanaye.elham88@gmail.com')
print(email)


