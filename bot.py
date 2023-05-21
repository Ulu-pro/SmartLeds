from aiogram import Bot, Dispatcher, executor, types
from serial import Serial

from config import Config
from converter import save_audio
from recognizer import get_detected

bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(bot)
serial = Serial(Config.COM_PORT, Config.BAUD_RATE)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    await message.reply(Config.START_TEXT,
                        parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(content_types=types.ContentType.VOICE)
async def voice_handler(message: types.Message):
    file = await bot.download_file_by_id(message.voice.file_id)
    save_audio(audio_file=file)
    text, command = get_detected()
    await message.reply(Config.DETECTED_TEXT.format(text),
                        parse_mode=types.ParseMode.MARKDOWN)
    serial.write(command.encode())
    print(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
