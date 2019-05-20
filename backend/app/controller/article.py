from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.article import Article
from ..util.logger import get_logger as log

def Findone( articleUrl=None, articleAuthor=None):
    query = Article.query
    if articleUrl is not None:
        query = query.filter_by(ArticleUrl=articleUrl)
    if articleAuthor is not None:
        query = query.filter_by(ArticleAuthor=articleAuthor)
    
    query = query.one_or_none()

    if query:
        query.__dict__.pop("_sa_instance_state")
        query = query.__dict__
        
        return query, 200
    else:
        return None, 404

def Create(articleUrl, articleAuthor, articleTitle, content, lang):
    _,c = Findone(articleUrl=articleUrl, articleAuthor=articleAuthor)
    if c == 200: return c

    newCommentEndorse = Article(
        ArticleUrl=articleUrl,
        ArticleAuthor=articleAuthor,
        Content=content,
        Language=lang,
        ArticleTitle=articleTitle
        )

    try:
        db.session.add(newCommentEndorse)
        db.session.commit()
        return newCommentEndorse.id, 200
    except:
        log().error("There's an error while creating commentEndorse")
        return None, 500
