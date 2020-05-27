import random

with open("Questions.txt",'r') as file: 
    lista=file.readlines()
    lista = [x.replace('\n', '') for x in lista]

ask=''
forblist=[]
print("Welcome! This is Answer & Pick (AnsPick). Version 1.0.1    Author: Chinemo ")
while (ask.lower() != "stop" and ask.lower() !='no' and ask.lower() != 'n'):
    while True:
        pick=random.randint(0,len(lista)-1)
        if forblist.count(pick) == 0:
            forblist.append(pick)
            break
        else:
            if len(forblist)==len(lista):
                print("Questions finished! You have done it!")
                quit()
    print("Question: " + str(lista[pick]))
    ask=(input("Do you want to continue? (y/n)").lower())


    
