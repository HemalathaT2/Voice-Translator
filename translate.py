import speech_recognition to sr #to recognise voice data
from google_trans_new import google_translator #to translate voice data
import pyttsx3 #text to speech conversion

recognizer=sr.recognizer()
engine=pyttsx3.init()

with sr.Microphone() as source:
    print('Clearing the background noises....')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    audio=recognizer.listen(source,timeout=1)
    print('Done recording')

try:
    print('Recognizing your voice\nplease hold on....')
    result=recognizer.recognize_google(audio,language='en')
except Exception as ex:
    print(ex)


def trans():
    langinput=input('Type the language code you want to translate')
    translator=google_translator()
    translate_text=translator.translate(str(result),lang_tgt=str(langinput))
    print(translate_text)
    engine.say(str(translate_text))
    engine.runAndWait()
trans()
