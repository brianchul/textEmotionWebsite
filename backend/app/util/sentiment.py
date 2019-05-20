import  json, requests
from ..config.conf import Config



url = 'https://japaneast.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/Sentiment'

header = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': Config.sentiment_key,
}

def getSentiment(text):
    documents = { 'documents': []}
    documents.setdefault('documents').append({"language":"en","id":"0","text":"Request body format is wrong. Make sure the json request is serialized correctly and there are no null members"})
    body = json.dumps(documents)



    response = requests.post(url+path, headers=header, json=body)
    print(response.text)

