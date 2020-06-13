from Library import Library,PickingQuestions
END_ANSWERS=["no","n","stop","enough", "bye","bye!","ciao","arrivederci"]




if __name__ == "__main__":
    print("Welcome! This is Answer & Pick (AnsPick). Version 1.1.0    Author: Chinemo \n\n")
    print("Let's start!\n")

    while(True):
        book=Library('Questions','txt')
        book.ChoosingFile()
        PickingQuestions(book)
        ans=input("\nDo you want to open another file? (yes/no)").lower()
        if (ans in END_ANSWERS):
            break

    print("Congratulations (and good luck!)")
    print("Goodbye <3 ! ")