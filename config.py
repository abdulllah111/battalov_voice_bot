# BOT_TOKEN = "6916064957:AAE_QqYUpfn58HHOLzx1yI7WR5AEB5tx-68"
import datetime

import pytz


BOT_TOKEN = "7321858442:AAFlcitqZjBb594eFh5Wz7JRl-65p-xkWTw"
ADMIN_ID = 1309944247
RIZVAN_ID = 877177375,
GROUP_ADMIN_ID = 1087968824 
ON_WORK = True


HEYGEN_API_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "heygen-video-id": "ae850775b7c84547b002f2cde6095c2b",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "traceparent": "00-00000000000000003e965f7015997f49-4e69829e620e85bd-01",
    "x-datadog-origin": "rum",
    "x-datadog-parent-id": "5650190824274560445",
    "x-datadog-sampling-priority": "1",
    "x-datadog-trace-id": "4509897011861487433",
    "x-language-override": "en-US",
    "x-last-build": "1750911455925",
    "x-path": "/create-v4/ae850775b7c84547b002f2cde6095c2b",
    "x-ver": "4.1.0",
    "x-zid": "XG2AIff7aXJHrrO7XXnzCS8JkrTtVLqJ",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "cookie": "_gcl_au=1.1.1778593495.1747665654; x-movio-v-id=XG2AIff7aXJHrrO7XXnzCS8JkrTtVLqJ; x-movio-shared-v-id=msSKsKXvlcNcBNcY3UZXtdXzqbr97NRo; _ga=GA1.1.1084510556.1747665655; _fbp=fb.1.1747665654927.509962968110387266; _tt_enable_cookie=1; _ttp=01JVMFV58SRAXGX05E9Y3J5TBJ_.tt.1; ajs_anonymous_id=ee4757e4-d0a1-4116-b095-9e6a8c005305; _adora_user_id=0196e8fd-f412-721a-a8cd-7512158f6903; ajs_user_id=9c82f7d3af624bee8eb13f50b920a9df; intercom-device-id-oiknz8io=eae4d37b-ca2f-492c-8e85-8453e72917c9; heygen_session=eyJzZXNzaW9uX3Rva2VuIjogImV5SjBiMnRsYmlJNklDSmlZekk0TlRFeE5qWXhZakkwWVRsak9EZGhPRGcxWkRBM09HVXpaR1ZoWWlJc0lDSjBiMnRsYmw5MGVYQmxJam9nSW5KbFozVnNZWElpTENBaVkzSmxZWFJsWkY5aGRDSTZJREUzTlRBeU5UZ3pOakI5In0=; heygen_is_login=true; heygen_space=; shared-u=9c82f7d3af624bee8eb13f50b920a9df; intercom-session-oiknz8io=dlQycnZkdmJwK2lJd0VUMU8wQzdqVGw1QVIyRWZ6UzQ1eDlSZ0FqWXdiV1A3c3htWXEzYnJFeldUZnBkS3RaRFZkTWZ2Ly9lM0lubU8xS2I2ZjZ6V2dpV1o5SFpVK0VPMGF0NHZvbk5ZV0E9LS00Vlk2SXhQVWk5ek16YnhzTmRNZ0lRPT0=--048cbcb9787da21bd16426f4c56d79153ede985e; cf_clearance=JAiyD3ixdVpVOC0zjRLx2.2LPR45fUUp41SrwOv9PMI-1750959346-1.2.1.1-Vh..kr6jTx.wrxPSu2NVK3Vd.RTEbDc_tgaPHnegANXK85QYhxObfJZHz3_F2eMy9h1GYNgoGHrnWC4R_gbKUvBZ9DvwBEMXRjaaue2oYTmPqMj4og49RFapKU8W9HAx8HUL_hlgVSGFBjMa3IZYSkDA5ABcnRaX42FCBj8VFdQ_lHCJain.VUOJL6ct_anZuZURJOqEnyjkL_VzE5KUtH1_MUchGwzVPR0ZvjLTkvm1dxSe_QE5gn6hZIAnYNDnF6UkFWfQs_zTiVtbXe02NP_MwtPAMBKqEs_J34JwkrybbMY8P1g_K46z2jXcIqGvo4hKvTdkn1HUk4IibAXtm42JoxXwztgHR1v.Bp.iDBA; ttcsid=1750959349049::psd28d6tSYdkp74YfZtz.2.1750959401621; ttcsid_CULAR4JC77U47BI945FG=1750959349049::jZ6gJ4H4ZagQR6F3fDKL.2.1750959401848; fs_uid=#o-22GV82-na1#bd55459a-254d-49d7-a67d-c3f4e9cfd8c6:665568dc-9e2c-468f-ae12-63a26b160e65:1750959276042::5#894f0fef#/1779202344; _ga_PMMWB6MFPC=GS2.1.s1750959276$o109$g1$t1750959569$j44$l0$h0; fs_lua=1.1750959575367; ph_phc_bcoaBa4uZdMp0CzXr7QhZRRpnNGgBRRZ1GStvuJVAgJ_posthog=%7B%22distinct_id%22%3A%229c82f7d3af624bee8eb13f50b920a9df%22%2C%22%24sesid%22%3A%5B1750959597266%2C%220197ad4e-42d5-7e6d-9a1d-e9adec8db737%22%2C1750959276757%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22u%22%3A%22https%3A%2F%2Fwww.heygen.com%2F%22%7D%7D"
}

