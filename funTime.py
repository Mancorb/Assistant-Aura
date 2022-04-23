from datetime import datetime
#Obtain the current time
def getTime ():
    timeRes = datetime.now().strftime("%H:%M:%S")

    hour=timeRes[0]+timeRes[1]
    minute=timeRes[3]+timeRes[4]
    second=timeRes[6]+timeRes[7]
    return [hour,minute,second]

print(getTime())