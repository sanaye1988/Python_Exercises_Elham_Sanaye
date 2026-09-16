#8_count_letter

def count_letter(word:str , letter:str )-> int:
    count = 0
    
    for i in word:
        if i == letter:
            count += 1
    return count
    

'''
ye tabe sakhtam k do vorodi migire, yeki kalame va yeki harf,
ba estefade az halghe for done done horofe kalame ra check mikonad,
agar horofe kalame ba harfe vared shode barabar bashad,
be shomarande yeki ezafe mishavad.
'''
    
count = count_letter('ergrtg', 'g')
print(count)

#------------------------------------------------------------------

'''
hamin tabe ra bedone for neveshtam
az tabe count estefade kardan ke harfe vared shode ra beshmore 
va pas bede

'''

def count_letter(word:str , letter:str )-> int:
    
    count = word.count(letter)
    
    return count
    
   

count = count_letter('dfvgdfgvb', 'g')
print(count)
