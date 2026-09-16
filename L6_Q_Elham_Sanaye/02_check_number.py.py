#2_check_number
#a---------------------------------------------

def zoj_fard(number:int)->str:
    if number % 2 == 0:
        number = 'even'
        return number
    if number % 2 != 0:
        number = 'odd'
        return number
  
'''
ye tabe neveshtam baraye tashkhise zoj ya fard boodane adade karbar,
mohasebe mikone, age baghimande bar 2 sefr shod zoj barmigardone
va age sefr nabood fard ra barmigardone

'''
    
adad = zoj_fard(6)
print(adad)


#b--------------------------------------------------

def zoj_fard(number:int) -> bool:
    if number % 2 == 0:
        return True
    if number % 2 != 0:
        return False

'''
ye tabe neveshtam baraye tashkhise zoj ya fard boodane adade karbar,
mohasebe mikone, age baghimande bar 2 sefr shod va zoj bod True
va age fard bood False barmigardone

'''
    
adad = zoj_fard(7)
print(adad)


#c----------------------------------------

def mosbat_manfi(number:int)->str :
    if number > 0:
        number = 'positive'
        return number
    elif number < 0:
        number = 'negative'
        return number
    else:
        number = 'zero'
        return number
   

'''
ye tabe neveshtam baraye tashkhise mosbat manfi bodane adad,
mire shart ro check mikone, age balaye sefr bod positive pas mide,
age zire sefr bod negative pas mide va age sefr bood
sefr barmigardone.

'''


adad = mosbat_manfi(0)
print(adad)

adad = mosbat_manfi(-7)
print(adad)