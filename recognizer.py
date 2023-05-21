import speech_recognition as sr

from config import Config


def get_detected():
    recognizer = sr.Recognizer()

    with sr.AudioFile(Config.AUDIO_FILE) as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio, language=Config.LANGUAGE)
    rgb = Config.COLORS.get(str(text).lower(), (0, 0, 0))

    color = ','.join(str(value) for value in rgb)

    return [text, color]
