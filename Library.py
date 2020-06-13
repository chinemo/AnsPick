import os
import glob
import random

REPOSITORY="Questions"
EXTENSION='txt'
#RESOURCES=REPOSITORY+EXTENSION

NEGATIVE_ANSWERS=["nie","no","wrong","I made a mistake","ops","no, sorry.","n", "0"]

def checkfolder(path=REPOSITORY):
    if (os.path.exists(path)== False):
        os.makedirs(path)


class Library():   
    def __init__(self,path=REPOSITORY,ext=EXTENSION):
        self.path=path
        checkfolder(self.path)
        self.ext='.'+ext
        self.mylist = [f for f in glob.glob(path+"/*"+ext)]
        self.counter=-1
        self.dimension=len(self.mylist)
        self.questions=[]
    
    def extractTitle(self,title):
        fullpath=self.path+"\\"
        title=title.replace(fullpath,'')
        title=title.replace(self.ext,'')
        return title

    def ChoosingFile(self):       
        if(self.dimension==0):
            #print("There is no file inside the resource file")
            self.counter=-1
            self.chosenfile=''
            return False
        if(self.dimension==1):
            title=self.mylist[0]
            cleaned_title=self.extractTitle(title)
            print("Opening the only file inside the folder: "+ str(cleaned_title))
            self.counter=0
            self.chosenfile=self.mylist[0]
            self.__scrubblingQuestions__()
            return True

        else:
            print("\nWhich file do you want to open ? ")
            self.counter=0
            for title in self.mylist:
                self.counter += 1
                cleaned_title=self.extractTitle(title)
                print(str(self.counter) + ". " + cleaned_title)
            while(True):
                answer=input(">>>")
                if answer.isnumeric() ==False:
                    print("Insert a number!!")
                    #answer=input(">>>")
                else:
                    answer=int(answer)
                    if 1<=answer<=self.counter:
                        break
                    else:
                        print("Insert a correct number!")
                        #answer=input(">>>")
             
            self.counter=(answer-1)
            self.chosenfile=self.mylist[self.counter]
            self.__scrubblingQuestions__()
            return True

    def __scrubblingQuestions__(self):
        if(self.chosenfile != ''):
            with open(self.chosenfile, 'r') as file:
                questions=file.readlines()  #it extracts the lines  
            
            questions = [x.replace('\n', '') for x in questions] #it separates the lines with \n
            questions= list(filter(None, questions)) #it removes all the empty elements
            self.questions= random.sample(questions,len(questions))
            print("Questions scrumbled")
        else:
            print("Error, no file has been picked (NO INSIDE THE OBJECT!)!")

    



    
def PickingQuestions(library): 
    """it is the function that has to pick and shows the questions

    Args:
        file (file): it is the file that it has to read
    """
    ask=''    
    score=0
    wrong_answers=[]

    scrumbled_questions = library.questions
    counter =1
    dimension=len(scrumbled_questions)

    for question in scrumbled_questions:
        #print( "\033[H\033[J")    
        print("\nQuestion: " + question)
        ask=(input("\nHave you answered correctly(Be honest)? (y/n):  \n>>>").lower())
        if (ask not in NEGATIVE_ANSWERS):
                score += 1
        else:
            wrong_answers.append(question)
        
        if counter != dimension:
            print("\nActual Score: " + str(score) + " / " + str(counter) + "\n")
        
        counter += 1
    
    #print( "\033[H\033[J")    
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
    

        
