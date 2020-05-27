import random

with open("Questions.txt",'r') as file: 
    lista=file.readlines()
    lista = [x.replace('\n', '') for x in lista]

ask=''
forblist=[]
finished=False
print("Welcome! This is Answer & Pick (AnsPick). Version 1.0.1    Author: Chinemo \n\n\n")
while (ask.lower() != "stop" and ask.lower() !='no' and ask.lower() != 'n' and finished == False):
    while True:
        pick=random.randint(0,len(lista)-1)
        if forblist.count(pick) == 0:
            forblist.append(pick)
            break
        else:
            if len(forblist)==len(lista):
                finished=True
                break
    if (finished == False):
        print("Question: " + str(lista[pick]))
        ask=(input("\nDo you want to continue? (y/n)").lower())
    else:
        break
print( "----------------------------------------------\n\n\n")
print("Questions finished! You have done it!")
print("Congratulations (and good luck!)")

    
