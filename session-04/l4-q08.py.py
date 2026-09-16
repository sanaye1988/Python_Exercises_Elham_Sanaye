users = ['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']

count = 0

for i in users:
    if len(i) < 5:
        count = count + 1
        
print(count)