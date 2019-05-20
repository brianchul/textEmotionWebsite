from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.article import Article
from ..util.logger import get_logger as log


def Findone(ID=None, articleUrl=None, articleAuthor=None):
    query = Article.query

    if ID is not None:
        query = query.filter_by(id=ID)
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

def Create(articleUrl, articleAuthor, content, lang):
    r,c = Findall(articleUrl, articleAuthor)
    if c == 200: return r,c

    newCommentEndorse = Article(
        ArticleUrl=articleUrl,
        ArticleAuthor=articleAuthor,
        Content=content,
        Language=lang
        )

    try:
        db.session.add(newCommentEndorse)
        db.session.commit()
        return 200
    except:
        log().error("There's an error while creating commentEndorse")
        return 500