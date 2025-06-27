import datetime
import logging
from aiogram.types import FSInputFile, URLInputFile
from helpers import compare_texts, generate_voice, printer, read_or_create_json, save_json, save_mp3_file


config = read_or_create_json("config.json")

async def get_config(msg):
    if (msg.from_user.id != config["ADMIN_ID"]):
        if (msg.from_user.id != config["GROUP_ADMIN_ID"]):
            return
    
    await msg.answer(str(config))


# async def set_generate_metod(msg):
#     if (msg.from_user.id != config["ADMIN_ID"]):
#         if (msg.from_user.id != config["GROUP_ADMIN_ID"]):
#             return
#     message = msg.text.replace("/setmetod ", "")
#     if (message == ""):
#         await msg.answer("Метод не найден!")
#         return

#     config["GENERATE_MODE"] = message
#     save_json("config.json", config)
#     await msg.answer("Метод генерации изменен.")



# Включить бота
async def start(msg):
    if (msg.from_user.id != config["ADMIN_ID"]):
        if (msg.from_user.id != config["GROUP_ADMIN_ID"]):
            return
    config["ON_WORK"] = True
    await msg.answer("Бот запущен")
    save_json("config.json", config)


# Остановить бота
async def stop(msg):
    if (msg.from_user.id != config["ADMIN_ID"]):
        if (msg.from_user.id != config["GROUP_ADMIN_ID"]):
            return
    config["ON_WORK"] = False
    await msg.answer("Бот остановлен")
    save_json("config.json", config)


# При любых сообщениях
async def allmsg(msg):
    message = msg.text
    logging.basicConfig(level=logging.DEBUG)
    printer(f"Message '{message}' from {msg.from_user.id}")
    if (config["ON_WORK"] == False):
        return
    if (msg.from_user.id != config["ADMIN_ID"]):
        if (msg.from_user.id != config["GROUP_ADMIN_ID"]):
            return
    else:
        await msg.answer("Секунду... Генерирую")
        if config["GENERATE_MODE"] == "1": 
            await msg.answer("Использую метод генерации 1")
            filename = generate_voice(message)
            if filename != 401:
                input_file = FSInputFile(path=filename)
                await msg.answer_voice(voice=input_file)
                return

logging.basicConfig(level=logging.DEBUG)
