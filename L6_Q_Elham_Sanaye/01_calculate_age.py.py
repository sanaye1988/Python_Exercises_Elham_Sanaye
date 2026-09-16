#1_calculate_age
#a--------------------------------------------

emsal = 2026

def calculate_age(sale_tavalod:int) -> int :
    age = emsal - sale_tavalod
    return age

'''
ye tabe neveshtam baraye mohasebe sene karbar,
ye vorodi migire be esme sale tavalod,
sali ke dar an hastim ro az ghabl tarif kardam,
baraye mohasebeye sen sale tavalod ra az sale kononi kam mikoniam.

'''

sen = calculate_age(1988)
print(sen)


#b------------------------------------------

sale_shamsi = 1405

sale_miladi = 2026

def calculate_tarikh(sale_tavalod:int , tarikh:str) -> int :
    if tarikh == 'shamsi':
        age = sale_shamsi - sale_tavalod
        return age
    elif tarikh == 'miladi':
        age = sale_miladi - sale_tavalod
        return age
    else:
        raise ValueError('sale tavalod ra be dorosti vared nakardid!!')
    
    
'''
ye tabe neveshtam baraye mohasebe sene karbar,
2 vorodi migire be esme sale tavalod va tarikhe shamsi ya miladi,
sali ke dar an hastim ro az ghabl tarif kardam che shamsi che miladi,
baraye mohasebeye sen sale tavalod ra az sale kononi kam mikoniam.

'''

    
sen = calculate_tarikh(1367, 'shamsi')
print(sen)

sen = calculate_tarikh(1988, 'miladi')
print(sen)


#c----------------------------------------

sale_shamsi = 1405

sale_miladi = 2026

def calculate_tarikh(sale_tavalod , tarikh = 'miladi')->int:
    if tarikh == 'shamsi':
        age = sale_shamsi - sale_tavalod
        return age
    elif tarikh == 'miladi':
        age = sale_miladi - sale_tavalod
        return age
    else:
        return None
    
    
'''
baraye tarikh default sazi shode ke 
age karbar tarikh ra vared nakard ,
tabe besoorate pish farz miladi hesab konad.

'''
    
    
sen = calculate_tarikh(1988)
print(sen)


#d----------------------------------------------

sale_shamsi = 1405

sale_miladi = 2026

def calculate_tarikh(tarikh:int)->int:
    if 1300 <= tarikh <= 1405:
        age = sale_shamsi - tarikh
        return age
    elif 1900 <= tarikh <= 2026:
        age = sale_miladi - tarikh
        return age
    else:
        raise ValueError('sale tavalod ra be dorosti vared nakardid!!')
        
        
'''
ye tabe neveshtam baraye mohasebe sene karbar,
ye vorodi migire be esme tarikh,tabe dar baze haye khasi check mikone 
va ba tavajoh be baze tashkhis mide ke shamsi hast ya miladi 
va sen ro mohasebe mikone.
'''    
        
        
sen = calculate_tarikh(1400)
print(sen)

sen = calculate_tarikh(1980)
print(sen)