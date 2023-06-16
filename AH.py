import speech_recognition as sr

def start_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something into the microphone')
        audio = r.listen(source, timeout=1)

    try:
        global text
        text = r.recognize_google(audio, language='id-ID')
        print("You said:", text)
    except sr.UnknownValueError:
        print('Audio unintelligible')
    except sr.RequestError as e:
        print("Cannot obtain result: {0}".format(e))

# start_speech()