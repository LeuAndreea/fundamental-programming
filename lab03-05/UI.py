'''
Created on Oct 27, 2018

@author: Leut
'''
import logic

def printMenu( ):
    s= "Menu:" + '\n'
    s+= '\t' + "1-Add a new score" + '\n'
    s+= '\t' + "2-Insert score at index" + '\n'
    s+= '\t' + "3-Remove score from  index" + '\n'
    s+= '\t' + "4-Remove scores between indices" + '\n'
    s+= '\t' + "5-Replace score at index with another value" + '\n'
    s+= '\t' + "6-Print scores less than a number" + '\n'
    s+= '\t' + "7-Print all scores sorted" + '\n'
    s+= '\t' + "8-Print all scores greater than a number,sorted" + '\n'
    s+= '\t' + "9-Print the average score for participants between two indices" + '\n'
    s+= '\t' + "10-Print the smallest score between two indices" + '\n'
    s+= '\t' + "11-Print scores which are multiples of a number" + '\n'
    s+= '\t' + "12-Keep only scores which are multiples of a number" + '\n'
    s+= '\t' + "13-Keep only scores greater than a number" + '\n'
    s+= '\t' + "14-Undo the last operation" + '\n'
    s+= '\t' + "15-View scores." + '\n'
    s+=' \t' + "16-Read a list of scores from a file of your choice" + '\n'
    s+= '\t' + "17-Write the current list to a file of your choice" + '\n'
    s+= '\t' + "0-Exit." + '\n'
    
    print(s)

def addSubMenu(participants):
    score=int(input("Type in the score you want to add:"))
    logic.addNewScore(participants, score)
    print("Score successfully added")

def insertSubMenu(participants):
    index=int(input("Type in the index at which you wish to introduce the score:"))
    score=int(input("Type in the score you want to insert:"))
    if index > 0 and index <= len(participants): 
        logic.insertNewScore(participants, index-1,score)
        print("Score successfully inserted")
    else:
        print("Invalid index.")

def removeOneSubMenu(participants):
    index=int(input("Type in the index of the score you want to remove"))
    if index > 0 and index <= len(participants): 
        logic.removeScore(participants, index-1)
        print("Score successfully removed")
    else:
        print("Invalid index.")
        
def removeMultipleSubMenu(participants):
    stindex=int(input("Type in the start index: "))
    fnindex=int(input("Type in the finish index: "))
    if stindex > 0 and fnindex <= len(participants) and fnindex-stindex >0: 
        logic.removeMultipleScores(participants, stindex-1, fnindex-1)
        print("Scores successfully removed")
    else:
        print("Invalid indices.")

def replaceSubMenu(participants):
    index=int(input("Type in the index :"))
    score=int(input("Type in the new score "))
    if index>0 and index<=len(participants):
        logic.replaceScore(participants,  index-1,score)
        print("Score succesfully replaced.")
    else:
        print("invalid index.")

def  printLessSubMenu(participants):
    x = int(input("Type in the number:"))
    scores = logic.findLessThan(participants, x)
    if (scores!=[]):
        print("Scores less than "+ str(x) + " are: " + logic.listToString(scores) + '\n')
    else:
        print("No scores are less than " + str(x))

def printSortedSubMenu(participants):
    scores=logic.sortList(participants)
    print("The sorted list is :  " + logic.listToString(scores)  + '\n')

def printSortedGreaterThanSubMenu(participants):
    x = int(input("Type in the number: "))
    scores= logic.sortGreaterThan(participants, x)
    if scores!=[ ] :
        print("Numbers greater than " + str(x) + " sorted are " + logic.listToString(scores)+ '\n')
    else:
        print("There are no scores greater than " + str(x))

def printAverageSubMenu(participants):
    stindex=int(input("Type in the start index: "))
    fnindex=int(input("Type in the finish index: "))
    if stindex > 0 and fnindex <= len(participants) and fnindex-stindex >0: 
        average=logic.findAverage(participants,stindex-1, fnindex-1 )
    print("The average score between indices " +str(stindex) + " and " + str(fnindex) + " is " + str(average))

def printMinSubMenu(participants):
    stindex=int(input("Type in the start index :")) 
    fnindex=int(input("Type in the finish index:")) 
    minimum=logic.findMin(participants,stindex-1,fnindex-1)
    print("The minimum between " + str(stindex) + " and " + str(fnindex) + " is " + str(minimum) + '\n')

def printMultiplesOfSubMenu(participants):
    stindex=int(input("Type in the start index :"))
    fnindex=int(input("Type in the finish index:"))
    x = int(input("Type in the number: "))
    scores=logic.findMultiplesOf(participants, stindex-1, fnindex-1, x)
    print("Multiples of " + str(x) + " between " + str(stindex) + " and  " + str(fnindex) + " are " + logic.listToString(scores))

def filterMultiplesOfSubMenu(participants):
    x = int(input("Type in the number: "))
    logic.filterMultiplesOf(participants,x)
    print("Numbers which are not multiples of " +str( x) + " succesfully deleted" + '\n')

def filterGreaterThanSubMenu(participants):
    x = int(input("Type in the number: "))
    logic.filterGreaterThan(participants,x)
    print("Numbers less than " + str(x) + " succesfully deleted." + '\n')
    
def undoOperationSubMenu(operations,participants):
    logic.undoOperation(operations,participants)
    print("Undo succesful!")

def printListSubmenu(participants):
    print(logic.listToString(participants))

def readFromFileSubMenu():
    filename=input("Introduce the name of the file:")
    try:
        f= open(filename,"r")
        participants=f.read()
        participants=participants.split(" ")
        f.close()
        
        for el in participants:
            el=int(el)

    except IOError as e1:
        print("Something was wrong with the file" +str(e1))
    except ValueError as e2:
        print("Something is wrong as value" + str(e2))
    return participants

def writeToFileSubMenu(participants):
    filename=input("Introduce the name of the file:")
    try:
        f=open(filename,"w")
        for el in participants:
            f.write(str(el) + " ")
        f.close()
    except IOError as e1:
        print("Something was wrong with the file" +str(e1))
    except ValueError as e2:
        print("Something is wrong as value" + str(e2))

def start():
    participants=[ ]
    operations=[  ]    
    option=int(input("Select option: " ))
    while (option!=0):
        if option==1:
            addSubMenu(participants)
        elif option==2 :
            insertSubMenu(participants)
        elif option==3 :
            removeOneSubMenu(participants)
        elif option==4 :
            removeMultipleSubMenu(participants)
        elif option==5 :
            replaceSubMenu(participants)
        elif option==6 :
            printLessSubMenu(participants)
        elif option==7 :
            printSortedSubMenu(participants)
        elif option==8 :
            printSortedGreaterThanSubMenu(participants)
        elif option==9 :
            printAverageSubMenu(participants)
        elif option==10 :
            printMinSubMenu(participants)
        elif option==11 :
            printMultiplesOfSubMenu(participants)
        elif option==12 :
            filterMultiplesOfSubMenu(participants)
        elif option==13 :
            filterGreaterThanSubMenu(participants)
        elif option==14 :
            undoOperationSubMenu(operations,participants)
        elif option==15:
            printListSubmenu(participants)
        elif option==16:
            participants=readFromFileSubMenu()
        elif option==17:
            writeToFileSubMenu(participants)
        else:
            print("Invalid option!")
          
        logic.storeOperations(operations,participants)
        input()
        printMenu( )
        option=int(input("Select option: " ))

printMenu()
start()