gmt_time = datetime.datetime.now(pytz.utc)


# Форматируем как требуется
formatted_time = gmt_time.strftime("%a, %d %b %Y %H:%M:%S GMT")

DOWNLOAD_HEADERS = {
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "heygen-video-id": "ae850775b7c84547b002f2cde6095c2b",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "traceparent": "00-00000000000000003e965f7015997f49-4e69829e620e85bd-01",
    "x-datadog-origin": "rum",
    "x-datadog-parent-id": "5650190824274560445",
    "x-datadog-sampling-priority": "1",
    "x-datadog-trace-id": "4509897011861487433",
    "x-language-override": "en-US",
    "x-last-build": "1750911455925",
    "x-path": "/create-v4/ae850775b7c84547b002f2cde6095c2b",
    "x-ver": "4.1.0",
    "x-zid": "XG2AIff7aXJHrrO7XXnzCS8JkrTtVLqJ",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "cookie": "_gcl_au=1.1.1778593495.1747665654; x-movio-v-id=XG2AIff7aXJHrrO7XXnzCS8JkrTtVLqJ; x-movio-shared-v-id=msSKsKXvlcNcBNcY3UZXtdXzqbr97NRo; _ga=GA1.1.1084510556.1747665655; _fbp=fb.1.1747665654927.509962968110387266; _tt_enable_cookie=1; _ttp=01JVMFV58SRAXGX05E9Y3J5TBJ_.tt.1; ajs_anonymous_id=ee4757e4-d0a1-4116-b095-9e6a8c005305; _adora_user_id=0196e8fd-f412-721a-a8cd-7512158f6903; ajs_user_id=9c82f7d3af624bee8eb13f50b920a9df; intercom-device-id-oiknz8io=eae4d37b-ca2f-492c-8e85-8453e72917c9; heygen_session=eyJzZXNzaW9uX3Rva2VuIjogImV5SjBiMnRsYmlJNklDSmlZekk0TlRFeE5qWXhZakkwWVRsak9EZGhPRGcxWkRBM09HVXpaR1ZoWWlJc0lDSjBiMnRsYmw5MGVYQmxJam9nSW5KbFozVnNZWElpTENBaVkzSmxZWFJsWkY5aGRDSTZJREUzTlRBeU5UZ3pOakI5In0=; heygen_is_login=true; heygen_space=; shared-u=9c82f7d3af624bee8eb13f50b920a9df; intercom-session-oiknz8io=dlQycnZkdmJwK2lJd0VUMU8wQzdqVGw1QVIyRWZ6UzQ1eDlSZ0FqWXdiV1A3c3htWXEzYnJFeldUZnBkS3RaRFZkTWZ2Ly9lM0lubU8xS2I2ZjZ6V2dpV1o5SFpVK0VPMGF0NHZvbk5ZV0E9LS00Vlk2SXhQVWk5ek16YnhzTmRNZ0lRPT0=--048cbcb9787da21bd16426f4c56d79153ede985e; cf_clearance=JAiyD3ixdVpVOC0zjRLx2.2LPR45fUUp41SrwOv9PMI-1750959346-1.2.1.1-Vh..kr6jTx.wrxPSu2NVK3Vd.RTEbDc_tgaPHnegANXK85QYhxObfJZHz3_F2eMy9h1GYNgoGHrnWC4R_gbKUvBZ9DvwBEMXRjaaue2oYTmPqMj4og49RFapKU8W9HAx8HUL_hlgVSGFBjMa3IZYSkDA5ABcnRaX42FCBj8VFdQ_lHCJain.VUOJL6ct_anZuZURJOqEnyjkL_VzE5KUtH1_MUchGwzVPR0ZvjLTkvm1dxSe_QE5gn6hZIAnYNDnF6UkFWfQs_zTiVtbXe02NP_MwtPAMBKqEs_J34JwkrybbMY8P1g_K46z2jXcIqGvo4hKvTdkn1HUk4IibAXtm42JoxXwztgHR1v.Bp.iDBA; ttcsid=1750959349049::psd28d6tSYdkp74YfZtz.2.1750959401621; ttcsid_CULAR4JC77U47BI945FG=1750959349049::jZ6gJ4H4ZagQR6F3fDKL.2.1750959401848; fs_uid=#o-22GV82-na1#bd55459a-254d-49d7-a67d-c3f4e9cfd8c6:665568dc-9e2c-468f-ae12-63a26b160e65:1750959276042::5#894f0fef#/1779202344; _ga_PMMWB6MFPC=GS2.1.s1750959276$o109$g1$t1750959569$j44$l0$h0; fs_lua=1.1750959575367; ph_phc_bcoaBa4uZdMp0CzXr7QhZRRpnNGgBRRZ1GStvuJVAgJ_posthog=%7B%22distinct_id%22%3A%229c82f7d3af624bee8eb13f50b920a9df%22%2C%22%24sesid%22%3A%5B1750959597266%2C%220197ad4e-42d5-7e6d-9a1d-e9adec8db737%22%2C1750959276757%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22u%22%3A%22https%3A%2F%2Fwww.heygen.com%2F%22%7D%7D",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Encoding": "identity;q=1, *;q=0",
    "Accept": "*/*",
    "Referer": "https://studio.heygen.com/text-to-speech ",  # или другая ссылка, если знаешь
    "Range": "bytes=0-"
# "accept-ranges" : "bytes",
# "content-length" : "64410",
# "content-range": "bytes 0-64409/64410",
# "content-type": "binary/octet-stream",
# "date": formatted_time,
# "etag": "08f8e95bbc1256c04b25e60dc85ff3db",
# "last-modified": formatted_time,
# "server": "AmazonS3",
# "vary": "Origin, Origin",
# "via": "1.1 e8c2cf9d03a9665aa8b199d35cadcba8.cloudfront.net (CloudFront)",
# "x-amz-cf-id": "R6fU9nQhCViv9w38dqUD64fy72flH-8-jlvlRlqnmZpfiQ-XTmQlLw==",
# "x-amz-cf-pop": "ARN53-P2",
# "x-amz-server-side-encryption": "AES256",
# "x-amz-version-id": "yUCzCt.i2m1UGJOONdzfwhm_MUFMfMoh",
# "x-cache": "Miss from cloudfront"
}
DEFAULT_VOICE_ID = "dede1f90264e44f7b28359b543a41e59"
DEFAULT_VIDEO_ID = "ae850775b7c84547b002f2cde6095c2b"
DEFAULT_SETTINGS = {
    "pitch": 0,
    "speed": 1,
    "volume": 1,
    "model": "eleven_multilingual_v2",
    "similarity": 0.01,
    "stability": 0.48,
    "style": 0.85,
    "use_speaker_boost": True,
    "tts_settings": None,
    "voice_engine_settings": {
        "type": "normal",
        "engine_type": "elevenLabs",
        "model_id": "eleven_multilingual_v2",
        "stability": 0.48,
        "similarity": 0.01,
        "style": 0.85,
        "use_speaker_boost": True
    }
}
