import pyttsx3
def speak (txt):
    ttsEng = pyttsx3.init()
    ttsEng.say(txt)
    ttsEng.runAndWait()
    ttsEng.stop()

def getPrefs():
    data =[]
    engine = pyttsx3.init() # object creation
    rate = engine.getProperty('rate') 
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices') 
    data.append(engine)
    data.append(rate)
    data.append(volume)
    data.append(voices)
    return data

def SetVolume(obj,vol):
    obj.setProperty('volume',vol)

def SetRate(obj,rate):
    obj.setProperty('rate', rate) 