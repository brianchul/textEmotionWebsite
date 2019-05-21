from flask import request, Blueprint
from collections import namedtuple
from ..controller import article, comment, emotionScore, user
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log
from ..util.dataWarp import jsonWarp
from ..util.translate import getTranslate
from ..util.sentiment import getSentiment
from ..util.crawler import getArticle
from ..util.urlParser import confirmPttUrl
import time

barticle = Blueprint('article', __name__)

articleFields = {"article_url"}


@barticle.route('/query', methods=['POST'])
def queryArticle():
    findOneArticle = jsonWarp(request.get_json(), articleFields, "findOneArticle")



    result, code = article.Findone(articleUrl=findOneArticle.article_url)


    if code == 200:
        result['ArticleAuthor'] = user.FindOneOrCreate(ID=result['ArticleAuthor'])['UserName']
        commentResult, _ = comment.Findall(fromArticle=result['id'])
        
        for rcomment in commentResult:
            emotionResult, _ = emotionScore.Findone(rcomment['id'])
            rcomment['emotionScore'] = emotionResult['Score']
            rcomment['Author'] = user.FindOneOrCreate(ID=rcomment['Author'])['UserName']

        integration = {'article': result, 'comment':commentResult}
        return warpResponse(response.OK, integration)

        
    elif code == 404:
        CreateArticle(findOneArticle)
        result, code = article.Findone(articleUrl=findOneArticle.article_url)


        if code == 200:
            result['ArticleAuthor'] = user.FindOneOrCreate(ID=result['ArticleAuthor'])['UserName']
            commentResult, _ = comment.Findall(fromArticle=result['id'])
            
            for rcomment in commentResult:
                emotionResult, _ = emotionScore.Findone(rcomment['id'])
                rcomment['emotionScore'] = emotionResult['Score']
                rcomment['Author'] = user.FindOneOrCreate(ID=rcomment['Author'])['UserName']

            integration = {'article': result, 'comment':commentResult}
            return warpResponse(response.OK, integration)
            
        


def CreateArticle(inputs):
    findOneArticle = inputs
    url = confirmPttUrl(findOneArticle.article_url)
    if not url: return warpResponse(response.InvalidArguments)

    
    articleContent, articleComment = getArticle(findOneArticle.article_url)
    
    articleAuthor = user.FindOneOrCreate(userName=articleContent['author'])['id']

    time.sleep(0.01)
    articleID, code = article.Create(url, articleAuthor, articleContent['title'], articleContent['content'], 'zh-Hant')

    articleYear = articleContent['time'][-4:]

    comments = {}
    for author in articleComment:
        time.sleep(0.01)
        userID = user.FindOneOrCreate(userName=author)['id']

        time.sleep(0.01)
        commentData = articleComment[author]
        for item in commentData:
            commentID, code = comment.Create(
                fromArticle=articleID,
                author=userID,
                commentString=item['comment'],
                commentTime=articleYear+"/"+item['pushDatetime'],
                commentPush=item['pushTag'],
                lang='zh-Hant')
            comments[commentID] = item['comment']
            time.sleep(0.01)

    translates = getTranslate(list(comments.values()))

    for num in range(len(translates)):
        commentKey = list(comments.keys())
        comments[commentKey[num]] = translates[num]['translations'][0]['text']
    
    sentiments = getSentiment(comments)


    for item in sentiments:
        code = emotionScore.Create(item['id'], item['score'])
        if code == 500:
            log().warn("ERROR create comment with ID: " + item['id']+ " Comment: "+comments[int(item['id'])])

    queryArticle()