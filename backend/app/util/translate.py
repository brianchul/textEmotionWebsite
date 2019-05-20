import requests, uuid
from ..config.conf import Config
def getTranslate(comments): 

    subscriptionKey = Config.translate_key
    constructed_url = Config.translate_base_url + Config.translate_path + Config.translate_params

    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = []
    for comment in comments:
        body.append({'text': comment})

    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    """[
            {
                'detectedLanguage': 
                {
                    'language': 'zh-Hant', 'score': 1.0
                }, 
                'translations': 
                [
                    {'text': 'can push', 'to': 'en'}
                ]
            }
        ]"""

    return response