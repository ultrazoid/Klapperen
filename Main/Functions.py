'''
Created on 28/06/2012

@author: ultrazoid_
'''
import string
import datetime
import os
import urllib
import time

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
    filename = logname+'.txt'
    logOpen = open(filename, 'a')
    logOpen.seek(2)
    logOpen.write(value+'\n')
    logOpen.close()

def verUpd(info):
    try:
        verNf = open(info["verIN"],'r')
        verN = verNf.readlines()
        verNf.close()
        info["verL"] = verN[1] 
        need = True
    except IOError:
        os.remove('VersionIN.txt')
        urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/version.txt',info["verIN"])
        verNf = open(info["verIN"],'r')
        verN = verNf.readlines()
        verNf.close()
        info["verL"] = verN[1] 
        need = False
    if need == True:
        urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/version.txt','VersionIN.txt')
        verINf = open('VersionIN.txt','r')
        verIN = verINf.readlines()
        verINf.close()
        info["verLN"] = verIN[1]

def noLog(lang, langL):
    print 'NO LIBRARY FOUND'
    dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE '+langL+' LIBRABRY(y/n)')
    cont = False
    while cont != True:
        if dldInp == 'y':
            print "Downloading"+lang+"lib.csv"
            urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/library/'+lang+'lib.csv',lang+'lib.csv')
            time.sleep(2)
            print 'Downloaded'                
            cont = True
        elif dldInp == 'n':
            print 'Program will now exit'
            print 'Please obtain a copy of the library'
            os.system('PAUSE')
            os.sys.exit()
        elif dldInp != 'y' or dldInp != 'n':
            print 'PLEASE ENTER A VALID RESPONSE.'
            dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE '+langL+ 'ONE(y/n)')

def logUpd(lang, info):
    print "Klapperen will now check to make sure "+lang+"lib.csv is up to date."
    if info["verLN"] != info["verL"]:
        print "There is an update for "+lang+"lib.csv."
        libUp = raw_input("update?:(y/n)")
        cont = False
        while cont != True:
            if libUp == 'y':
                os.remove(lang+'lib.csv')
                urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/library/'+lang+'lib.csv',lang+'lib.csv')
                os.remove('Version.txt')
                urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/version.txt',info["verIN"])
                print "UPDATE FINISHED"
                raw_input("Press enter to continue...")
                cont = True
            elif libUp == 'n':
                print 'Update aborted'
                print 'Program will now continue'
                raw_input("Press enter to continue...")
                cont = True
            elif libUp != 'y' or libUp != 'n':
                print "Please enter a valid response:"
    elif info["verLN"] == info["verL"]:
        print "No update needed langlib.csv is up to date"
        raw_input("Press enter to continue...")