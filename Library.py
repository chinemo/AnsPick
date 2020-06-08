import os
import glob
import random

REPOSITORY="Questions"
EXTENSION='.txt'
#RESOURCES=REPOSITORY+EXTENSION

def checkfolder(path=REPOSITORY):
    if (os.path.exists(path)== False):
        os.makedirs(path)

def extractTitle(title,path=REPOSITORY,ext=EXTENSION,):
    fullpath=path+"\\"
    title=title.replace(fullpath,'')
    title=title.replace(ext,'')
    return title

def readfile(path,ext,mylist):
    checkfolder(path)

    
    dimension=len(mylist)
    
    if(dimension==0):
        #print("There is no file inside the resource file")
        return -1

    if(dimension==1):
        print("Opening the only file inside the folder: "+ str(mylist[0]))
        return 0

    else:
        print("\nWhich file do you want to open ? ")
        counter=0
        for title in mylist:
            counter += 1
            cleaned_title=extractTitle(title,path,ext)
            print(str(counter) + ". " + cleaned_title)
        while(True):
            answer=input(">>>")
            answer=int(answer)
            if answer in range(1,counter):
                break
            else:
                print("Insert a correct number!")
                answer=input(">>>")
        return (answer-1)

def OpenFile(path=REPOSITORY,ext=EXTENSION):
    
    mylist = [f for f in glob.glob(path+"/*"+ext)]
    counter=readfile(path,ext,mylist)
    if counter==-1:
        print("There are no "+ ext+ " files into the "+path +" folder!")
        return False
    else: 
        with open(mylist[counter],'r') as file:
            PickingQuestions(file)
        return True

    
def PickingQuestions(file): 
    questions=file.readlines()
    questions = [x.replace('\n', '') for x in questions]

    ask=''
    forblist=[]
    finished=False
    
    while (ask.lower() != "stop" and ask.lower() !='no' and ask.lower() != 'n' and finished == False):
        while True:
            pick=random.randint(0,len(questions)-1)
            if forblist.count(pick) == 0:
                forblist.append(pick)
                break
            else:
                if len(forblist)==len(questions):
                    finished=True
                    break
        if (finished == False):
            print("\nQuestion: " + str(questions[pick]))
            ask=(input("\nDo you want to continue? (y/n):  ").lower())
        else:
            break
    print( "----------------------------------------------\n\n\n")
    print("Questions finished! You have answered:" + str( len(forblist)) +  " questions !!")
    

        