from gtts import gTTS
import os
import subprocess as sp
import pyttsx

def main(val):
    '''
    try:
        tts = gTTS(text=val, lang='hi')
        print os.getcwd()
        filename = "tempfileTTS.mp3"
        path = os.getcwd() + '/app/speak/' + filename
        tts.save(path)
        print path
        sp.Popen(["vlc", path])
    except Exception as e:
        print e
    '''

    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'english-us')
    engine.say(val)
    engine.runAndWait()
