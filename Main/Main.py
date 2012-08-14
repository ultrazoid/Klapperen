'''
Created on 28/06/2012

@author: ultrazoid_

Klapperen Chatbot
Version (CODE) dev 1.4
'''
import string
import time
import os
import Functions
import datetime
import urllib

verP = '(CODE) dev'
verNu = '1.4'
verPN = verP+' '+verNu
info = {"Name":"Klapperen","Version":verPN,"verIN":"Version.txt","verL":"1","verLN":"1"}


Functions.verUpd(info)

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
        Functions.logUpd('EN',info)
        greetings = Functions.listGet(0,'EN')
        farewells = Functions.listGet(1,'EN')
        sGreetings = Functions.listGet(2,'EN')
        questions = Functions.listGet(3,'EN')
        stalls = Functions.listGet(4,'EN')
        print "SUCCESS"
        raw_input("Press enter to continue...")
        lib = True
    except IOError:
        Functions.noLog('EN', 'ENGLISH')
        try:
            greetings = Functions.listGet(0,'EN')
            farewells = Functions.listGet(1,'EN')
            sGreetings = Functions.listGet(2,'EN')
            questions = Functions.listGet(3,'EN')
            stalls = Functions.listGet(4,'EN')
            print "SUCCESS"
            raw_input("Press enter to continue...")
            lib = True
        except IOError:
            print 'FATAL ERROR ENCOUNTED'
            print 'PROGRAM WILL NOW SHUT DOWN'
            raw_input("Press enter to continue...")
                