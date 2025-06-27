import datetime
import re
import json
import logging
import datetime

import requests
from heygen.heygen_api_client import HeygenAPIClient
from config import HEYGEN_API_HEADERS, DEFAULT_VOICE_ID, DEFAULT_VIDEO_ID, DEFAULT_SETTINGS, DOWNLOAD_HEADERS



def read_or_create_json(filename):
    try:
        with open(filename, "r") as f:
            json_data = f.read()
            data = json.loads(json_data)
    except FileNotFoundError:
        data = {}

    return data


def printer(printing):
    log_file = open("messages.txt", "a")
    print(datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S") + ' ' + str(printing))
    log_file.write(datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S") + ' ' + str(printing) + '\n')
    log_file.close()
    return printer


def save_json(filename, data):
    json_data = json.dumps(data)
    with open(filename, "w") as f:
        f.write(json_data)


def save_mp3_file(audio_url, filename):
    response = requests.get(audio_url, stream=True)
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


def generate_voice(text):
    logging.basicConfig(level=logging.DEBUG)

    # text = input().strip()
    if not text:
        return "Текст не должен быть пустым!"

    # Формируем SSML
    ssml = f"<speak><voice name='{DEFAULT_VOICE_ID}'><prosody rate='1' pitch='0%'>{text}</prosody></voice></speak>"

    client = HeygenAPIClient(HEYGEN_API_HEADERS)
    try:
        result = client.generate_audio(
            text=ssml,
            voice_id=DEFAULT_VOICE_ID,
            video_id=DEFAULT_VIDEO_ID,
            settings=DEFAULT_SETTINGS
        )
        client = HeygenAPIClient(DOWNLOAD_HEADERS)
        audio = client.save_audio(
            voice_id=DEFAULT_VOICE_ID,
            video_id=DEFAULT_VIDEO_ID,
            settings=DEFAULT_SETTINGS,
            url_aud=result
        )
        return audio
    except Exception as e:
        print(e)
        return 401

    
    


   


def compare_texts(text):

    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    return text


# def generate_voice_1(text):
#     config = read_or_create_json("config.json")
    
#     CHUNK_SIZE = 1024
#     url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

#     headers = {
#         "Accept": "audio/mpeg",
#         "Content-Type": "application/json",
#         "xi-api-key": config["ELEVENLABS_KEY"]
#     }

#     data = {
#         "text": text,
#         "model_id": "eleven_multilingual_v2",
#         "voice_settings": {
#             "stability": 0.05,
#             "similarity_boost": 0.08,
#             "style": 0.7
#         }
#     }

#     response = requests.post(url, json=data, headers=headers)
#     if response.status_code != 401:
#         filename = "women_mp3/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp3"
#         with open(filename, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#                 if chunk:
#                     f.write(chunk)
#         return filename
#     return 401

logging.basicConfig(level=logging.DEBUG)
