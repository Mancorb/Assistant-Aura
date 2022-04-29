import json
from random import randint
#Select default greeting if admin not online
def selectGreeting(timeH,usrT):
    if usrT:
        return selectGreetingAdmin(timeH)
    
    with open ("userPhrases.json", "r") as adG:
        dataAdG = json.loads(adG.read())
        if timeH <= 11:
            return dataAdG["morning"]

        elif timeH >= 12:
            return dataAdG["evening"]

        elif timeH >= 19:
            return dataAdG["night"]

#Select admin only greeting
def selectGreetingAdmin (timeH):
    with open ("adminGreeting.json", "r") as adG:
        dataAdG = json.loads(adG.read())
        type = chooseType()
        temp=""
        if timeH <= 11:
            return dataAdG["morning"]
        
        elif timeH >= 12:
            return dataAdG["evening"]
        
        elif timeH >= 19:
            return dataAdG["night"]
            
        return adminType(type, temp)    
            
#Choose one of three options
def chooseType():
    temp = randint(1,10)
    if temp % 2 == 0: return 1
    elif temp % 3 == 0: return 2
    else: return 3

#return the type of greeting
def adminType(type, temp):
    type = chooseType()
    temp=temp[type-1]
    return(temp[f"Greeting{type}"])
