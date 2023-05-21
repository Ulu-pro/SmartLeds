import speech_recognition as sr

from config import Config


def get_detected():
    recognizer = sr.Recognizer()

    with sr.AudioFile(Config.AUDIO_FILE) as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio, language=Config.LANGUAGE)
    action_word, led_color = str(text).lower().split()

    action_id = Config.ACTIONS[action_word]
    led_id = Config.LEDS[led_color]

    return [
        text,
        str(led_id) + str(action_id)
    ]
