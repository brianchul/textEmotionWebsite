import  json, requests, uuid
from ..config.conf import Config



# comments = [{id:comment}]
def getSentiment(comments):
    header = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': Config.sentiment_key,
    }

    documents = { 'documents': []}
    for key in comments:
        documents.setdefault('documents').append({"language":"en","id":str(key),"text":comments[key]})
        
    body = json.dumps(documents)

    try:
        response = requests.post(Config.sentiment_url+Config.sentiment_path, headers=header, data=body).json()
        
        return response['documents']
    except:
        return None