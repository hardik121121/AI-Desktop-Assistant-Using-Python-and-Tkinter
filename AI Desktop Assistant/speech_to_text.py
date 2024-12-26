# pip install SpeechRecognition==3.8.1
# pip install PyAudio

import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = ""
            voice_data = r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError:
            print("RequestError")

speech_to_text()
