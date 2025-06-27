import datetime
import requests
import json
from typing import Optional, Dict, Any

class HeygenAPIClient:
    BASE_URL = "https://api2.heygen.com/v2/online/text_to_speech.generate"

    def __init__(self, api_headers: Dict[str, str]):
        self.api_headers = api_headers

    def generate_audio(self, text: str, voice_id: str, video_id: str, settings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload = {
            "text_type": "ssml",
            "text": text,
            "voice_id": voice_id,
            "settings": settings or {},
            "with_timestamps": True,
            "video_id": video_id,
            "emotion": "",
            "generation_type": "preview",
            "voice_engine": "elevenLabs"
        }
        response = requests.post(self.BASE_URL, headers=self.api_headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def save_audio(self, url_aud: str, voice_id: str, video_id: str, settings: Optional[Dict[str, Any]] = None, ) -> Dict[str, Any]:
        CHUNK_SIZE = 1024
        audio_url = url_aud.get('data', {}).get('audio_url')
        if audio_url:
            response = requests.get(audio_url, headers=self.api_headers, stream=True)
            if response.status_code != 401:
                filename = "battalov" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp3"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                return filename
            return 401
        else:
            return 401
