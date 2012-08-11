'''
Created on 28/06/2012

@author: ultrazoid_

Klapperen Chatbot
Version (CODE) dev 1.3
'''
import string
import time
import os
import Functions
import datetime
import urllib

verP = '(CODE) dev'
verNu = '1.3'
verPN = verP+' '+verNu
info = {"Name":"Klapperen","Version":verPN,"verIN":"Version.txt","verL":"1","verLN":"1"}

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

now = datetime.datetime.now()
lfd = now.strftime("%Y-%d-%m %H%M")

print info["Name"]
print info["Version"]
lanInt = raw_input('Please select a language(EN):')
LanInp = string.upper(lanInt)

if LanInp == 'EN':
    print 'ENGLISH SELECTED'
    Functions.logMakeEN(lfd,verP,verNu)
    try:
        print "Klapperen will now check to make sure ENlib.csv is up to date."
        if info["verLN"] != info["verL"]:
            print "There is an update for ENlib.csv."
            libUp = raw_input("update?:(y/n)")
            cont = False
            while cont != True:
                if libUp == 'y':
                    os.remove('ENlib.csv')
                    urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/library/ENlib.csv','ENlib.csv')
                    os.remove('Version.txt')
                    urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/version.txt',info["verIN"])
                    print "UPDATE FINISHED"
                    os.system("PAUSE")
                    cont = True
                elif libUp == 'n':
                    print 'Update aborted'
                    print 'Program will now continue'
                    os.system('PAUSE')
                    cont = True
                elif libUp != 'y' or libUp != 'n':
                    print "Please enter a valid response:"
        elif info["verLN"] == info["verL"]:
            print "No update needed ENlib.csv is up to date"
            os.system("PAUSE")
        greetings = Functions.listGet(0,'EN')
        farewells = Functions.listGet(1,'EN')
        sGreetings = Functions.listGet(2,'EN')
        questions = Functions.listGet(3,'EN')
        stalls = Functions.listGet(4,'EN')
        print "SUCCESS"
        os.system('PAUSE')
        lib = True
    except IOError:
        print 'NO LIBRARY FOUND'
        dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE ENGLISH ONE(y/n)')
        cont = False
        lib = False
        while cont != True:
            if dldInp == 'y':
                print "Downloading ENlib.csv"
                urllib.urlretrieve('http://ultrazoidserver.x10.mx/klapperen/library/ENlib.csv','ENlib.csv')
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
                dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE ENGLISH ONE(y/n)')
        try:
            greetings = Functions.listGet(0,'EN')
            farewells = Functions.listGet(1,'EN')
            sGreetings = Functions.listGet(2,'EN')
            questions = Functions.listGet(3,'EN')
            stalls = Functions.listGet(4,'EN')
            print "SUCCESS"
            os.system('PAUSE')
            lib = True
        except IOError:
            print 'FATAL ERROR ENCOUNTED'
            print 'PROGRAM WILL NOW SHUT DOWN'
            os.system('PAUSE')
                