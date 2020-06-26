from Library import Library,PickingQuestions



END_ANSWERS=["no","n","stop","enough", "bye","bye!","ciao","arrivederci"]




if __name__ == "__main__":
    print("Welcome! This is Answer & Pick (AnsPick). Version 1.2.2    Author: Chinemo \n\n")
    print("Let's start!\n")

    while(True):
        book=Library('Questions','txt')
        book.ChoosingFile()
        #bisogna aggiungere qua la possibilità di andare a vedere se esiste una cache per il file creato
        PickingQuestions(book)
        ans=input("\nDo you want to open another file? (yes/no)").lower()
        if (ans in END_ANSWERS):
            break

    print("Congratulations (and good luck!)")
    print("Goodbye <3 ! ")
