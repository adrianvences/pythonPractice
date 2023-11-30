import random 

names_string = "Adrian,David,julio,Selvin"

name = names_string.split(",")

num_names = len(name)

print(name , num_names)

random_name = random.randint(0, num_names-1)

print(random_name)

personWhoWillBuy = name[random_name]

print(personWhoWillBuy + " va invitar las miches.")

