# pip install pyttsx3

import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-10')
    engine.say(text)
    engine.runAndWait()

text_to_speech("Hello World")