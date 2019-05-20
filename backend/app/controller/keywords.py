from sqlalchemy.exc import InvalidRequestError, IntegrityError
from ..app import db
from ..model.keywords import Keywords
from ..util.logger import get_logger as log

def Findall(commentID):
    query = Keywords.query.filter_by(CommentID=commentID).all()

    if query:
        result = []
        for data in query:
            data.__dict__.pop("_sa_instance_state")
            data.__dict__.pop("id")
            data = data.__dict__
            result.append(data)
        return result, 200
    else:
        return None, 404

def Create(commentID, phase):

    newKeywords = Keywords(
        CommentID=commentID,
        Phase=phase
        )
    try:
        db.session.add(newKeywords)
        db.session.commit()
        return 200
    except:
        log().error("There's a error while creating UserEndorse")
        return 500
