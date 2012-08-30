'''
Klapperen Chatbot
Version (CODE) dev 1.6

English run-time for Klapperen Chatbot

Created on 30/08/2012

@author: ultrazoid_
'''
import string
import time
import os
import Functions
import random

def main(lfd, verP, verNu, info, verPN, k, s, y):
    print 'ENGLISH SELECTED'
    Functions.logMakeEN(lfd,verP,verNu)
    try:
        Functions.logUpd('EN',info)
        greetings = Functions.listGet(0,'EN')
        farewells = Functions.listGet(1,'EN')
        sGreetings = Functions.listGet(2,'EN')
        questions = Functions.listGet(3,'EN')
        stalls = Functions.listGet(4,'EN')
        sReplies = Functions.listGet(5, 'EN')
        ssReplies = Functions.listGet(6, 'EN')
        print "Library loaded!"
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
            sReplies = Functions.listGet(5, 'EN')
            ssReplies = Functions.listGet(6, 'EN')
            print "Library loaded!"
            raw_input("Press enter to continue...")
            lib = True
        except IOError:
            print 'FATAL ERROR ENCOUNTED'
            print 'PROGRAM WILL NOW SHUT DOWN'
            raw_input("Press enter to continue...")
    red = raw_input("Would you like to begin now(y/n)?")
    cont = False
    while cont == False:
        if red == 'y':
            print "Klapperen will now initiate"
            time.sleep(1)
            cont = True
        elif red == 'n':
            print "Klapperen will now exit"
            time.sleep(2)
            os.sys.exit()
        else:
            print 'Please enter a valid value'
            red = raw_input("Would you like to begin now(y/n)?")
    print "\nWelcome to Klapperen"
    print "Version",verPN
    print "By ultrazoid_"
    raw_input("Press enter to begin chat(Chat sequence not complete)")
    klp = k+"Hi my name is Klapperen:"
    en_inp = string.lower(raw_input(klp))
    en_wr = y+en_inp
    Functions.logWrite(lfd,klp)
    while en_inp != 'end':
        Functions.logWrite(lfd,en_wr)
        if en_inp in greetings:
            klp = k+greetings[random.randrange(0,len(greetings))]
            Functions.logWrite(lfd,klp)
            print klp
            klp = k+sGreetings[random.randrange(0,len(sGreetings))]
            Functions.logWrite(lfd,klp)
            print klp
        elif en_inp in farewells:
            klp = k+farewells[random.randrange(0,len(farewells))]
            Functions.logWrite(lfd,klp)
            print klp
            lin = s+"IF YOU WOULD LIKE TO EXIT PLEASE TYPE END"
            Functions.logWrite(lfd,lin)
            print lin
        elif en_inp in sGreetings:
            klp = k+sReplies[random.randrange(0,len(sReplies))]
            Functions.logWrite(lfd,klp)
            print klp
            klp = k+ssReplies[random.randrange(0,len(ssReplies))]
            Functions.logWrite(lfd,klp)
            print klp
        else:
            klp = k+stalls[random.randrange(0,len(stalls))]
            Functions.logWrite(lfd,klp)
            print klp
        en_inp = string.lower(raw_input('RESPONSE: '))
        en_wr = y+en_inp
    klp = k+farewells[random.randrange(0,len(farewells))]
    Functions.logWrite(lfd,klp)
    print klp
    print s+'ENDING'
    lin = s+'USER TERMINATED CONVERSTATION'
    Functions.logWrite(lfd,lin)
    print lin
    lin = 'LOG END'
    Functions.logWrite(lfd,lin)
    print s+'KLAPPEREN WILL NOW TERMINATE'
    raw_input('press enter to end...')