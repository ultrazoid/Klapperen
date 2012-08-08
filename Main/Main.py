'''
Created on 28/06/2012

@author: ultrazoid_

Klapperen Chatbot
'''
import string
import time
import os
import Functions
import datetime
import urllib
verP = 'dev'
verN = '1.2'

now = datetime.datetime.now()
lfd = now.strftime("%Y-%d-%m %H%M")

lanInt = raw_input('Please select a language(EN):')
LanInp = string.upper(lanInt)

if LanInp == 'EN':
    print 'ENGLISH SELECTED'
    Functions.logMakeEN(lfd,verP,verN)
    try:
        greetings = Functions.listGet(0,'EN')
        farewells = Functions.listGet(1,'EN')
        sGreetings = Functions.listGet(2,'EN')
        questions = Functions.listGet(3,'EN')
        stalls = Functions.listGet(4,'EN')
        print greetings
        print farewells
        print sGreetings
        print questions
        print stalls
        print '\n'
        print 'SUCCESSFUL'
        os.system('PAUSE')
    except IOError:
        print 'NO LIBRARY FOUND'
        dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE ENGLISH ONE(y/n)')
        cont = False
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
            print greetings
            print farewells
            print sGreetings
            print questions
            print stalls
            print '\n'
            print 'SUCCESSFUL'
            os.system('PAUSE')
        except IOError:
            print 'FATAL ERROR ENCOUNTER'
            print 'PROGRAM WILL NOW SHUT DOWN'
            os.system('PAUSE')
            os.sys.exit()
                