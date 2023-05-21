# noinspection SpellCheckingInspection
class Config:
    COM_PORT = 'COM3'
    BAUD_RATE = 9600
    BOT_TOKEN = ''
    START_TEXT = 'Отправьте голосовую команду, например:\n`Включи красный`\n`Выключи синий`'
    DETECTED_TEXT = 'Распознанный текст:\n`{}`'
    TEMPORARY_FILE = 'temporary.ogg'
    AUDIO_FILE = 'audio.wav'
    LANGUAGE = 'ru-RU'
    ACTIONS = {
        'включи': 1,
        'выключи': 0,
        'отключи': 0,
        'включить': 1,
        'выключить': 0,
        'отключить': 0
    }
    LEDS = {
        'красный': 1,
        'жёлтый': 2,
        'зелёный': 3,
        'синий': 4,
        'белый': 5
    }
