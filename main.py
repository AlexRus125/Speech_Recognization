import speech_recognition as sp
from webbrowser import *
import pyaudio
recognizer = sp.Recognizer()

def searching() -> None:
    '''input voice:
    output search:'''
    micro = sp.Microphone()

    print('Say something...')
    audio = recognizer.listen(micro)

    try:
        print('recognition')
        q = recognizer.recognize_google_cloud(audio, language='ru-RU')
        print(f'You said:{q.strip()}')
        search_url = f'https://www.google.com/search?q={q}'
        open(search_url)

    except sp.UnknownValueError:
        print('An error has occurred')

searching()







