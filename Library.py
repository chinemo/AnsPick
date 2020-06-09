import os
import glob
import random

REPOSITORY="Questions"
EXTENSION='.txt'
#RESOURCES=REPOSITORY+EXTENSION

NEGATIVE_ANSWERS=["nie","no","wrong","I made a mistake","ops","no, sorry.","n", "0"]


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
            if 1<=answer<=counter:
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
    score=0
    wrong_answers=[]
    while ( finished == False):
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
            ask=(input("\nHave you answered correctly(Be honest)? (y/n):  ").lower())
            if (ask not in NEGATIVE_ANSWERS):
                score += 1
            else:
                wrong_answers.append(questions[pick])

            if(len(forblist) != len(questions)):
                print("Actual Score: " + str(score) + " / " + str(len(forblist)) + "\n")
            

        else:
            break
    print( "\n----------------------------------------------\n\n\n")
    print("Questions finished!")
    print(" You have answered: (" + str(score) + " / " + str(len(questions))+  ") questions !!")
    percentage=float(score/len(questions)*100)
    percentage=round(percentage)
    print(str(score) + " / " + str(len(questions))+ "--> "+str(percentage) +  " %")
    print("You should repeat: ")
    for wrong_answer in wrong_answers :
        print( wrong_answer + "\n")
    

        
