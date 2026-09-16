information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

information.clear()

print(information)

#pak mikone dakhele reshte ra

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

information.copy()

print(information)

#ye copy migire azash

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

print(information.get('reshte_tahsili'))

#value e iteme moshakhas shode ra midahad.

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

print(list(information.keys()))

#liste key haro mide

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

print(list(information.values()))

#liste value haro mide

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software'}

information.update({'lastname':'sanaye'})

print(information)

#iteme jadid ezafe mikone ya ghabli haro taghir mide.

information = {'name':'elham', 'age':37, 'reshte_tahsili':'software', 'lastname': 'sanaye'}

information.pop('lastname')

print(information)

#iteme morede nazar ra hazf mikonad.
