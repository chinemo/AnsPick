import os
import glob
import random
#from functools import partial

#print=partial(print,flush=True)
#printf=functools.partial(print, flush=True)
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
        cleaned_title=extractTitle(mylist[0],path,ext)
        print("Opening the only file inside the folder: "+ str(cleaned_title))
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
    """it is the function that has to pick and shows the questions

    Args:
        file (file): it is the file that it has to read
    """
     
    questions=file.readlines()  #it extracts the lines  
    questions = [x.replace('\n', '') for x in questions] #it separates the lines with \n
    questions= list(filter(None, questions)) #it removes all the empty elements
    ask=''
    
    score=0
    wrong_answers=[]

    scrumbled_questions = random.sample(questions,len(questions))
    counter =1
    dimension=len(scrumbled_questions)

    for question in scrumbled_questions:
        print("\nQuestion: " + question)
        ask=(input("\nHave you answered correctly(Be honest)? (y/n):  \n>>>").lower())
        if (ask not in NEGATIVE_ANSWERS):
                score += 1
        else:
            wrong_answers.append(question)
        
        if counter != dimension:
            print("\nActual Score: " + str(score) + " / " + str(counter) + "\n")
        
        counter += 1
    
    
    #print = partial(print, flush=False)
    print( "\n----------------------------------------------\n\n\n")
    print("Questions finished!")
    print("You have answered: (" + str(score) + " / " + str(dimension)+  ") questions !!")
    percentage=float(score/dimension*100)
    percentage=round(percentage)
    print(str(score) + "/" + str(dimension)+ " -->  "+str(percentage) +  " %")
    print("You should repeat: \n")
    for wrong_answer in wrong_answers :
        print( wrong_answer + "\n")
    

        
