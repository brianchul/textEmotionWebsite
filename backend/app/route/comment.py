from flask import request, Blueprint
from ..controller import comment
from ..controller import article
from ..util.warpResponse import warpResponse, response
from ..util.logger import get_logger as log
from ..util.dataWarp import jsonWarp
from ..util.crawler import get_push


bComment = Blueprint('comment', __name__)

findCommentField = {"fromArticle", "author", "keywords"}
newCommentField = {"fromArticle",
    "author",
    "commentString",
    "commentTime",
    "lang",
    "keywords"}

@bComment.route("/", methods=['POST'])
def findArticleOrCreate():
    findComments = jsonWarp(request.get_json(), findCommentField, "findComment")

    resp, code = comment.Findall(fromArticle=findComments.fromArticle, author=findComments.author, keywords=findComments.keywords)


    if code == 200:
        return warpResponse(response.OK, resp)
    elif code == 404:
        articleResult, articleCode = article.Findone(ID=findComments.fromArticle)
        if articleCode == 200:
            craw = get_push(articleResult['ArticleUrl'])
            
        else:
            return warpResponse(response.ResourceNotFound)

        