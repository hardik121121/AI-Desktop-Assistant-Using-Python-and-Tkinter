import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Aido, and I am a virtual assistant")
        return "My name is Aido, and I am a virtual assistant"
    
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hey, Hardik how can i help you today")
        return "Hey, Hardik how can i help you today"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir hope you are having a great time")
        return "Good morning sir hope you are having a great time"
    
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour : " , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Ok sir have a great day ahead shutting down")
        return "Ok sir have a great day ahead shutting down"
    
    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("Spotify is ready to play")
        return "Spotify is ready to play"
    
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("Youtube is on see your favourite content now")
        return "Youtube is on see your favourite content now"
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google is on happy surfing on the internet")
        return "Google is on happy surfing on the internet"
    
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("Functionality not achievable Sorry sir")
        return "Functionality not achievable Sorry sir"