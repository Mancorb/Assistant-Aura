import pyttsx3
def speak (txt):
    ttsEng = pyttsx3.init()
    ttsEng.say(txt)
    ttsEng.runAndWait()
    ttsEng.stop()

def getPrefs():
    engine = pyttsx3.init() # object creation
    rate = engine.getProperty('rate') 
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices') 
    return [engine,rate,volume,voices]

def SetVolume(obj,vol):
    obj.setProperty('volume',vol)

def SetRate(obj,rate):
    obj.setProperty('rate', rate) 