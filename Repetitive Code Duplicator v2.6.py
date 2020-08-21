import os
import re
from pathlib import Path

listContents = []
commandList = []
outList = []
listInput = ""
codeNumTest = ""
truePath = ""
getCommand = ""

MAX_VALUE = ""
numCount = 0

def generate():
    os.system('cls' if os.name == 'nt' else 'clear')
    global outList
    outList = []
    if '_oList_' in commandList:
        num = 0
        for element in listContents:
            num += 1
            out = ""
            for o in commandList:
                if o == '_oList_':
                    out += element
                elif o == '_oNumber_':
                    out += str(num)
                else:
                    out += o
            outList.append(out)

    elif '_oNumber_' in commandList:
        for num in range(0,int(MAX_VALUE)):
            out = ""
            for o in commandList:
                if o == '_oNumber_':
                    out += str(num)
                else:
                    out += o
            outList.append(out)

    else:
        out = ""
        for o in commandList:
            out += o
        outList.append(out)

def isThisPath(path):
    return Path(path).exists()

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

menuLoop = True
print(' -=CowsDaBest\'s Repetitive Code Duplicator Featuring SpartanSpark!=-\n')

while menuLoop:
    menuSelect = input('---------------------------------------------------\n 1) Set List\n 2) Set Dupe Command\n 3) List Commands\n 4) Generate\n 5) About\n>')

#// Set List
    if menuSelect == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        listInput = input(' Drag And Drop The List File\n>')

        listInput2 = listInput.replace(' ','')

        if listInput2 == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Nothing Was Inputed So Operation Has Stopped')

        else:
            listInput1 = listInput.replace('"','')
            confirmPath = isThisPath(listInput1)

            if confirmPath == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(' WARNING: "' + str(listInput1) + '" Path Does Not Exist!')

            else:
                truePath = listInput1
                openList = open(listInput1, 'r')
                listContents = openList.read()
                listContents = listContents.split('\n')
                openList.close()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(' "' + str(listInput1) + '" Set As current List')

#// Set Command
    elif menuSelect == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        dupeCommandLoop = True
        while dupeCommandLoop:
            lastCommand = getCommand
            lastCMDList = commandList
            getCommand = input("---------------------------------------------------\n Current Dupe Command:\n -" + str(getCommand) + "\n---------------------------------------------------\n \"_oList_\" = List\n \"_oNumber_\" = Number Value (Starts At 0)\n---------------------------------------------------\n Example 1: tag @e[type=_oList_] add _oNumber_\n Example 2: execute as @a[scores={scoreboard__oNumber_=1..}] at @s run tag @e[type=item,distance=..6.5] add _oNumber_\n ---------------------------------------------------\n Input Your Dupe Command\n>")
            getCommand = getCommand.replace('"','\"')
            testCommand = getCommand.replace(' ','')

            if testCommand == '':
                os.system('cls' if os.name == 'nt' else 'clear')
                getCommand = lastCommand
                print(' Input Was Blank So Aborting...')
                dupeCommandLoop = False
            else:
                #// NEEDS TO SPLIT OLIST AND ONUMBER | Also need to change _thing_other_ to the new format
                commandList = re.split(r'(_oList_|_oNumber_)', getCommand)

                if '_oNumber_' in commandList:
                    if '_oList_' in commandList:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(' Command Set To "' + str(getCommand) + '"')
                        print(' Max Number Value = Number Of Items In List')
                        dupeCommandLoop = False

                    else:
                        checkNum = True
                        while checkNum:
                            MAX_VALUE = input(' Please Enter the Max Number Value (1 Being 0)\n>')
                            testValue = isInt(MAX_VALUE)
                            if testValue == True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(' Command Set To "' + str(getCommand) + '"')
                                if '_oNumber_' in commandList:
                                    print(' Max Number Value: ' + str(MAX_VALUE))
                                checkNum = False
                                dupeCommandLoop = False
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(' Input Not A Number!')

                elif '_oList_' in commandList:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(' Command Set To "' + str(getCommand) + '"')
                    dupeCommandLoop = False
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(' Inavlid Input!\n -Input neither had "_oList_" nor "_oNumber_"')
                    commandList = lastCMDList
                    getCommand = lastCommand
                    dupeCommandLoop = False

#// List Of Commands And List Path
    elif menuSelect == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' List Path:\n -' + truePath + '\n\n Dupe Command:\n -'+ str(getCommand))
        if '_oNumber_' in commandList:
            if '_oList_' not in commandList:
                print('\n Max Number Value: ' + str(MAX_VALUE))
            else:
                print('\n Max Number Value = Number Of Items In List')


#// Generate
    elif menuSelect == '4':
        if not commandList:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' Command Not Set!')

        elif '_oList_' in commandList:
            if not listContents:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(' Nothing In List!')
            else:
                generate()
                print(' File Has Been Generated')
                with open('Generated Commands.txt', "w") as f:
                    for s in outList:
                        f.write(str(s) + str('\n'))
                f.close

        else:
            generate()
            print(' File Has Been Generated')
            with open('Generated Commands.txt', "w") as f:
                for s in outList:
                    f.write(str(s) + str('\n'))
            f.close


    elif menuSelect == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Repetitive Code Duplicator By CowsDaBest\n Special thanks to SpartanSpark making generation proccess possible!')

    elif menuSelect == 'debug':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(truePath)
        print(listContents)
        print(commandList)
        print(outList)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Unknown Command')

