'''
Klapperen Chatbot
Version (CODE) dev 1.6

Main runtime

Created on 28/06/2012

@author: ultrazoid_

'''
import string
import Functions
import datetime
import english
import time

verP = '(CODE) dev'
verNu = '1.6'
verPN = verP+' '+verNu
info = {"Name":"Klapperen","Version":verPN,"verIN":"Version.txt","verL":"1","verLN":"1","Av":"EN"}
k = "KLP: "
y = "YOU: "
s = "SYS: "
#this is a random comment line
Functions.verUpd(info)

now = datetime.datetime.now()
lfd = now.strftime("%Y-%d-%m %H%M")

print info["Name"]
print info["Version"]
lanInt = raw_input('Please select a language(EN):')
LanInp = string.upper(lanInt)
cont = False
while cont == False:
    if LanInp == 'EN':
        cont = True
        english.main(lfd, verP, verNu, info, verPN, k, s, y)
        break
    elif LanInp == "END" or LanInp == "EXIT":
        print 'END/EXIT CODE RECOGNISED'
        time.sleep(1)
        break
    elif LanInp not in info["Av"]:
        cont = False
        print "Language unavailable"
        print "Currently only "+info["Av"]+" is available"
        print "Please try again!"
    lanInt = raw_input('Please select a language(EN):')
    LanInp = string.upper(lanInt)


        
                