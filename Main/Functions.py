'''
Created on 28/06/2012

@author: ultrazoid_
'''
import string
import datetime

def listGet(lineNumber, lang): #lineNumber starts at 0. So line 1 is 0, 2 1 and so on
    filename = lang+"lib.csv"
    fileOpen = open(filename, 'r')
    fileLines = fileOpen.readlines()
    listGot = string.split(fileLines[lineNumber],',')
    snoop = listGot[len(listGot)-1]
    if '\n' in snoop:
        listGot[-1] = listGot[-1].strip()
        listDone = listGot
    else:
        listDone = listGot
    fileOpen.close()
    return listDone

def logMakeEN(lfd, verP, verN):
    lfn = lfd+".txt"
    lfo = open(lfn , 'a')
    version = verP+' '+ verN
    lfo.write("KLAPPEREN LOG\n")
    lfo.write("Date: ")
    lfo.write(lfd+'\n')
    lfo.write("Version: ")
    lfo.write(version)
    lfo.write("\n")
    lfo.close()
    
def logWrite(logname, value):
    filename = logname+'txt'
    logOpen = open(filename, 'w')
    
