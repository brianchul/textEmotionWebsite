import requests
from bs4 import BeautifulSoup

def isOver18(url):
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    print(response.text)
    return response
    
def deleteUrlInComment(text):
    if "http" in text:
        return None
    return text

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
article={}
def get_push(url):#單篇文章所有留言

    author_message = {}
    soup = BeautifulSoup(isOver18(url).text,"html.parser")
    articles=soup.find_all('div','push')
    for article in articles:
        try:
            
            author = article.find("span", "f3 hl push-userid").getText()
            parseComment = deleteUrlInComment(article.find("span","f3 push-content").getText().replace(":"," ").strip())
            pushTag = article.find("span","f1 hl push-tag").getText().replace(":"," ").strip()
            pushDatetime = article.find("span","push-ipdatetime").getText().strip()
            
            comment = {pushTag: parseComment, "pushDatetime": pushDatetime}
            if parseComment is not None:
                author_message.setdefault(author, []).append(comment)
                    
        except AttributeError:
            print("資料有誤")

    return author_message