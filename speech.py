import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="vi-VN")
        translator = Translator()
        textTranslated = translator.translate(text)
        print('You said: {}'.format(textTranslated.text))
    except:
        print('Sorry could not recognize your voice')