from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.comment import Comment
from ..util.logger import get_logger as log
from datetime import datetime


def Findall(ID=None, fromArticle=None, author=None, keywords=None):
    query = Comment.query

    if ID is not None:
        query = query.filter_by(id=ID)
    if fromArticle is not None:
        query = query.filter_by(FromArticle=fromArticle)
    if author is not None:
        query = query.filter_by(Author=author)
    if keywords is not None:
        query = query.filter_by(Keywords=keywords)

    query = query.all()

    if query:
        result = []
        for data in query:
            data.__dict__.pop("_sa_instance_state")
            data = data.__dict__
            result.append(data)
        return result, 200
    else:
        return None, 404

# cond = {id:123 , comment:"STRING"}
def Create(fromArticle, author, commentString, commentTime, commentPush, lang ):
    newComment = Comment(
        FromArticle=fromArticle,
        Author=author,
        CommentString=commentString,
        CommentTime=commentTime,
        Language=lang,
        CommentPush=commentPush
        )
    
    try:
        db.session.add(newComment)
        db.session.commit()
        return newComment.id, 200
    except InvalidRequestError:
        log().error("Unable to create comment")
        return None, 400
    except IntegrityError:
        log().error("Comment Foreign key not found")
        return None, 400
