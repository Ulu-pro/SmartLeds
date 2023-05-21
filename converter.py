import os

import soundfile as sf

from config import Config


def save_audio(audio_file):
    with open(Config.TEMPORARY_FILE, 'wb') as file:
        file.write(audio_file.read())

    data, samplerate = sf.read(Config.TEMPORARY_FILE)
    sf.write(Config.AUDIO_FILE, data, samplerate, format='wav')
    os.remove(Config.TEMPORARY_FILE)
