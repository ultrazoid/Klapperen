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

verP = '(CODE) dev'
verNu = '1.5'
verPN = verP+' '+verNu
info = {"Name":"Klapperen","Version":verPN,"verIN":"Version.txt","verL":"1","verLN":"1"}
k = "KLP: "
y = "YOU: "
s = "SYS: "

Functions.verUpd(info)

now = datetime.datetime.now()
lfd = now.strftime("%Y-%d-%m %H%M")

print info["Name"]
print info["Version"]
lanInt = raw_input('Please select a language(EN):')
LanInp = string.upper(lanInt)

if LanInp == 'EN':
    english.main(lfd, verP, verNu, info, verPN, k, s, y)
        
                