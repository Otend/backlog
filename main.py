# -*- coding: utf-8 -*-
#Backlog Manager
#programmed by Ian Hitterdal (otend)
#licensed under MIT license
import work
import random


def addWork(medium):
#input: valid medium string
#user input: work title string
#output: none
#user output: none, really
    global workDict
    global mediumList
    if medium not in mediumList:
        print("Invalid medium, otend did something wrong")
    else:
        inName = input("What is the name of the work? ")
        workDict[medium].append(work.Work(inName))


def pickMedium():
#input: none
#user input: integer to choose a medium from the list
#output: valid medium string
    global mediumList
    print("Which medium would you like to use?")
    n = 1
    for med in mediumList:
        print(n,". ",med)
        n = n+1
    choice = int(input("Enter a number. "))
    return mediumList[choice-1]

def chooseWork(medium):
#input: valid medium string
#user input: affirmation of viewing
#output: none
#user output: work chosen
    global workDict
    valList = []
    for item in workDict[medium]:
        if item.wasViewed == False:
            valList.append(item)
    if len(valList) == 0:
        print("No works.")
    else:
        a = random.choice(workDict[medium])
        print("You should watch/play/whatever...")
        print(a.name,"\n")
        b = input("Did you watch it? y/n")
        if(b == "y"):
            a.wasViewed = True

def listWork(medium):
#Input: string that is in the medium list
#output: none
#user output: all entries present in the list for that medium.
    global workDict
    print("Here are the works registered for {}.",medium)
    for i in workDict[medium]:
        print(i)



def watDo():
#input: none
#user input: choice of task
#output: none
#user output: tasks available, other outputs dependent on validity of choice
#valid: goodbye or none
#invalid: error message
    print("What do you want to do?")
    print("1. Add a work.")
    print("2. Have a work chosen.")
    print("3. List works.")
    print("4. Quit.")
    choice = input("Enter a number.")
    if choice not in ["1","2","3","4"]:
        print("You have entered an invalid choice.  Please try again.")
        watDo()
    elif choice == "4":
        print("Goodbye.")
    else:
        a = pickMedium()
        if(choice == "1"):
            addWork(a)
            watDo()
        elif(choice == "2"):
            chooseWork(a)
            watDo()
        else:
            listWork(a)
            watDo()

mediumList = ["film", "game", "show", "comic", "book", "album"]
workDict = dict()
for n in mediumList:
    workDict[n] = list()

print("Welcome to Backlog Manager 0.1 Pre-Alpha!")
watDo()
