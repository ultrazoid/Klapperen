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
import urllib2

now = datetime.datetime.now()
lfd = now.strftime("%Y-%d-%m %H%M")

LanInp = raw_input('Please select a language(EN):')

if LanInp == 'EN':
    print 'ENGLISH SELECTED'
    Functions.logMakeEN(lfd,'dev','1')
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
    except IOError:
        print 'NO LIBRARY FOUND'
        dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE ENGLISH ONE(y/n)')
        cont = False
        while cont != True:
            if dldInp == 'y':
                print "Downloading ENlib.csv"
                libfile = urllib2.urlopen('http://ultrazoidserver.x10.mx/klapperen/library/ENlib.csv')
                output = open('ENlib.csv','w')
                output.write(libfile.read())
                output.close
                time.sleep(2)
                print 'Downloaded'                
                cont = True
            elif dldInp == 'n':
                #TO DO: Add program end statement
                a=1
                cont = True
            elif dldInp != 'y' or dldInp != 'n':
                print 'PLEASE ENTER A VALID RESPONSE.'
                dldInp = raw_input('WOULD YOU LIKE TO DOWNLOAD THE ENGLISH ONE(y/n)')
                