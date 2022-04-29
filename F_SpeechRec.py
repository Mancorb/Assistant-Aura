import speech_recognition as sr
def audio2txt():
    r = sr.Recognizer()#Create Recognizer object
    audio = sr.AudioFile("output.wav")#open audio file
    with audio as source:
        r.adjust_for_ambient_noise(source) #Eliminate noise
        audio = r.record(source) #temporarly record audio from file
        command = r.recognize_google(audio) #Send data to speech rec
        return command

print(audio2txt())