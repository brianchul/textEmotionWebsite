import requests
from bs4 import BeautifulSoup

def isOver18(url):
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !

    return response
    
def deleteUrlInComment(text):
    if "http" in text:
        return None
    return text

def getArticle(url):

    author_message = {}
    articleInfo = {}
    webpage = isOver18(url).text
    soup = BeautifulSoup(webpage ,"html.parser")
    metaline = soup.find_all('div', 'article-metaline')
    
    tmp = []
    for t1 in metaline:
        tmp.append(t1.find("span", "article-meta-value").getText())
        
    articleInfo['author'] = tmp[0]
    articleInfo['title'] = tmp[1]
    articleInfo['time'] = tmp[2]
    
    articles=soup.find_all('div','push')
    for article in articles:
        try:
            articleInfo['content'] = webpage[webpage.index("article-meta-tag\">時間</span>")+98:webpage.index('<span class="f2">※')]
            articleInfo['content'] = articleInfo['content'].replace("\n", "<br />")
                        
            author = article.find("span", "f3 hl push-userid").getText()
            parseComment = deleteUrlInComment(article.find("span","f3 push-content").getText().replace(":"," ").strip())
            try:
                pushTag = article.find("span","f1 hl push-tag").getText().replace(":"," ").strip()
            except:
                pushTag = article.find("span","hl push-tag").getText().replace(":"," ").strip()
                
            pushDatetime = article.find("span","push-ipdatetime").getText().strip()
            
            comment = {"pushTag": pushTag, "comment": parseComment, "pushDatetime": pushDatetime}
            if parseComment is not None:
                author_message.setdefault(author, []).append(comment)
                
        except AttributeError:
            #print("資料有誤")
            pass

    
    return articleInfo, author_message

